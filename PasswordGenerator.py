import sys
import string
import random
from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QSlider, QVBoxLayout, QHBoxLayout, QCheckBox, QPushButton
from PyQt6 import QtCore, QtGui
from PyQt6.QtCore import *
from PyQt6.QtGui import *

WINDOW_WIDTH = 350 #300
WINDOW_HEIGHT = 175 #150

class PassGeneratorWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowIcon(QtGui.QIcon("ProgramIcon.png"))
        outer_layout = QVBoxLayout()
        self.setWindowTitle("Password Generator")
        self.setFixedSize(WINDOW_WIDTH, WINDOW_HEIGHT)

        inner_layout = QHBoxLayout()
        self.l0 = QLabel("Password Length: ")
        inner_layout.addWidget(self.l0)
        self.l1 = QLabel("12")
        #self.l1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        inner_layout.addWidget(self.l1)

        self.slider = QSlider(Qt.Orientation.Horizontal)
        self.slider.setMinimum(4)
        self.slider.setMaximum(20)
        self.slider.setValue(12)
        self.slider.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.slider.setTickInterval(1)
        inner_layout.addWidget(self.slider)
        self.slider.valueChanged.connect(self.slider_changed)

        checkbox_layout = QHBoxLayout()
        self.checkbox1 = QCheckBox("Letters")
        checkbox_layout.addWidget(self.checkbox1)
        self.checkbox2 = QCheckBox("Numbers")
        checkbox_layout.addWidget(self.checkbox2)
        self.checkbox3 = QCheckBox("Special Characters")
        checkbox_layout.addWidget(self.checkbox3)

        outer_layout.addLayout(inner_layout)
        outer_layout.addLayout(checkbox_layout)

        self.generate = QPushButton(self)
        self.generate.setText("Generate Password")
        outer_layout.addWidget(self.generate)
        self.password = QLabel("")
        self.password.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.password.setFont(QFont("Arial", 18))
        self.password.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)
        outer_layout.addWidget(self.password)
        self.generate.clicked.connect(self.generate_password)

        self.setLayout(outer_layout)

    def slider_changed(self):
        slider_value = self.slider.value()
        self.l1.setText(str(slider_value))

    def generate_password(self):
        password_choices = ""
        password_string = ""

        if self.checkbox1.isChecked():
            password_choices += string.ascii_lowercase
            password_choices += string.ascii_uppercase
        if self.checkbox2.isChecked():
            password_choices += string.digits
        if self.checkbox3.isChecked():
            password_choices += string.punctuation

        if len(password_choices) > 0:
            password_string = ''.join(random.choices(password_choices, k=self.slider.value()))
            self.password.setText(password_string)
        else:
            self.password.setText("")

def main():
    app = QApplication([])
    window = PassGeneratorWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()