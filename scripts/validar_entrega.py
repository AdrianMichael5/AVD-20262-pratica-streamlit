# [IA] Codex (OpenAI) - inspeção do PDF e execução/validação técnica da EDA.
"""Inspeção do template e execução auditável da EDA.

python scripts/validar_entrega.py template
python scripts/validar_entrega.py notebook
Ferramentas de revisão: pip install -r requirements-dev.txt
"""

import argparse
import hashlib
import json
import os
from pathlib import Path
import sys
import time

ROOT = Path(__file__).resolve().parents[1]


def template():
    from pypdf import PdfReader
    import pymupdf

    path = ROOT / "DECLARACAO_USO_IA_Streamlit_2026-2_NOVA.pdf"
    reader = PdfReader(path)
    print(f"Template: {len(reader.pages)} páginas; campos interativos: {len(reader.get_fields() or {})}")
    for i, page in enumerate(reader.pages, 1):
        print(f"--- Página {i} ---\n{page.extract_text()}")
    out = ROOT / "tmp/pdfs"
    out.mkdir(parents=True, exist_ok=True)
    with pymupdf.open(path) as doc:
        for i, page in enumerate(doc, 1):
            page.get_pixmap(matrix=pymupdf.Matrix(1.5, 1.5)).save(out / f"template-{i}.png")
    print("Renderizações em tmp/pdfs/ para inspeção visual.")


def notebook():
    import nbformat
    from nbclient import NotebookClient
    from jupyter_client.kernelspec import KernelSpecManager
    import pandas as pd

    path = ROOT / "notebooks/eda.ipynb"
    csv_path = ROOT / "data/clean/dataset.csv"
    before = pd.read_csv(csv_path)
    before_bytes = csv_path.read_bytes()
    nb = nbformat.read(path, as_version=4)
    # Kernel temporário usa o mesmo Python/venv deste comando, sem instalação global.
    kernel_dir = ROOT / "tmp/jupyter/kernels/entrega"
    kernel_dir.mkdir(parents=True, exist_ok=True)
    (kernel_dir / "kernel.json").write_text(json.dumps({
        "argv": [sys.executable, "-m", "ipykernel_launcher", "-f", "{connection_file}"],
        "display_name": "Python da entrega", "language": "python",
    }), encoding="utf-8")
    os.environ["MPLBACKEND"] = "module://matplotlib_inline.backend_inline"
    os.environ["PYTHONIOENCODING"] = "utf-8"
    manager = KernelSpecManager(kernel_dirs=[str(kernel_dir.parent)])
    client = NotebookClient(
        nb, timeout=240, kernel_name="entrega", allow_errors=False,
        resources={"metadata": {"path": str(ROOT / "notebooks")}},
    )
    client.create_kernel_manager()
    client.km.kernel_spec_manager = manager
    started = time.monotonic()
    def andamento(cell, cell_index, **kwargs):
        if cell.cell_type == "code":
            print(f"Executando célula {cell_index}...", flush=True)
    client.on_cell_start = andamento
    client.execute()
    # Exportação deve reproduzir o dado do app (tolerância apenas para arredondamento de float).
    after = pd.read_csv(csv_path)
    try:
        pd.testing.assert_frame_equal(before, after, check_dtype=False, rtol=1e-12, atol=1e-12)
    finally:
        csv_path.write_bytes(before_bytes)
    nb.metadata.kernelspec = {"display_name": "Python 3", "language": "python", "name": "python3"}
    path.write_bytes(nbformat.writes(nb).replace("\r\n", "\n").encode("utf-8"))
    codes = [c for c in nb.cells if c.cell_type == "code"]
    errors = [o for c in codes for o in c.get("outputs", []) if o.output_type == "error"]
    assert not errors
    report = {
        "data": "2026-11-03", "executor": "Codex (OpenAI), solicitado por Adrian Michael",
        "python": sys.version.split()[0], "celulas_codigo": len(codes),
        "celulas_executadas": sum(c.execution_count is not None for c in codes),
        "erros": len(errors), "duracao_segundos": round(time.monotonic() - started, 3),
        "linhas": len(after), "colunas": len(after.columns),
        "csv_reproduzido": True, "csv_sha256": hashlib.sha256(before_bytes).hexdigest(),
        "notebook_sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
    }
    destination = ROOT / "entregas/execucao-notebook.json"
    destination.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser()
    parser.add_argument("acao", choices=["template", "notebook"])
    args = parser.parse_args()
    (template if args.acao == "template" else notebook)()
