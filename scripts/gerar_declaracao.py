# [IA] Codex (OpenAI) - preenchimento factual do template, anexos e campo de reflexão.
"""Gera prompts/DECLARACAO_IA.pdf sem assinatura ou reflexão inventadas."""
from html import escape
import io
from pathlib import Path
import re
import sys

import pymupdf
from pypdf import PdfReader
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, KeepTogether

ROOT = Path(__file__).resolve().parents[1]
TEMPLATE = ROOT / "DECLARACAO_USO_IA_Streamlit_2026-2_NOVA.pdf"
OUTPUT = ROOT / "prompts/DECLARACAO_IA.pdf"
NOME = "Adrian Michael de Araujo"
DATA = "03/11/2026"


def inspect():
    with pymupdf.open(TEMPLATE) as doc:
        for i, page in enumerate(doc):
            print("PÁGINA", i + 1, page.rect)
            for label in ["Turma", "Nome Completo", "E-mail", "Repositório", "Data de entrega", "Ferramentas utilizadas", "Uso nº", "Reflexão individual", "Nome", "Assinatura"]:
                matches = page.search_for(label)
                if matches:
                    print(label, [tuple(round(v, 1) for v in rect) for rect in matches])
            rects = sorted({tuple(round(v, 1) for v in d["rect"]) for d in page.get_drawings() if d["rect"].width > 250})
            print("RETÂNGULOS", rects[:30])


def textbox(page, rect, text, size=9, color=(0.05, 0.18, 0.3), clear=False):
    rect = pymupdf.Rect(rect)
    if clear:
        page.draw_rect(rect, fill=(1, 1, 1), color=None, overlay=True)
    if "\n" not in text and pymupdf.get_text_length(text, fontname="helv", fontsize=size) <= rect.width:
        if size * 1.4 > rect.height:
            raise ValueError(f"Altura insuficiente para {text[:30]}")
        page.insert_text((rect.x0, rect.y0 + size * 1.1), text, fontname="helv", fontsize=size, color=color)
        return
    result = page.insert_textbox(rect, text, fontname="helv", fontsize=size, color=color, overlay=True)
    if result < 0:
        raise ValueError(f"Texto não cabe: {text[:55]} em {rect}")


def paragraph_text(text):
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r"\1 (\2)", text)
    return escape(text.replace("**", "").replace("`", "").replace("—", "-").replace("–", "-"))


def appendix():
    pdfmetrics.registerFont(TTFont("ArialDoc", "C:/Windows/Fonts/arial.ttf"))
    pdfmetrics.registerFont(TTFont("ArialDocBold", "C:/Windows/Fonts/arialbd.ttf"))
    normal = ParagraphStyle("Corpo", fontName="ArialDoc", fontSize=9, leading=12, spaceAfter=4)
    heading = ParagraphStyle("Titulo", parent=normal, fontName="ArialDocBold", fontSize=12, leading=16, spaceBefore=10, spaceAfter=6)
    small = ParagraphStyle("Nota", parent=normal, textColor=colors.HexColor("#475569"))
    story = [Paragraph("ANEXO A - Registro detalhado de usos de IA", heading),
             Paragraph("Adrian Michael de Araujo | Turma 5A | 03/11/2026 | Projeto College.csv", small),
             Paragraph("Complementa a Seção 5 do template (opção B). Os arquivos citados são registros e resumos, não transcrições completas. O enquadramento e a revisão individual continuam sob responsabilidade do autor.", normal)]
    md = (ROOT / "prompts/declaracao-uso-ia.md").read_text(encoding="utf-8")
    records = md.split("## 5. Registro de usos", 1)[1].split("## 6.", 1)[0]
    for block in records.split("### ")[1:]:
        lines = [line.strip() for line in block.strip().splitlines() if line.strip()]
        title = Paragraph(paragraph_text(lines[0]), heading)
        body = [Paragraph(paragraph_text(line.lstrip("- ")), normal) for line in lines[1:]]
        story.append(KeepTogether([title, body[0]]))
        story.extend(body[1:])
    story.append(KeepTogether([Spacer(1, 12), Paragraph("Revisão e assinatura", heading),
                  Paragraph("A reflexão foi redigida com apoio do Codex, a pedido do autor e com base nos relatos fornecidos. A assistência está registrada no Uso 12. Confirmar o uso histórico de streamlit skills e revisar as declarações, escolhas e conclusões antes da assinatura. O autor confirmou testes do app publicado e revisão das métricas. A assinatura permanece pessoal e não foi inserida pela IA.", normal)]))
    stream = io.BytesIO()
    def footer(canvas, doc):
        canvas.setFont("ArialDoc", 8)
        canvas.setFillColor(colors.HexColor("#64748b"))
        canvas.drawString(42, 24, f"College | Registro factual de IA | Anexo A - {doc.page}")
    document = SimpleDocTemplate(stream, pagesize=A4, leftMargin=42, rightMargin=42, topMargin=36, bottomMargin=42)
    document.build(story, onFirstPage=footer, onLaterPages=footer)
    return stream.getvalue()


