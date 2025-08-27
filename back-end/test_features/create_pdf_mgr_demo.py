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

from typing import Any

from PyPDF2 import PdfWriter, PdfReader
import io
import random


class PDFComponentGenerationManager:
    def __init__(self):
        self.buffer = io.BytesIO()
        self._template = SimpleDocTemplate(self.buffer)
        self._styles = getSampleStyleSheet()
        self.content = []
        self.frames = []
        self._set_pdf_font()

    def _set_pdf_font(self):
        pdfmetrics.registerFont(TTFont(name="InterNormal", filename="app/static/fonts/Inter/Inter_18pt-Regular.ttf"))
        pdfmetrics.registerFont(TTFont(name="InterBold", filename="app/static/fonts/Inter/Inter_18pt-Bold.ttf"))
        pdfmetrics.registerFont(TTFont(name="InterItalic", filename="app/static/fonts/Inter/Inter_18pt-Italic.ttf"))
        pdfmetrics.registerFont(
            TTFont(name="InterBoldItalic", filename="app/static/fonts/Inter/Inter_18pt-BoldItalic.ttf"))

        pdfmetrics.registerFontFamily(
            normal="InterNormal",
            bold="InterBold",
            italic="InterItalic",
            boldItalic="InterBoldItalic",
            family="InterNormal",
        )

        self._styles["Normal"].fontName = "InterNormal"
        self._styles["Normal"].fontSize = 20
        self._styles["Normal"].textColor = HexColor(0x0d7682)

        # log.info("Done setting custom font for PDF.")

    def create_frame(self,
                     x1: Any,
                     y1: Any,
                     width: Any,
                     height: Any,
                     leftPadding: int = 0,
                     bottomPadding: int = 0,
                     rightPadding: int = 0,
                     topPadding: int = 0,
                     id: Any = None,
                     showBoundary: int = 0) -> Frame:
        frame = Frame(x1=x1, y1=y1, width=width, height=height,
                      leftPadding=leftPadding, bottomPadding=bottomPadding,
                      rightPadding=rightPadding, topPadding=topPadding,
                      showBoundary=showBoundary, id=id, )
        self.frames.append(frame)
        return frame

    def get_paragraph_style(self,
                            name: str = 'CustomParagraph',
                            parent=None,
                            leftIndent=0,
                            fontSize=20,
                            firstLineIndent=0,
                            spaceBefore=0,
                            spaceAfter=0,
                            leading=20,
                            bulletFontName="InterNormal",
                            bulletFontSize=20,
                            textColor=None,
                            ) -> ParagraphStyle:
        return ParagraphStyle(
            name=name,
            parent=self._styles['Normal'] if parent is None else parent,
            leftIndent=leftIndent,
            fontSize=fontSize,
            firstLineIndent=firstLineIndent,
            spaceBefore=spaceBefore,
            spaceAfter=spaceAfter,
            leading=leading,
            bulletFontName=bulletFontName,
            bulletFontSize=bulletFontSize,
            textColor=HexColor(0x0d7682) if textColor is None else textColor
        )

    def create_horizontal_bar_chart(self,
                                    psychometrics_len: int,
                                    category_names: list[str],
                                    data: list[tuple[float]],
                                    width: int = 400,
                                    height: int = 340,
                                    x: int = None,
                                    y: int = None,
                                    minValue: int = None,
                                    maxValue: int = None,
                                    labelAngle: int = 0,
                                    lables_dx: int = 0,
                                    lables_dy: int = 0,
                                    ) -> Drawing:
        chart = HorizontalBarChart()
        chart.width = width
        chart.height = height
        chart.data = data
        chart.x = 0 if x is None else x
        chart.y = -200 if y is None else y
        chart.valueAxis.valueMin = 0 if minValue is None else minValue
        chart.valueAxis.valueMax = 10 if maxValue is None else maxValue
        chart.categoryAxis.labels.fontName = 'InterNormal'
        chart.categoryAxis.labels.angle = labelAngle
        chart.categoryAxis.labels.dy = lables_dy
        chart.categoryAxis.labels.dx = lables_dx
        chart.categoryAxis.categoryNames = category_names
        chart.fillColor = HexColor(0xFFFFFF)

        for i in range(0, psychometrics_len):
            color = random.randrange(0, 2 ** 24)
            chart.strokeColor = HexColor(hex(color))
            chart.bars[(0, i)].fillColor = HexColor(hex(color))
            print(hex(color), chart.bars[i].fillColor)

        # Create a Drawing object and add the chart to it
        chart_drawing = Drawing()
        chart_drawing.add(chart)
        return chart_drawing

    def create_spacer(self, height: Any = 8, width: Any = 0):
        return Spacer(height=height, width=width)

    def prepare_pdf(self):
        print(len(self.frames))
        self._template.addPageTemplates([PageTemplate(frames=self.frames)])
        self._template.build(self.content)


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

