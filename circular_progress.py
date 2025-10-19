# circular_progress.py
from PySide6.QtCore import Qt, QRectF, Property, QSize
from PySide6.QtGui import QPainter, QPen, QColor
from PySide6.QtWidgets import QWidget

class CircularProgress(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._min = 0
        self._max = 100
        self._val = 42
        self._thickness = 10
        self._startAngle = -90        # grados (arriba = -90)
        self._clockwise = True
        self._capRound = True
        self._trackColor = QColor("#1a2340")
        self._progressColor = QColor("#3a7dff")
        self.setMinimumSize(80, 80)

    # ----- Propiedades (para que Designer pueda cambiarlas) -----
    def getMinimum(self): return self._min
    def setMinimum(self, v): self._min = v; self.update()

    def getMaximum(self): return self._max
    def setMaximum(self, v): self._max = v; self.update()

    def getValue(self): return self._val
    def setValue(self, v):
        self._val = max(self._min, min(v, self._max))
        self.update()

    def getThickness(self): return self._thickness
    def setThickness(self, v): self._thickness = max(1, v); self.update()

    def getStartAngle(self): return self._startAngle
    def setStartAngle(self, v): self._startAngle = v; self.update()

    def isClockwise(self): return self._clockwise
    def setClockwise(self, v: bool): self._clockwise = bool(v); self.update()

    def isCapRound(self): return self._capRound
    def setCapRound(self, v: bool): self._capRound = bool(v); self.update()

    def getTrackColor(self): return self._trackColor
    def setTrackColor(self, c): self._trackColor = QColor(c); self.update()

    def getProgressColor(self): return self._progressColor
    def setProgressColor(self, c): self._progressColor = QColor(c); self.update()

    minimum = Property(int, getMinimum, setMinimum)
    maximum = Property(int, getMaximum, setMaximum)
    value = Property(int, getValue, setValue)
    thickness = Property(int, getThickness, setThickness)
    startAngle = Property(int, getStartAngle, setStartAngle)
    clockwise = Property(bool, isClockwise, setClockwise)
    capRound = Property(bool, isCapRound, setCapRound)
    trackColor = Property(QColor, getTrackColor, setTrackColor)
    progressColor = Property(QColor, getProgressColor, setProgressColor)

    def sizeHint(self): return QSize(120, 120)

    # ----- Dibujo -----
    def paintEvent(self, _):
        w = min(self.width(), self.height())
        margin = self._thickness / 2 + 1
        rect = QRectF(margin, margin, w - 2*margin, w - 2*margin)

        # Ajuste centrado si el widget no es cuadrado
        if self.width() > self.height():
            dx = (self.width() - w) / 2
            rect.translate(dx, 0)
        elif self.height() > self.width():
            dy = (self.height() - w) / 2
            rect.translate(0, dy)

        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing, True)

        # Pista
        pen = QPen(self._trackColor, self._thickness, Qt.SolidLine,
                   Qt.RoundCap if self._capRound else Qt.FlatCap)
        painter.setPen(pen)
        painter.drawEllipse(rect)

        # Progreso
        rng = max(1, self._max - self._min)
        pct = (self._val - self._min) / rng
        span_deg = pct * 360.0
        if self._clockwise:
            span_deg = -span_deg  # Qt dibuja CCW si span positivo

        pen.setColor(self._progressColor)
        painter.setPen(pen)

        # Qt trabaja en "grados * 16"
        start_deg16 = int(self._startAngle * 16)
        span_deg16 = int(span_deg * 16)
        painter.drawArc(rect, start_deg16, span_deg16)
