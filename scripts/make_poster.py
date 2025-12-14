"""Generate a simple one-page PDF poster from the Jülich proposal text.

This uses ReportLab to produce a basic PDF; it's intentionally minimal and meant
as a quick-export artifact for meetings/presentations.
"""
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer

def main():
    doc = SimpleDocTemplate("docs/Juelich_PROPOSAL.pdf", pagesize=A4)
    styles = getSampleStyleSheet()
    story = []
    with open("docs/Juelich_PROPOSAL.md", "r", encoding="utf8") as fh:
        text = fh.read()
    for line in text.splitlines():
        if not line.strip():
            story.append(Spacer(1, 6))
            continue
        story.append(Paragraph(line.replace("\n", "<br/>"), styles["Normal"]))
    doc.build(story)
    print("Wrote docs/Juelich_PROPOSAL.pdf")


if __name__ == "__main__":
    main()
