# [IA] Codex (OpenAI) - inspeção limitada de arquivos/histórico antes da publicação.
"""Procura padrões conhecidos sem imprimir o conteúdo potencialmente sensível.

python scripts/auditar_publicacao.py
O resultado é uma triagem, não uma certificação de ausência de vazamento.
"""

import csv
from datetime import datetime
import json
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]
PREFIX = ["git", "-c", f"safe.directory={ROOT.as_posix()}"]
PATTERNS = {
    "chave privada": rb"-----BEGIN (?:RSA |EC |OPENSSH |DSA )?PRIVATE KEY-----",
    "token GitHub": rb"\b(?:gh[pousr]_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{50,})\b",
    "identificador de chave AWS": rb"\b(?:AKIA|ASIA)[A-Z0-9]{16}\b",
    "token OpenAI": rb"\bsk-(?:proj-|svcacct-)?[A-Za-z0-9_-]{40,}\b",
    "credencial em URL": rb"\b(?:postgres(?:ql)?|mysql|mongodb(?:\+srv)?)://[^\s/:]+:[^\s@]+@",
}
EMAIL = re.compile(rb"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b")
EXCLUDE = {".git", ".venv", "venv", "tmp", "__pycache__", ".pytest_cache"}


def git(*args):
    return subprocess.run(PREFIX + list(args), cwd=ROOT, check=True, capture_output=True).stdout


def main():
    findings, contacts, binaries = [], [], []
    def inspect(data, location):
        if b"\x00" in data or data.startswith((b"%PDF", b"\x89PNG", b"\xff\xd8")):
            binaries.append(location)
            return
        for label, pattern in PATTERNS.items():
            if re.search(pattern, data):
                findings.append({"local": location, "tipo": label})
        if EMAIL.search(data):
            contacts.append(location)

    paths = []
    for path in ROOT.rglob("*"):
        relative = path.relative_to(ROOT)
        if any(part in EXCLUDE for part in relative.parts) or not path.is_file():
            continue
        # Evita incluir os resultados anteriores na própria inspeção.
        if relative.as_posix() == "entregas/auditoria-publicacao.json":
            continue
        paths.append(relative.as_posix())
        inspect(path.read_bytes(), relative.as_posix())

    objects = git("rev-list", "--objects", "--all").decode("utf-8").splitlines()
    blob_count = 0
    for obj in objects:
        oid, _, path = obj.partition(" ")
        if git("cat-file", "-t", oid).strip() != b"blob":
            continue
        blob_count += 1
        inspect(git("cat-file", "blob", oid), f"git:{oid[:12]}:{path}")

    with (ROOT / "data/clean/dataset.csv").open(encoding="utf-8", newline="") as stream:
        reader = csv.DictReader(stream)
        columns = reader.fieldnames
        rows = list(reader)
    ignored = {}
    for item in [".env", ".streamlit/secrets.toml", ".venv/pyvenv.cfg", "tmp/teste.txt"]:
        result = subprocess.run(PREFIX + ["check-ignore", "--no-index", item], cwd=ROOT, capture_output=True)
        ignored[item] = result.returncode == 0
    report = {
        "data": datetime.now().astimezone().isoformat(timespec="seconds"),
        "executor": "Codex (OpenAI), solicitado por Adrian Michael",
        "head_local": git("rev-parse", "HEAD").decode().strip(),
        "arquivos_locais_examinados": len(paths), "blobs_historicos_examinados": blob_count,
        "padroes": list(PATTERNS), "achados_credenciais": findings,
        "arquivos_com_email_para_revisao": contacts,
        "binarios_sem_inspecao_de_conteudo": binaries,
        "protecao_gitignore": ignored,
        "csv_linhas": len(rows), "csv_colunas": columns,
        "limites": [
            "Padrões limitados: nenhum achado não prova ausência de segredos.",
            "Imagens base64, anexos e binários precisam de revisão visual; o scanner não faz OCR.",
            "Revisa objetos alcançáveis nas refs locais; não busca refs remotas, artefatos apagados do servidor ou serviços externos.",
            "Não substitui o teste do app publicado e de downloads/tooltips/mensagens de erro.",
        ],
    }
    destination = ROOT / "entregas/auditoria-publicacao.json"
    destination.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: report[k] for k in ["arquivos_locais_examinados", "blobs_historicos_examinados", "achados_credenciais", "arquivos_com_email_para_revisao", "protecao_gitignore", "csv_linhas"]}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    import sys
    sys.stdout.reconfigure(encoding="utf-8")
    main()
