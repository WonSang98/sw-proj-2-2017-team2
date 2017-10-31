import pickle
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton,
    QHBoxLayout, QVBoxLayout, QApplication, QLabel,
    QComboBox, QTextEdit, QLineEdit, QGridLayout)
from PyQt5.QtCore import Qt

class ScoreDB(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()
        self.dbfilename = 'assignment6.dat'
        self.scoredb = []
        self.readScoreDB()
        self.showScoreDB()


    def initUI(self):

        grid = QGridLayout()
        self.setLayout(grid)
        grid.setSpacing(10)

        ##모든 레이블+버튼 선언##
        name = QLabel('Name:',self)
        age = QLabel('Age:',self)
        score = QLabel('Score:',self)
        amount = QLabel('Amout:',self)

        self.key = QComboBox()
        self.key.addItem("Name")
        self.key.addItem("Age")
        self.key.addItem("Score")

        self.nameEdit = QLineEdit()
        self.ageEdit = QLineEdit()
        self.scoreEdit = QLineEdit()
        self.amountEdit = QLineEdit()

        aButton = QPushButton("Add", self)
        dButton = QPushButton("Del", self)
        fButton = QPushButton("Find", self)
        iButton = QPushButton("Inc", self)
        sButton = QPushButton("show", self)

        result = QLabel('Result:')

        aButton.clicked.connect(self.addButtonClick)
        dButton.clicked.connect(self.delButtonClick)
        fButton.clicked.connect(self.findButtonClick)
        iButton.clicked.connect(self.incButtonClick)
        sButton.clicked.connect(self.showButtonClick)

        self.allText = QTextEdit(self)


        ##모든 항목 표출##
        grid.addWidget(name, 1, 0)
        grid.addWidget(self.nameEdit, 1, 1)

        grid.addWidget(age, 1, 2)
        grid.addWidget(self.ageEdit, 1, 3)

        grid.addWidget(score, 1, 4)
        grid.addWidget(self.scoreEdit, 1, 5)

        grid.addWidget(amount, 2, 3)
        grid.addWidget(self.amountEdit, 2, 4)

        grid.addWidget(self.key, 2, 5)

        grid.addWidget(aButton, 3, 1)
        grid.addWidget(dButton, 3, 2)
        grid.addWidget(fButton, 3, 3)
        grid.addWidget(iButton, 3, 4)
        grid.addWidget(sButton, 3, 5)

        grid.addWidget(result, 4, 0)

        grid.addWidget(self.allText, 5, 0, 1, 6)


        self.setGeometry(300, 300, 400, 250)
        self.setWindowTitle('Assignment6')
        self.show()


    def closeEvent(self, event):
        self.writeScoreDB()

    def readScoreDB(self):
        try:
            fH = open(self.dbfilename, 'rb')
        except FileNotFoundError as e:
            self.scoredb = []
            return
        try:
            self.scoredb =  pickle.load(fH)
        except:
            pass
        else:
            #scoredb에서 age랑 score밸류값 int형으로 변경
            for i in self.scoredb:
                i['Age'] = int(i['Age'])
                i['Score'] = int(i['Score'])
        fH.close()

    def writeScoreDB(self):
        fH = open(self.dbfilename, 'wb')
        pickle.dump(self.scoredb, fH)
        fH.close()

    def showScoreDB(self,keyname="Score"):
        answer = ""
        for p in sorted(self.scoredb, key=lambda person: person[keyname]):
            for attr in sorted(p):
                answer += attr + "=" + str(p[attr]) + " "
            answer += "\n"
        self.allText.setText(answer)


    def addButtonClick(self):
        record = {'Name': self.nameEdit.text(), 'Age': int(self.ageEdit.text()), 'Score': int(self.scoreEdit.text())}
        self.scoredb += [record]
        self.showScoreDB()

    def delButtonClick(self):
        scdb = sorted(self.scoredb, key=lambda person: person["Name"])
        for n in range(len(scdb)):
            for p in scdb:
                if p['Name'] == self.nameEdit.text():
                    self.scoredb.remove(p)
        self.showScoreDB()

    def findButtonClick(self):
        answer = ""
        for p in sorted(self.scoredb, key=lambda person: person["Name"]):
            for attr in sorted(p):
                if p["Name"] == self.nameEdit.text():
                    answer += attr + "=" + str(p[attr]) + " "
            answer += "\n"
        self.allText.setText(answer)

    def incButtonClick(self):
        for p in sorted(self.scoredb , key=lambda person: person["Name"]):
            for attr in sorted(p):
                if p["Name"] == self.nameEdit.text():
                    p["Score"] += int(self.amountEdit.text())
        self.showScoreDB()

    def showButtonClick(self):
        self.showScoreDB(self.key.currentText())

    ##esc누르면 꺼져요.
    def keyPressEvent(self,e):
        if e.key() == Qt.Key_Escape:
            self.close()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = ScoreDB()
    sys.exit(app.exec_())

#QComboBox
#self.000 = QComboBox()
#self.000.addItem("Name")
# ''             ("Age")
# ''             ("Score")
#
#self.000.currentText( ->문자열 ("name"...)