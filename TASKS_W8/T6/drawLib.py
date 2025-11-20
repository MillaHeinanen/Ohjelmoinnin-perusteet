from svgwrite import Drawing
from svgwrite.shapes import Rect, Circle, Polygon

def drawSquare(PDwg: Drawing, left: float, top: float, sideLength: float, color: str, strokeColor: str) -> None:
    PDwg.add(Rect(insert=(left, top), size=(sideLength, sideLength), fill =color, stroke=strokeColor))
    return None

def drawCircle(PDwg: Drawing, centerX: float, centerY: float, radius: float, color: str, stroke: str) -> None:
    PDwg.add(Circle(center=(centerX, centerY), r=radius, fill=color, stroke=stroke))
    return None

def saveSvg(PDwg: Drawing, file: str) -> None:
    PDwg.saveas(file, pretty=True, indent=2)
    return None