def main():
    if OUTPUT.exists():
        for field in (PdfReader(OUTPUT).get_fields() or {}).values():
            if field.get("/FT") == "/Sig" and field.get("/V"):
                raise RuntimeError("O PDF possui assinatura. Não será sobrescrito; use uma cópia não assinada.")
    doc = pymupdf.open(TEMPLATE)
    page = doc[0]
    values = {"Turma": "5A", "Nome Completo": NOME, "E-mail": "ama3@cesar.school", "Repositório": "https://github.com/AdrianMichael5/AVD-20262-pratica-streamlit", "Data de entrega": DATA}
    for label, value in values.items():
        rect = page.search_for(label)[-1]
        size = 8 if label == "Repositório" else 9
        assert pymupdf.get_text_length(value, fontname="helv", fontsize=size) < 355
        page.draw_rect((180, rect.y0 - 1, 537, rect.y1 + 1), fill=(1, 1, 1), color=None)
        page.insert_text((184, rect.y1 - 2), value, fontname="helv", fontsize=size, color=(0.05, 0.18, 0.3))
    # Campos e registros das páginas seguintes são preenchidos após conferir o layout original.
    tools = [
        ("Claude Code", "Versão/plano: ver Anexo A", "Implementação médica histórica"),
        ("Colab AI / Gemini", "Versão/plano não informado", "EDA College e textos preexistentes"),
        ("Codex (OpenAI)", "Versão/plano não confirmado", "Adaptação College, testes, PDF e Git"),
        ("streamlit skills", "Uso histórico a confirmar", "Codex não utilizou nesta sessão"),
    ]
    # Coordenadas do template original A4; o script --inspect auxilia a conferência.
    for row, values in enumerate(tools):
        y = 323 + row * 21
        for x, width, value in zip([61, 211, 340], [143, 123, 193], values):
            textbox(doc[1], (x, y, x + width, y + 15), value, size=7.3)
    textbox(doc[1], (61, 247, 535, 257), "Uso de IA confirmado; conferir declaração geral e ressalvas do Anexo A.", size=6.5)
    # Os quatro blocos originais remetem aos registros completos, sem texto microscópico.
    for page_number, ys, uses in [(2, [319, 338, 358, 386, 414, 443, 482, 511], [1, 2]),
                                  (3, [100, 120, 139, 168, 196, 224, 264, 292], [3, 4])]:
        for index, use in enumerate(uses):
            rows = ["22/10/2026", "Claude Code, conforme histórico", "Anexo A, Uso " + str(use),
                    "Finalidade e enquadramento: ver registro no anexo.",
                    "Pedido detalhado no Anexo A, Uso " + str(use),
                    "Aproveitamento/modificações descritos no mesmo registro.",
                    "Verificação histórica relatada; revisão do autor pendente.",
                    "prompts/declaracao-uso-ia.md / Anexo A" if use == 1 else "22/10/2026"]
            for y, value in zip(ys, rows):
                top = y + index * 250
                textbox(doc[page_number], (191, top, 532, top + 14), value, size=7.2)
    # Seção 6: apoio confirmado, detalhes e ressalvas no anexo.
    for y, text in zip([692, 714, 745, 766], ["Reestruturação técnica com Codex", "Gráficos e filtros com Codex", "Cálculos/gráficos com Codex; ver ressalvas", "Preparação de deploy; publicação pendente"]):
        textbox(doc[3], (305, y, 532, y + 14), text, size=7)
    for rect in doc[3].search_for("Sim"):
        if rect.y0 > 687:
            textbox(doc[3], (rect.x0 - 12, rect.y0, rect.x0 - 3, rect.y1 + 1), "X", size=8)
    # Campo editável com a redação assistida solicitada pelo autor.
    reflection_path = ROOT / "prompts/reflexao-individual.txt"
    reflection = reflection_path.read_text(encoding="utf-8").strip() if reflection_path.exists() else ""
    if reflection:
        lines = reflection.splitlines()
        assert 8 <= len(lines) <= 15
        assert all(pymupdf.get_text_length(line, fontname="helv", fontsize=10) < 462 for line in lines)
    widget = pymupdf.Widget()
    widget.field_name = "reflexao_individual"
    widget.field_type = pymupdf.PDF_WIDGET_TYPE_TEXT
    widget.field_flags = pymupdf.PDF_TX_FIELD_IS_MULTILINE
    widget.rect = pymupdf.Rect(61, 161, 531, 342)
    widget.text_font = "Helv"
    widget.text_fontsize = 10
    widget.field_value = reflection
    doc[4].add_widget(widget)
    textbox(doc[4], (61, 476, 294, 492), NOME, size=9)
    textbox(doc[4], (457, 476, 532, 492), DATA, size=9)
    with pymupdf.open(stream=appendix(), filetype="pdf") as annex:
        doc.insert_pdf(annex)
    doc.set_metadata({"title": "Declaração de uso de IA - College", "author": NOME, "subject": "Identificação e reflexão assistida preenchidas; revisão e assinatura do autor pendentes"})
    doc.save(OUTPUT, garbage=4, deflate=True)
    doc.close()
    reader = PdfReader(OUTPUT)
    fields = reader.get_fields() or {}
    assert "reflexao_individual" in fields and fields["reflexao_individual"].get("/V", "") == reflection
    render = ROOT / "tmp/pdfs/declaracao"
    render.mkdir(parents=True, exist_ok=True)
    with pymupdf.open(OUTPUT) as rendered:
        for i, page in enumerate(rendered, 1):
            page.get_pixmap(matrix=pymupdf.Matrix(1.1, 1.1)).save(render / f"pagina-{i:02}.png")
    print(f"PDF: {OUTPUT}; páginas: {len(reader.pages)}; reflexão: {len(reflection.splitlines())} linhas, editável; assinatura não inserida.")


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    inspect() if "--inspect" in sys.argv else main()
