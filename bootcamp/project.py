import sqlite3
import subprocess
from PyQt5.QtWidgets import QApplication, QTableWidget, QStackedWidget, QMainWindow, QPushButton, QCommandLinkButton, QLineEdit, QListWidget, QComboBox, QFileDialog, QTableWidgetItem
from PyQt5 import uic, QtWidgets, QtCore
from PyQt5.QtCore import QTimer
from index import BarProcess, PieProcess
import sys, os, datetime, pyautogui, shutil, webbrowser

conn = sqlite3.connect("myAnalysis.db")
c = conn.cursor()

c.execute("CREATE TABLE if not exists data(ids real, title text, day text, male text, female text, week text)")

conn.commit()
conn.close()

class StatisticsUi(QMainWindow):
  def __init__(self):
    super(StatisticsUi, self).__init__()
    uiResult = uic.loadUi("statistics.ui", self)

    # self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
    # self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
    self.add_attendant = uiResult.findChild(QPushButton, "add_attendant")
    self.add_attendance_2 = uiResult.findChild(QPushButton, "add_attendance_2")
    self.view_all = uiResult.findChild(QPushButton, "view_all")
    self.delete_attendant = uiResult.findChild(QPushButton, "delete_attendant")
    self.go_back = uiResult.findChild(QPushButton, "go_back")
    self.clear_attendant = uiResult.findChild(QPushButton, "clear_attendant")
    self.view_statistics = uiResult.findChild(QPushButton, "view_statistics")
    self.view_statistics_2 = uiResult.findChild(QPushButton, "view_statistics_2")
    self.download_image = uiResult.findChild(QPushButton, "download_image")
    self.title = uiResult.findChild(QLineEdit, "Title")
    self.day = uiResult.findChild(QComboBox, "day")
    self.male = uiResult.findChild(QLineEdit, "male")
    self.female = uiResult.findChild(QLineEdit, "female")
    self.listWidget = uiResult.findChild(QListWidget, "listWidget")
    self.dropdown = uiResult.findChild(QComboBox, "dropdown")
    self.tableWidget = uiResult.findChild(QTableWidget, "tableWidget")

    self.stack = uiResult.findChild(QStackedWidget, "stackedWidget")

    self.show()
    self.dropdown.addItem("Week 1")
    self.dropdown.addItem("Week 2")
    self.dropdown.addItem("Week 3")
    self.dropdown.addItem("Week 4")
    self.dropdown.addItem("Week 5")
    self.day.addItem("Sunday")
    self.day.addItem("Monday")
    self.day.addItem("Tuesday")
    self.day.addItem("Wednesday")
    self.day.addItem("Thurday")
    self.day.addItem("Friday")
    self.day.addItem("Saturday")
    self.add_attendant.clicked.connect(self.redirect_add)
    self.add_attendance_2.clicked.connect(self.submit)
    self.view_all.clicked.connect(self.viewAll)
    self.delete_attendant.clicked.connect(self.deleteItem)
    self.go_back.clicked.connect(self.go_backs)
    self.clear_attendant.clicked.connect(self.clearItem)
    self.view_statistics.clicked.connect(self.statistics)
    self.view_statistics_2.clicked.connect(self.statistics_2)
    self.download_image.clicked.connect(self.download_images)
    self.listWidget.itemDoubleClicked.connect(self.active)

    self.grab_all()
    self.tableWidget.setColumnCount(5)
    self.stack.setCurrentIndex(2)

  def download_images(self):
    conn = sqlite3.connect("myAnalysis.db")
    c = conn.cursor()
    c.execute("SELECT * FROM data")
    records = c.fetchall()

    conn.commit()
    conn.close()

    labels = []
    boy_mean = []
    girl_mean = []

    for record in records:
      labels.append(record[2])
      boy_mean.append(int(record[3]))
      girl_mean.append(int(record[4]))

    ylabel = "numbers of Natives"
    title = "Tef Community Innovation Hub Attendance"
    flabel = "boys"
    slabel = "girls"
    processer = BarProcess(labels, boy_mean, girl_mean, ylabel, title, flabel, slabel)
    options = QFileDialog.Options()
    file = QFileDialog.getSaveFileName(self, "save attendance bar chart", "yembot.png", "All Files (*)", options = options)
    processer.save(file[0])

  def grab_all(self):
    self.listWidget.clear()
    conn = sqlite3.connect("myAnalysis.db")
    c = conn.cursor()
    c.execute("SELECT * FROM data")
    records = c.fetchall()

    conn.commit()
    conn.close()

    for record in records:
      format_str = f"{str(record[0])} - {str(record[5])} - {str(record[2])}"
      self.listWidget.addItem(format_str)

  def active(self):
    clicked = self.listWidget.currentRow()
    id = float(self.listWidget.item(clicked).text().split(" - ")[0])
    conn = sqlite3.connect("myAnalysis.db")
    c = conn.cursor()
    c.execute(f"SELECT * FROM data WHERE ids = {id}")
    records = c.fetchall()[0]
    conn.commit()
    conn.close()

    title = records[1]
    day = records[2]
    male = records[3]
    female = records[4]
    week = records[5]
    data = [int(male), int(female)]
    labels = ["Male", "Female"]
    heading = f"{week} - {day}"
    title = title
    process = PieProcess(data, labels, heading, title)

    process.show()

  def viewAll(self):
    self.tableWidget.setHorizontalHeaderLabels(("Weeks", "Days", "Male", "Female", "Total"))
    self.listWidget.clear()
    conn = sqlite3.connect("myAnalysis.db")
    c = conn.cursor()
    c.execute("SELECT * FROM data")
    records = c.fetchall()

    conn.commit()
    conn.close()
    self.tableWidget.setRowCount(len(records))
    for num, record in enumerate(records, start=0):
      self.tableWidget.setItem(num, 0, QTableWidgetItem(record[5]))
      self.tableWidget.setItem(num, 1, QTableWidgetItem(record[2]))
      self.tableWidget.setItem(num, 2, QTableWidgetItem(record[3]))
      self.tableWidget.setItem(num, 3, QTableWidgetItem(record[4]))
      self.tableWidget.setItem(num, 4, QTableWidgetItem(str(int(record[3]) + int(record[4]))))

    self.stack.setCurrentIndex(1)

  def go_backs(self):
    self.grab_all()
    self.stack.setCurrentIndex(2)

  def clearItem(self):
    conn = sqlite3.connect("myAnalysis.db")
    c = conn.cursor()
    c.execute(f"DELETE FROM data")
    conn.commit()
    conn.close()
    self.grab_all()

  def deleteItem(self):
    try:
      clicked = self.listWidget.currentRow()
      id = float(self.listWidget.item(clicked).text().split(" - ")[0])
      conn = sqlite3.connect("myAnalysis.db")
      c = conn.cursor()
      c.execute(f"DELETE FROM data WHERE ids = {id}")
      conn.commit()
      conn.close()
      self.grab_all()
    except AttributeError:
      pass

  def submit(self):
    title = self.title.text()
    day = self.day.currentText()
    male = self.male.text()
    female = self.female.text()
    week = self.dropdown.currentText()
    id = datetime.datetime.now().timestamp()
    # format_str = f"{id} - {week} - {day}"
    # self.listWidget.addItem(format_str)
    conn = sqlite3.connect("myAnalysis.db")
    c = conn.cursor()
    c.execute(f"INSERT INTO data VALUES (:ids, :title, :day, :male, :female, :week)", {"ids": id, "title": title, "day": day, "male": male, "female": female, "week": week})

    conn.commit()
    conn.close()
    self.listWidget.clear()
    self.grab_all()
    self.stack.setCurrentIndex(2)


  def statistics_2(self):
    self.listWidget.clear()
    conn = sqlite3.connect("myAnalysis.db")
    c = conn.cursor()
    c.execute("SELECT * FROM data")
    records = c.fetchall()

    conn.commit()
    conn.close()

    labels = []
    boy_mean = []
    girl_mean = []

    for record in records:
      labels.append(record[2])
      boy_mean.append(int(record[3]))
      girl_mean.append(int(record[4]))

    ylabel = "numbers of Natives"
    title = "Tef Community Innovation Hub Attendance"
    flabel = "boys"
    slabel = "girls"
    self.processer = BarProcess(labels, boy_mean, girl_mean, ylabel, title, flabel, slabel)
    self.processer.show()

  def statistics(self):
    title = self.title.text()
    day = self.day.currentText()
    male = self.male.text()
    female = self.female.text()
    week = self.dropdown.currentText()
    data = [int(male), int(female)]
    labels = ["Male", "Female"]
    heading = f"{week} - {day}"
    title = title
    process = PieProcess(data, labels, heading, title)

    process.show()

  def redirect_add(self):
    self.stack.setCurrentIndex(0)

if __name__ == "__main__":
  app = QApplication(sys.argv)
  ui = StatisticsUi()
  app.exec_()