# --------- Creating Page1 Edits -----------------
user_info = PDFComponentGenerationManager()
frame = user_info.create_frame(x1=50, y1=A4[1] - 430, width=500, height=120,
                       leftPadding=30)
# user_info.frames.append(frame)
user_info_style = user_info.get_paragraph_style(leftIndent=100)

user_info.content.append(Paragraph("Tapoban Ray", user_info_style))
user_info.content.append(Spacer(height=8, width=0))
user_info.content.append(Paragraph("20", user_info_style))
user_info.content.append(Spacer(height=8, width=0))
user_info.content.append(Paragraph("Maulana Abdul Kalam Azad University of Technology", user_info_style))
user_info.prepare_pdf()

# --------------- Creating Page2 Edits ----------------
chart_and_careers = PDFComponentGenerationManager()
graph_frame = chart_and_careers.create_frame(x1=0, y1=385, width=A4[0], height=A4[1] - (A4[1] / 2),
                               leftPadding=140, bottomPadding=0,
                               rightPadding=0, topPadding=0,
                               showBoundary=10, )
careers_frame = chart_and_careers.create_frame(x1=0, y1=0, width=A4[0], height=330,
                               leftPadding=60, bottomPadding=0,
                               rightPadding=20, topPadding=0,
                               showBoundary=10)

data: list[tuple[float]] = [tuple([x["score"] for x in demo_data["psychometrics"]])]
chart = chart_and_careers.create_horizontal_bar_chart(
    x=0,
    y=-200,
    minValue=0,
    maxValue=10,
    lables_dx=-10,
    psychometrics_len=len(demo_data["psychometrics"]),
    category_names=[x["parameter"] for x in demo_data["psychometrics"]],
    data=data
)

current_style = chart_and_careers.get_paragraph_style(
    fontSize=16,
    bulletFontName="InterNormal",
    bulletFontSize=20,
    textColor=HexColor(0x222222)
)

# chart_and_careers.frames.append(graph_frame)
# chart_and_careers.frames.append(careers_frame)


careers = [f"<bullet>&bull;</bullet> <b>{x["career"]}:</b> {x["explanation"]}" for x in demo_data["careers"]]

chart_and_careers.content.append(chart)
chart_and_careers.content.append(FrameBreak())
chart_and_careers.content.append(Paragraph(careers[0], current_style))

chart_and_careers.prepare_pdf()

# ------- Preparing the output pdf ----------------
page1_pdf = PdfReader(user_info.buffer)
page2_pdf = PdfReader(chart_and_careers.buffer)
existing_pdf = PdfReader(open("Psychometric Test Report.pdf", mode="rb"))
output = PdfWriter()

page1 = existing_pdf.pages[0]
page2 = existing_pdf.pages[1]
page3 = existing_pdf.pages[2]

page1.merge_page(page1_pdf.pages[0])
page3.merge_page(page2_pdf.pages[0])
output.add_page(page1)
output.add_page(page2)
output.add_page(page3)

output_stream = open("mgr_demo.pdf", "wb")
output.write(output_stream)
output_stream.close()
