import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QDialog, QLabel, QLineEdit
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt
from math import *
from sympy import *
from sympy.plotting import plot, plot_parametric

import globalFunctions
from globalFunctions import *


class WindowChoose(QWidget):
    def __init__(self):
        super().__init__()
         
        self.setGeometry(500, 200, 350, 220)
        self.setWindowTitle("Iscrtavanje pravih")
        self.setWindowIcon(QIcon('icons/icon.jpg'))
        
        self.setFixedHeight(220)
        self.setFixedWidth(350)


        self.labelTxt = QLabel("Odaberite način unosa podataka za prave:", self)
        self.labelTxt.setGeometry(40, 30, 270, 20)
        self.labelTxt.setWordWrap(True)
        self.labelTxt.setAlignment(Qt.AlignCenter)
        
        self.btnCoord = QPushButton("Preko koordinata tačaka", self)
        self.btnCoord.setGeometry(85, 80, 180, 35)
        self.btnCoord.clicked.connect(self.clicked_btnCoord)
        
        self.btnSlopeIntercept = QPushButton("Preko nagiba i odsječka", self)
        self.btnSlopeIntercept.setGeometry(85, 135, 180, 35)
        self.btnSlopeIntercept.clicked.connect(self.clicked_btnSlopeIntercept)
        
    def clicked_btnCoord(self):
        windowCoord.show()
        self.close()
    
    def clicked_btnSlopeIntercept(self):
        windowSlopeIntercept.show()
        self.close()
        

