import sys
from PySide6.QtWidgets import QMainWindow,QApplication,QHBoxLayout,QVBoxLayout,QLabel,QWidget,QPushButton,QProgressBar
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from websitelinks import *
from readval import *

class Mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()

# Basic Info for the app filled.!
        self.setWindowTitle("Striker ")
        self.setWindowIcon(QIcon("icons8-fire.gif"))
        self.setFixedSize(300,450)

#Content
#Layouts.
        linkVLayout = QVBoxLayout()
        hLayout = QHBoxLayout()
        butonVLayout = QVBoxLayout()
        btnPlusLink = QHBoxLayout()
        finalLayout = QVBoxLayout()
# -------------------------------
# header for the show Score
        self.ScoreLable = QLabel("Strike:")
        hLayout.addWidget(self.ScoreLable)
        self.ScoreLable.setAlignment(Qt.AlignmentFlag.AlignCenter)


#progress Bar with Score
        self.Pbar = QProgressBar()
        self.flreader = fileReader()
        self.Pbar.setRange(0,100)
        self.Pbar.setValue(int(fileReader().readValue()))
        hLayout.addWidget(self.Pbar)

        headerWidget = QWidget()
        headerWidget.setLayout(hLayout)

# Links. and buttons.
        self.leetName = QLabel("LeetCode")
        self.chefName = QLabel("CodeChef")
        self.hackName = QLabel("HackrRank")
        self.soloName = QLabel("SoloLearn")
        linkVLayout.addWidget(self.leetName)
        linkVLayout.addWidget(self.chefName)
        linkVLayout.addWidget(self.hackName)
        linkVLayout.addWidget(self.soloName)

        linkWidget = QWidget()
        linkWidget.setLayout(linkVLayout)

#Buttons.      
        self.leetbtn = QPushButton("LeetCode")
        self.chefbtn = QPushButton("CodeChef")
        self.hackbtn = QPushButton("HackrRank")
        self.solobtn = QPushButton("SoloLearn")


        butonVLayout.addWidget(self.leetbtn)
        butonVLayout.addWidget(self.chefbtn)
        butonVLayout.addWidget(self.hackbtn)
        butonVLayout.addWidget(self.solobtn)

#button methods
        # self.leetbtn.clicked.connect(weblink().printf())
        def link_pbar(plate_form:str):
            val = weblink().linkOpen(plate_form)
            self.Pbar.setValue(int(fileReader().readValue()))

        self.leetbtn.clicked.connect(lambda:link_pbar("leet"))
        self.chefbtn.clicked.connect(lambda:link_pbar("chef"))
        self.hackbtn.clicked.connect(lambda:link_pbar("hack"))
        self.solobtn.clicked.connect(lambda:link_pbar("solo"))

        



        btnWidget = QWidget()
        btnWidget.setLayout(butonVLayout)

        btnPlusLink.addWidget(linkWidget)
        btnPlusLink.addWidget(btnWidget)
        # setting btn and link widget in single layout.!
        btnPlusLinkWidget = QWidget()
        btnPlusLinkWidget.setLayout(btnPlusLink)

#finalLayout connect to the other layouts.!
        finalLayout.addWidget(headerWidget)
        finalLayout.addWidget(btnPlusLinkWidget)

#final Widget.
        finalWidget = QWidget()
        finalWidget.setLayout(finalLayout)
        self.setCentralWidget(finalWidget)



app = QApplication()
window = Mainwindow()
window.show()

sys.exit(app.exec())