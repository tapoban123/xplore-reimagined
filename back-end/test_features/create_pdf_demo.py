import os.path

from PyPDF2 import PdfWriter, PdfReader
import io
import random

from reportlab.graphics.charts.barcharts import HorizontalBarChart
from reportlab.graphics.shapes import Drawing
from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, FrameBreak
from reportlab.platypus.doctemplate import PageTemplate
from reportlab.platypus.frames import Frame

# file_name = f"report_123.pdf"
# pdf = canvas.Canvas(file_name, pagesize=A4)

demo_data = {
    "careers": [
        {
            "career": "Psychologist/Therapist",
            "explanation": "Your high empathy, emotional intelligence, and interest in human behavior align perfectly with helping individuals understand and improve their well-being."
        },
        {
            "career": "UX Designer/Researcher",
            "explanation": "You combine creativity, attention to detail, and empathy to design user-friendly experiences, aligning with your design interest and problem-solving skills."
        },
        {
            "career": "Non-profit Program Manager/Coordinator",
            "explanation": "Your leadership in organizing, strong communication, empathy, and desire to help others make a significant difference in a mission-driven environment."
        }
    ],
    "psychometrics": [
        {
            "parameter": "Analytical Thinking",
            "score": 8.5
        },
        {
            "parameter": "Creativity",
            "score": 9
        },
        {
            "parameter": "Emotional Intelligence",
            "score": 9.5
        },
        {
            "parameter": "Leadership",
            "score": 7.5
        },
        {
            "parameter": "Communication Skills",
            "score": 8.5
        },
        {
            "parameter": "Risk-taking",
            "score": 4
        },
        {
            "parameter": "Attention to Detail",
            "score": 8.5
        },
        {
            "parameter": "Problem-solving",
            "score": 8.5
        },
        {
            "parameter": "Empathy",
            "score": 9.5
        },
        {
            "parameter": "Teamwork",
            "score": 6.5
        },
        {
            "parameter": "Independence",
            "score": 8
        },
        {
            "parameter": "Decision-making",
            "score": 8
        },
        {
            "parameter": "STEM Interest",
            "score": 4
        },
        {
            "parameter": "Humanities Interest",
            "score": 9.5
        },
        {
            "parameter": "Business Interest",
            "score": 3
        },
        {
            "parameter": "Design/Arts Interest",
            "score": 8
        },
        {
            "parameter": "Social Work Interest",
            "score": 9.5
        }
    ],
    "report": "https://res.cloudinary.com/dduagzkor/raw/upload/v1756108749/report_841515a0458e42b091b3a8b677f39234.pdf"
}
# ------ Page 1 ------
page1_buffer = io.BytesIO()
doc = SimpleDocTemplate(page1_buffer, pagesize=A4)

pdfmetrics.registerFont(TTFont(name="InterNormal", filename="Inter/static/Inter_18pt-Regular.ttf"))
pdfmetrics.registerFont(TTFont(name="InterBold", filename="Inter/static/Inter_18pt-Bold.ttf"))
pdfmetrics.registerFont(TTFont(name="InterItalic", filename="Inter/static/Inter_18pt-Italic.ttf"))
pdfmetrics.registerFont(TTFont(name="InterBoldItalic", filename="Inter/static/Inter_18pt-BoldItalic.ttf"))

pdfmetrics.registerFontFamily(
    normal="InterNormal",
    bold="InterBold",
    italic="InterItalic",
    boldItalic="InterBoldItalic",
    family="InterNormal",
)
styles = getSampleStyleSheet()

styles["Normal"].fontName = "InterNormal"
styles["Normal"].fontSize = 20
styles["Normal"].textColor = HexColor(0x0d7682)

frame = Frame(x1=50, y1=A4[1] - 430, width=500, height=120,
              leftPadding=30, bottomPadding=0,
              rightPadding=0, topPadding=0,
              showBoundary=0)

custom_style = ParagraphStyle(
    name='CustomParagraph',
    parent=styles['Normal'],
    leftIndent=100,
    firstLineIndent=0,
    spaceBefore=0,
    spaceAfter=0,
    leading=20
)

content = []
content.append(Paragraph("Tapoban Ray", custom_style))
content.append(Spacer(height=8, width=0))
content.append(Paragraph("20", custom_style))
content.append(Spacer(height=8, width=0))
content.append(Paragraph("Maulana Abdul Kalam Azad University of Technology", custom_style))
doc.addPageTemplates([PageTemplate(frames=[frame])])
doc.build(content)
# page1_buffer.seek(0)
# --------------------


