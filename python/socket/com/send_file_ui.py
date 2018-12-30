from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import ctypes

START = 'start'
STOP = 'stop'


class MainWindow(object):

    main_window = None
    start_btn = None
    _translate = None

    def __init__(self, main_window):
        self.main_window = main_window
        self._translate = QtCore.QCoreApplication.translate

    def setup_ui(self):
        self.main_window.setObjectName("MainWindow")
        self.main_window.resize(850, 392)
        self.centralwidget = QtWidgets.QWidget(self.main_window)
        self.centralwidget.setObjectName("centralwidget")
        self.start_btn = QtWidgets.QPushButton(self.centralwidget)
        self.start_btn.setGeometry(QtCore.QRect(680, 70, 93, 28))
        self.start_btn.setObjectName("start_btn")
        self.start_btn.clicked.connect(self.start)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(50, 40, 571, 301))
        self.groupBox.setObjectName("groupBox")
        self.radioButton = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(130, 40, 115, 19))
        self.radioButton.setObjectName("radioButton")
        self.radioButton.setChecked(True)
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(260, 40, 115, 19))
        self.radioButton_2.setObjectName("radioButton_2")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(130, 80, 421, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(30, 80, 72, 15))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(30, 40, 72, 15))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(30, 130, 72, 15))
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_2.setGeometry(QtCore.QRect(130, 130, 421, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_3.setGeometry(QtCore.QRect(130, 180, 421, 21))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(30, 180, 72, 15))
        self.label_4.setObjectName("label_4")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_4.setGeometry(QtCore.QRect(130, 230, 421, 21))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(30, 230, 72, 15))
        self.label_5.setObjectName("label_5")
        self.main_window.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self.main_window)
        self.statusbar.setObjectName("statusbar")
        self.main_window.setStatusBar(self.statusbar)

        self.translate_ui()
        QtCore.QMetaObject.connectSlotsByName(self.main_window)

    def start(self):
        self.start_btn.setText(self._translate("MainWindow", STOP))
        self.start_btn.clicked.disconnect(self.start)
        self.start_btn.clicked.connect(self.stop)
        print 'start'
        print 'Category: %s' % ('DJ_Portal' if self.radioButton.isChecked() else 'Other')
        print 'Path: %s' % self.lineEdit.text()
        ctypes.windll.user32.MessageBoxA(0, 'content', 'message', 0)

    def stop(self):
        self.start_btn.setText(self._translate("MainWindow", START))
        self.start_btn.clicked.connect(self.start)
        self.start_btn.clicked.disconnect(self.stop)
        print 'stop'

    def translate_ui(self):
        _translate = self._translate
        self.main_window.setWindowTitle(_translate("MainWindow", "Auto_send_file"))
        self.start_btn.setText(_translate("MainWindow", START))
        self.groupBox.setTitle(_translate("MainWindow", "Settings"))
        self.radioButton.setText(_translate("MainWindow", "DJ_Portal"))
        self.radioButton_2.setText(_translate("MainWindow", "Other"))
        self.label.setText(_translate("MainWindow", "Path"))
        self.label_2.setText(_translate("MainWindow", "Category"))
        self.label_3.setText(_translate("MainWindow", "IP"))
        self.label_4.setText(_translate("MainWindow", "LoginUser"))
        self.label_5.setText(_translate("MainWindow", "Password"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    base = QtWidgets.QMainWindow()
    window = MainWindow(base)
    window.setup_ui()

    base.show()
    sys.exit(app.exec_())
