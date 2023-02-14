from PyQt5 import QtCore, QtGui, QtWidgets
import pyperclip, pyautogui, time, pyttsx3
import wolframalpha, winotify


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        app_id = "YTY8X5-UKTGJ4QRJ3"
        self.client = wolframalpha.Client(app_id)
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(361, 588)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("antivirus_p0H_icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.outputLabel = QtWidgets.QLabel(self.centralwidget)
        self.outputLabel.setGeometry(QtCore.QRect(10, 10, 341, 91))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.outputLabel.setFont(font)
        self.outputLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.outputLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.outputLabel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.outputLabel.setLineWidth(2)
        self.outputLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.outputLabel.setObjectName("outputLabel")
        self.percentageBtn = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("%"))
        self.percentageBtn.setGeometry(QtCore.QRect(10, 110, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.percentageBtn.setFont(font)
        self.percentageBtn.setObjectName("percentageBtn")
        self.cBtn = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("C"))
        self.cBtn.setGeometry(QtCore.QRect(100, 110, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.cBtn.setFont(font)
        self.cBtn.setObjectName("cBtn")
        self.arrowBtn = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.delete_it())
        self.arrowBtn.setGeometry(QtCore.QRect(190, 110, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.arrowBtn.setFont(font)
        self.arrowBtn.setObjectName("arrowBtn")
        self.divideBtn = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("/"))
        self.divideBtn.setGeometry(QtCore.QRect(280, 110, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.divideBtn.setFont(font)
        self.divideBtn.setObjectName("divideBtn")
        self.sevenBtn = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("7"))
        self.sevenBtn.setGeometry(QtCore.QRect(10, 200, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.sevenBtn.setFont(font)
        self.sevenBtn.setObjectName("sevenBtn")
        self.nineBtn = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("9"))
        self.nineBtn.setGeometry(QtCore.QRect(190, 200, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.nineBtn.setFont(font)
        self.nineBtn.setObjectName("nineBtn")
        self.mutipleBtn = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("*"))
        self.mutipleBtn.setGeometry(QtCore.QRect(280, 200, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.mutipleBtn.setFont(font)
        self.mutipleBtn.setObjectName("mutipleBtn")
        self.eightBtn = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("8"))
        self.eightBtn.setGeometry(QtCore.QRect(100, 200, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.eightBtn.setFont(font)
        self.eightBtn.setObjectName("eightBtn")
        self.fourBtn = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("4"))
        self.fourBtn.setGeometry(QtCore.QRect(10, 290, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.fourBtn.setFont(font)
        self.fourBtn.setObjectName("fourBtn")
        self.sixBtn = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("6"))
        self.sixBtn.setGeometry(QtCore.QRect(190, 290, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.sixBtn.setFont(font)
        self.sixBtn.setObjectName("sixBtn")
        self.minusBtn = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("-"))
        self.minusBtn.setGeometry(QtCore.QRect(280, 290, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.minusBtn.setFont(font)
        self.minusBtn.setObjectName("minusBtn")
        self.fiveBtn = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("5"))
        self.fiveBtn.setGeometry(QtCore.QRect(100, 290, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.fiveBtn.setFont(font)
        self.fiveBtn.setObjectName("fiveBtn")
        self.oneBtn = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("1"))
        self.oneBtn.setGeometry(QtCore.QRect(10, 380, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.oneBtn.setFont(font)
        self.oneBtn.setObjectName("oneBtn")
        self.threeBtn = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("3"))
        self.threeBtn.setGeometry(QtCore.QRect(190, 380, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.threeBtn.setFont(font)
        self.threeBtn.setObjectName("threeBtn")
        self.plusBtn = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("+"))
        self.plusBtn.setGeometry(QtCore.QRect(280, 380, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.plusBtn.setFont(font)
        self.plusBtn.setObjectName("plusBtn")
        self.twoBtn = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("2"))
        self.twoBtn.setGeometry(QtCore.QRect(100, 380, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.twoBtn.setFont(font)
        self.twoBtn.setObjectName("twoBtn")
        self.plusMinusBtn = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.minus_plus_it())
        self.plusMinusBtn.setGeometry(QtCore.QRect(10, 470, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.plusMinusBtn.setFont(font)
        self.plusMinusBtn.setObjectName("plusMinusBtn")
        self.decimalBtn = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.dot_it())
        self.decimalBtn.setGeometry(QtCore.QRect(190, 470, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.decimalBtn.setFont(font)
        self.decimalBtn.setObjectName("decimalBtn")
        self.equalBtn = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.equal_to())
        self.equalBtn.setGeometry(QtCore.QRect(280, 470, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.equalBtn.setFont(font)
        self.equalBtn.setObjectName("equalBtn")
        self.zeroBtn = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("0"))
        self.zeroBtn.setGeometry(QtCore.QRect(100, 470, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.zeroBtn.setFont(font)
        self.zeroBtn.setObjectName("zeroBtn")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, -20, 121, 51))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 361, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        engine = pyttsx3.init()

    def equal_to(self):
        if self.outputLabel.text() == "Syntax Error":
            pass
        else:
            try:
                screen = self.outputLabel.text()
                answer = eval(screen)
                self.outputLabel.setText(str(answer))
            except:
                self.outputLabel.setText("Syntax Error")

    def minus_plus_it(self):
        screen = self.outputLabel.text()
        if self.outputLabel.text() == "Syntax Error":
            pass
        else:
            if screen.startswith("-"):
                new_screen = screen.removeprefix("-")
                self.outputLabel.setText(new_screen)
            else:
                pos = len(screen) + 1
                new_screen = screen.rjust(pos, "-")
                self.outputLabel.setText(new_screen)


    def delete_it(self):
        screen = self.outputLabel.text()
        screen = screen[:-1]
        if self.outputLabel.text() == "Syntax Error":
            pass
        else:
            if len(screen) <= 0:
                self.outputLabel.setText("0")
            else:
                self.outputLabel.setText(screen)

    def indexs(self, name:str, value:str):
        try:
            indexs = name.rindex(value)
        except:
            indexs = -1
        return indexs 

    def sym_search(self, screen):
        sym = ["*", "-", "/", "+"]
        syms = ""
        for i in screen:
            if i in sym:
                syms = i
        mu = self.indexs(screen, syms)
        return mu

    def dot_it(self):
        screen = self.outputLabel.text()
        de = self.indexs(screen, ".")
        try:
            if self.outputLabel.text() == "Syntax Error":
                pass
            else:
                if "." not in screen[:-1]:
                    self.outputLabel.setText(f"{screen}.")
                else:
                    sym = ["*", "-", "/", "+"]
                    sym_count = 0
                    for i in sym:
                        if i in screen:
                            sym_count +=1
                    if sym_count > 0:
                        last_sym = self.sym_search(screen)
                        if last_sym > de:
                            self.outputLabel.setText(f"{screen}.")
                        else:
                            pass
                    else:
                        pass

            
        except Exception as e:
            print(e)
            pass 
    
    def answers(self, question):
        try:
            res = self.client.query(question)
            answer = next(res.results).text
            self.say(answer)
            print(f"Q: {answer}")
            print(F"A: {answer}")
        except Exception as e:
            self.say("we need internet connection to work properly.")
            print(e)
    
    def say(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

    def press_it(self, pressed):
        if pressed == "C":
            self.outputLabel.setText("0")
        elif pressed == "%":
            v1 = pyperclip.paste()
            self.answers(v1)
        else:
            if self.outputLabel.text() == "Syntax Error":
                pass
            else:
                if self.outputLabel.text() == "0":
                    self.outputLabel.setText("")
                self.outputLabel.setText(f"{self.outputLabel.text()}{pressed}")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator"))
        self.outputLabel.setText(_translate("MainWindow", "0"))
        self.percentageBtn.setText(_translate("MainWindow", "%"))
        self.cBtn.setText(_translate("MainWindow", "C"))
        self.arrowBtn.setText(_translate("MainWindow", "<<"))
        self.divideBtn.setText(_translate("MainWindow", "/"))
        self.sevenBtn.setText(_translate("MainWindow", "7"))
        self.nineBtn.setText(_translate("MainWindow", "9"))
        self.mutipleBtn.setText(_translate("MainWindow", "x"))
        self.eightBtn.setText(_translate("MainWindow", "8"))
        self.fourBtn.setText(_translate("MainWindow", "4"))
        self.sixBtn.setText(_translate("MainWindow", "6"))
        self.minusBtn.setText(_translate("MainWindow", "-"))
        self.fiveBtn.setText(_translate("MainWindow", "5"))
        self.oneBtn.setText(_translate("MainWindow", "1"))
        self.threeBtn.setText(_translate("MainWindow", "3"))
        self.plusBtn.setText(_translate("MainWindow", "+"))
        self.twoBtn.setText(_translate("MainWindow", "2"))
        self.plusMinusBtn.setText(_translate("MainWindow", "+/-"))
        self.decimalBtn.setText(_translate("MainWindow", "."))
        self.equalBtn.setText(_translate("MainWindow", "="))
        self.zeroBtn.setText(_translate("MainWindow", "0"))
        self.label.setText(_translate("MainWindow", "created by yembot"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