class WindowCoordinates(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setGeometry(300, 200, 675, 300)
        self.setWindowTitle("Iscrtavanje pravih preko koordinata")
        self.setWindowIcon(QIcon('icons/icon.jpg'))
        
        self.setFixedHeight(300)
        self.setFixedWidth(675)
        
        
        self.labelOne = QLabel("Prava 1:", self)
        self.labelOne.setGeometry(125, 30, 70, 20)
        self.labelOne.setFont(QFont("Sanserif", 14))
        
        self.labelX11 = QLabel("X11:", self)
        self.labelX11.setGeometry(35, 80, 30, 30)
        self.inputX11 = QLineEdit(self)
        self.inputX11.setGeometry(70, 80, 60, 30)
        
        self.labelY11 = QLabel("Y11:", self)
        self.labelY11.setGeometry(185, 80, 30, 30)
        self.inputY11 = QLineEdit(self)
        self.inputY11.setGeometry(220, 80, 60, 30)
        
        self.labelX12 = QLabel("X12:", self)
        self.labelX12.setGeometry(35, 140, 30, 30)
        self.inputX12 = QLineEdit(self)
        self.inputX12.setGeometry(70, 140, 60, 30)
        
        self.labelY12 = QLabel("Y12:", self)
        self.labelY12.setGeometry(185, 140, 30, 30)
        self.inputY12 = QLineEdit(self)
        self.inputY12.setGeometry(220, 140, 60, 30)
        
        
        self.labelTwo = QLabel("Prava 2:", self)
        self.labelTwo.setGeometry(485, 30, 70, 20)
        self.labelTwo.setFont(QFont("Sanserif", 14))
        
        self.labelX21 = QLabel("X21:", self)
        self.labelX21.setGeometry(395, 80, 30, 30)
        self.inputX21 = QLineEdit(self)
        self.inputX21.setGeometry(430, 80, 60, 30)
        
        self.labelY21 = QLabel("Y21:", self)
        self.labelY21.setGeometry(545, 80, 30, 30)
        self.inputY21 = QLineEdit(self)
        self.inputY21.setGeometry(580, 80, 60, 30)
        
        self.labelX22 = QLabel("X22:", self)
        self.labelX22.setGeometry(395, 140, 30, 30)
        self.inputX22 = QLineEdit(self)    
        self.inputX22.setGeometry(430, 140, 60, 30)    
            
        self.labelY22 = QLabel("Y22:", self)
        self.labelY22.setGeometry(545, 140, 30, 30)
        self.inputY22 = QLineEdit(self) 
        self.inputY22.setGeometry(580, 140, 60, 30)
        
        
        self.btnBackCoord = QPushButton("NAZAD", self)
        self.btnBackCoord.setGeometry(210, 220, 120, 35)
        self.btnBackCoord.clicked.connect(self.clicked_back_coord)
        
        
        self.btnDrawCoord = QPushButton("POTVRDI", self)
        self.btnDrawCoord.setGeometry(345, 220, 120, 35)
        self.btnDrawCoord.clicked.connect(self.clicked_submit_coord)
        
    def clicked_back_coord(self):
        windowChoose.show()
        self.close()
        
    def clicked_submit_coord(self):
        
        dictInputs = {}
        dictInputs['x11'] = self.inputX11.text()
        dictInputs['x12'] = self.inputX12.text()
        dictInputs['y11'] = self.inputY11.text()
        dictInputs['y12'] = self.inputY12.text()
        
        dictInputs['x21'] = self.inputX21.text()
        dictInputs['x22'] = self.inputX22.text()
        dictInputs['y21'] = self.inputY21.text()
        dictInputs['y22'] = self.inputY22.text()
        
        messageInvalidInput = invalidInputMessage(dictInputs, 'coordinates')
        
        if messageInvalidInput != '':
            dialogInvalidInput.labelWarning.setText(messageInvalidInput)
            dialogInvalidInput.show()
            return 0
        
        line1 = setLinFuncFromPoints(dictInputs['x11'], dictInputs['y11'], dictInputs['x12'], dictInputs['y12'])
        
        line2 = setLinFuncFromPoints(dictInputs['x21'], dictInputs['y21'], dictInputs['x22'], dictInputs['y22'])
        
        drawPlot(line1, line2)
        
        return 1


class WindowSlopeIntercept(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setGeometry(350, 200, 500, 360)
        self.setWindowTitle("Iscrtavanje pravih preko nagiba i odsječka")
        self.setWindowIcon(QIcon('icons/icon.jpg'))
    
        self.setFixedHeight(360)
        self.setFixedWidth(500)
        

        self.labelOne = QLabel("Prava 1:", self)
        self.labelOne.setGeometry(100, 30, 70, 20)
        self.labelOne.setFont(QFont("Sanserif", 14))
        
        self.labelAngle1 = QLabel("ugao1:", self)
        self.labelAngle1.setGeometry(70, 80, 50, 25)
        self.inputAngle1 = QLineEdit(self)
        self.inputAngle1.setGeometry(120, 80, 60, 30)
        
        self.labelIntercept1 = QLabel("odsječak1:", self)
        self.labelIntercept1.setGeometry(50, 140, 70, 25)
        self.inputIntercept1 = QLineEdit(self)
        self.inputIntercept1.setGeometry(120, 140, 60, 30)
        
        
        self.labelTwo = QLabel("Prava 2:", self)
        self.labelTwo.setGeometry(330, 30, 70, 20)
        self.labelTwo.setFont(QFont("Sanserif", 14))
        
        self.labelAngle2 = QLabel("ugao2:", self)
        self.labelAngle2.setGeometry(300, 80, 50, 25)
        self.inputAngle2 = QLineEdit(self)
        self.inputAngle2.setGeometry(350, 80, 60, 30)
        
        self.labelIntercept2 = QLabel("odsječak2:", self)
        self.labelIntercept2.setGeometry(280, 140, 70, 25)
        self.inputIntercept2 = QLineEdit(self)
        self.inputIntercept2.setGeometry(350, 140, 60, 30)

        self.labelNote = QLabel("NAPOMENA: Za uglove je potrebno unijeti vrijednosti u stepenima(°) od 0 do 360.\nVAŽNO: Ukoliko unesete 90 ili 270 vrijednost odsječka biće vrijednost u kojoj prava presjeca x osu, a ne y osu!", self)
        self.labelNote.setGeometry(50, 190, 400, 70)
        self.labelNote.setWordWrap(True)
        self.labelNote.setAlignment(Qt.AlignCenter)

        self.btnBackSlopeIntercept = QPushButton("NAZAD", self)
        self.btnBackSlopeIntercept.setGeometry(120, 290, 120, 35)
        self.btnBackSlopeIntercept.clicked.connect(self.clicked_back_slope_intercept)

        self.btnDrawSlopeIntercept = QPushButton("POTVRDI", self)
        self.btnDrawSlopeIntercept.setGeometry(250, 290, 120, 35)
        self.btnDrawSlopeIntercept.clicked.connect(self.clicked_submit_slope_intercept)
        
    def clicked_back_slope_intercept(self):
        windowChoose.show()
        self.close()
        
    def clicked_submit_slope_intercept(self):
        
        dictInputs = {}
        dictInputs['ugao1'] = self.inputAngle1.text()
        dictInputs['odsjecak1'] = self.inputIntercept1.text()
        dictInputs['ugao2'] = self.inputAngle2.text()
        dictInputs['odsjecak2'] = self.inputIntercept2.text()
        
        messageInvalidInput = invalidInputMessage(dictInputs, 'slope_intercept')
        
        if messageInvalidInput != '':
            dialogInvalidInput.labelWarning.setText(messageInvalidInput)
            dialogInvalidInput.show()
            return 0
        
        line1 = setLinFuncFromSlopeIntercept(dictInputs['ugao1'], dictInputs['odsjecak1'])
        
        line2 = setLinFuncFromSlopeIntercept(dictInputs['ugao2'], dictInputs['odsjecak2'])
        
        drawPlot(line1, line2)
        
        return 1
		
		
class DialogInvalidInput(QDialog):
    def __init__(self):
        super().__init__()
        
        self.setGeometry(500, 220, 400, 160)
        self.setWindowTitle("Upozorenje")
        self.setWindowIcon(QIcon('icons/warning.png'))
        
        self.setFixedHeight(160)
        self.setFixedWidth(400)
        
        self.labelWarning = QLabel("", self)
        self.labelWarning.setGeometry(40, 20, 320, 50)
        self.labelWarning.setWordWrap(True)
        self.labelWarning.setAlignment(Qt.AlignCenter)
        
        self.btnOK = QPushButton("OK", self)
        self.btnOK.setGeometry(160, 90, 80, 35)
        self.btnOK.clicked.connect(self.clicked_ok)
        
    def clicked_ok(self):
        self.close()


if __name__ == '__main__':
	app = QApplication(sys.argv)
	windowChoose = WindowChoose()
	windowChoose.show()
	windowCoord = WindowCoordinates()
	windowSlopeIntercept = WindowSlopeIntercept()
	dialogInvalidInput = DialogInvalidInput() 
	sys.exit(app.exec_())

