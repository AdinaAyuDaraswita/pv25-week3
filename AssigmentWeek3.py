import sys
import random
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow
from PyQt5.QtCore import Qt, QEvent

class GerakLabel(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Task Week 3 - (F1D022030- Adina Ayu Daraswita)")
        self.setGeometry(100, 100, 600, 400)

        self.lbl_koordinat = QLabel("x: 0, y: 0", self)
        self.lbl_koordinat.setFixedSize(160, 30)
        
        
        self.posisi_label_random()

        self.setMouseTracking(True)  
        self.lbl_koordinat.setMouseTracking(True)

        self.lbl_koordinat.setAttribute(Qt.WA_Hover)
        self.lbl_koordinat.installEventFilter(self)

    def posisi_label_random(self):
        batas = 20  
        x_baru = random.randint(batas, self.width() - self.lbl_koordinat.width() - batas)
        y_baru = random.randint(batas, self.height() - self.lbl_koordinat.height() - batas)
        self.lbl_koordinat.move(x_baru, y_baru)

    def mouseMoveEvent(self, event):
        self.lbl_koordinat.setText(f"x: {event.x()}, y: {event.y()}")

    def leaveEvent(self, event):
        self.lbl_koordinat.setText("x: -, y: -")

    def eventFilter(self, obj, event):
        if obj == self.lbl_koordinat and event.type() == QEvent.HoverEnter:
            self.posisi_label_random()
        return super().eventFilter(obj, event)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GerakLabel()
    window.show()
    sys.exit(app.exec_())