# ------ Page 3 (With graphs & careers) -------
page2_buffer = io.BytesIO()
page2 = SimpleDocTemplate(page2_buffer, pagesize=A4)
data = [tuple([x["score"] for x in demo_data["psychometrics"]])]

# Define the chart
chart = HorizontalBarChart()
chart.width = 400
chart.height = 340
chart.data = data
chart.x = 0
chart.y = -200
chart.valueAxis.valueMin = 0
chart.valueAxis.valueMax = 10

chart.categoryAxis.labels.fontName = 'InterNormal'
chart.categoryAxis.labels.angle = 0
# chart.categoryAxis.labels.dy = -30
chart.categoryAxis.labels.dx = -10
chart.categoryAxis.categoryNames = ['Ying', 'Yang']
chart.categoryAxis.categoryNames = [x["parameter"] for x in demo_data["psychometrics"]]
chart.fillColor = HexColor(0xFFFFFF)

for i in range(0, len(demo_data["psychometrics"])):
    color = random.randrange(0, 2 ** 24)
    chart.strokeColor = HexColor(hex(color))
    chart.bars[(0, i)].fillColor = HexColor(hex(color))
    print(hex(color), chart.bars[i].fillColor)

# Create a Drawing object and add the chart to it
drawing = Drawing()
drawing.add(chart)
# Add the Drawing to the PDF document
# pdf = canvas.Canvas(page2_buffer, pagesize=A4)
# drawing.drawOn(pdf, 0, 0)
# pdf.save()
# page2_buffer.seek(0)

# ---------- Careers frame ---------------
# careers_buffer = io.BytesIO()
# careers_template = SimpleDocTemplate(careers_buffer, pagesize=A4)


graph_frame = Frame(x1=0, y1=385, width=A4[0], height=A4[1] - (A4[1] / 2),
                    leftPadding=140, bottomPadding=0,
                    rightPadding=0, topPadding=0,
                    showBoundary=0)

careers_frame = Frame(x1=0, y1=0, width=A4[0], height=330,
                      leftPadding=60, bottomPadding=0,
                      rightPadding=20, topPadding=0,
                      showBoundary=0)

careers_style = ParagraphStyle(
    name='CustomParagraph',
    parent=styles['Normal'],
    leftIndent=0,
    fontSize=16,
    firstLineIndent=0,
    spaceBefore=0,
    spaceAfter=0,
    leading=20,
    bulletFontName="InterNormal",
    bulletFontSize=20,
    textColor=HexColor(0x222222)
)

careers = [f"<bullet>&bull;</bullet> <b>{x["career"]}:</b> {x["explanation"]}" for x in demo_data["careers"]]

careers_content = []
careers_content.append(drawing)
careers_content.append(FrameBreak())
careers_content.append(Paragraph(careers[0], careers_style))
careers_content.append(Spacer(height=8, width=0))
careers_content.append(Paragraph(careers[1], careers_style))
careers_content.append(Spacer(height=8, width=0))
careers_content.append(Paragraph(careers[2], careers_style))

# careers_content.append(Paragraph("Tapoban Ray", custom_style))
# careers_content.append(Spacer(height=8, width=0))
# careers_content.append(Paragraph("20", custom_style))
# careers_content.append(Spacer(height=8, width=0))
# careers_content.append(Paragraph("Maulana Abdul Kalam Azad University of Technology", custom_style))
page2.addPageTemplates([PageTemplate(frames=[graph_frame, careers_frame])])
page2.build(careers_content)
# page2_buffer.seek(0)


# ------- Preparing the output pdf ----------------
page1_pdf = PdfReader(page1_buffer)
page2_pdf = PdfReader(page2_buffer)

base_dir = os.path.dirname(__file__)
template_path = os.path.join(base_dir, "Psychometric Test Report.pdf")
print(template_path)
existing_pdf = PdfReader(open(template_path, mode="rb"))

output = PdfWriter()

page1 = existing_pdf.pages[0]
page2 = existing_pdf.pages[1]
page3 = existing_pdf.pages[2]

page1.merge_page(page1_pdf.pages[0])
page3.merge_page(page2_pdf.pages[0])
output.add_page(page1)
output.add_page(page2)
output.add_page(page3)

output_stream = open("new_pdf.pdf", "wb")
output.write(output_stream)
output_stream.close()

#
# pdf.setTitle(document_title)
# pdf.drawCentredString(y=770, text=title)
# pdf.drawCentredString(y=720, text=subtitle)
#
# text = pdf.beginText(40, 680)
# for line in text_lines:
#     text.textLine(line)
# pdf.drawText(text)
# pdf.showPage()
# pdf.save()
