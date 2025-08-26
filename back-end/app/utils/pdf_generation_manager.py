import os
from typing import Any

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

from ..logging import log


class PDFComponentGenerationManager:
    """Provide fields and methods to generate the psychometric report pdf."""
    def __init__(self):
        self.buffer = io.BytesIO()
        self.template = SimpleDocTemplate(self.buffer)
        self.styles = getSampleStyleSheet()
        self.content = []
        self.frames = []
        self._set_pdf_font()

    def _set_pdf_font(self):
        """Run in constructor to initialise reportlab pdfmetrics with custom font family and its values."""
        base_dir = os.path.dirname(__file__)
        regular_font_path = os.path.join(base_dir, "../", "static", "fonts", "Inter", "Inter_18pt-Regular.ttf")
        bold_font_path = os.path.join(base_dir, "../", "static", "fonts", "Inter", "Inter_18pt-Bold.ttf")
        italic_font_path = os.path.join(base_dir, "../", "static", "fonts", "Inter", "Inter_18pt-Italic.ttf")
        boldItalic_font_path = os.path.join(base_dir, "../", "static", "fonts", "Inter", "Inter_18pt-BoldItalic.ttf")

        pdfmetrics.registerFont(TTFont(name="InterNormal", filename=regular_font_path))
        pdfmetrics.registerFont(TTFont(name="InterBold", filename=bold_font_path))
        pdfmetrics.registerFont(TTFont(name="InterItalic", filename=italic_font_path))
        pdfmetrics.registerFont(TTFont(name="InterBoldItalic", filename=boldItalic_font_path))

        pdfmetrics.registerFontFamily(
            normal="InterNormal",
            bold="InterBold",
            italic="InterItalic",
            boldItalic="InterBoldItalic",
            family="InterNormal",
        )

        self.styles["Normal"].fontName = "InterNormal"
        self.styles["Normal"].fontSize = 20
        self.styles["Normal"].textColor = HexColor(0x0d7682)

        log.info("Done setting custom font for PDF.")

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
            parent=self.styles['Normal'] if parent is None else parent,
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
                                    data: list[tuple[float, ...]],
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

        # Create a Drawing object and add the chart to it
        chart_drawing = Drawing()
        chart_drawing.add(chart)
        return chart_drawing

    def create_spacer(self, height: Any = 8, width: Any = 0):
        return Spacer(height=height, width=width)

    def prepare_pdf(self):
        self.template.addPageTemplates([PageTemplate(frames=self.frames)])
        self.template.build(self.content)
