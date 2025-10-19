from PySide6.QtCore import QTimer
from pyqtgraph import PlotWidget, FillBetweenItem, mkPen, mkBrush
import numpy as np

class RealtimeGraph(PlotWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setBackground("#1a1a2e")

        self.x = np.linspace(0, 10, 200)
        self.phase = 0

        self.line = self.plot(self.x, np.sin(self.x), pen=mkPen("#3a7dff", width=2))
        self.base = self.plot(self.x, np.zeros_like(self.x))
        self.fill = FillBetweenItem(self.line, self.base, brush=mkBrush(58, 125, 255, 100))
        self.addItem(self.fill)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_plot)
        self.timer.start(30)

    def update_plot(self):
        self.phase += 0.1
        y = np.sin(self.x + self.phase)
        self.line.setData(self.x, y)
        self.base.setData(self.x, np.zeros_like(self.x))
