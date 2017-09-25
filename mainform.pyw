##!-*-coding:utf-8-*-
import sys
import init
# import PyQt5 QtCore and QtGui modules
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import uic

(Ui_MainWindow, QMainWindow) = uic.loadUiType('mainform.ui')


class MainWindow(QMainWindow):
    """MainWindow inherits QMainWindow"""

    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.Tool)
        self.loadedpage()

    def __del__(self):
        self.ui = None

    def close(self):
        sys.exit(0)

    def loadedpage(self):
        self.rate_dollars = float(init.get_exchange_rate()[0])
        self.rate_yuan = float(init.get_exchange_rate()[2]) / 10
        self.ui.lineEdit_dollar.setValidator(QDoubleValidator(0.0, 9999999.99, 2))
        self.ui.lineEdit_yuan.setValidator(QDoubleValidator(0.0, 9999999.99, 2))
        self.ui.lineEdit_rub.setValidator(QDoubleValidator(0.0, 9999999.99, 2))

    def inputrubslot(self, text):
        dollars = str('{:.2f}'.format(float(text) / self.rate_dollars))
        yuans = str('{:.2f}'.format(float(text) / self.rate_yuan))
        self.ui.lineEdit_dollar.setText(dollars)
        self.ui.lineEdit_yuan.setText(yuans)

    def inputyuanslot(self, text):
        dollars = str('{:.2f}'.format(float(text) * self.rate_yuan / self.rate_dollars))
        rubles = str('{:.2f}'.format(float(text) * self.rate_yuan))
        self.ui.lineEdit_dollar.setText(dollars)
        self.ui.lineEdit_rub.setText(rubles)

    def inputdollarslot(self, text):
        yuans = str('{:.2f}'.format(float(text) * self.rate_dollars / self.rate_yuan))
        rubles = str('{:.2f}'.format(float(text) * self.rate_dollars))
        self.ui.lineEdit_rub.setText(rubles)
        self.ui.lineEdit_yuan.setText(yuans)

    def setTopLevelWindow(self):
        if self.windowState() != Qt.WindowMaximized:
            self.showMaximized()
            self.showNormal()

        else:
            self.showNormal()
            self.showMaximized()

        self.raise_()
        self.activateWindow()


class SystemTrayIcon(QSystemTrayIcon):
    def __init__(self):
        QSystemTrayIcon.__init__(self)
        self.setIcon(QIcon('./icon.svg'))
        menu = QMenu()
        self.setContextMenu(menu)
        self.activated.connect(self.onTrayClick)
        openAction = menu.addAction("Show")
        hideAction = menu.addAction("Hide")
        menu.addSeparator()
        exitAction = menu.addAction("Exit")
        openAction.triggered.connect(w.show)
        hideAction.triggered.connect(w.hide)
        exitAction.triggered.connect(qApp.quit)

    def onTrayClick(self, reason):
        if reason == QSystemTrayIcon.Trigger:
            w.setTopLevelWindow()


    def welcome(self):
        self.showMessage("Hello", "I should be aware of both buttons")

    def show(self):
        QSystemTrayIcon.show(self)


if __name__ == '__main__':
    # create application
    app = QApplication(sys.argv)
    app.setApplicationName('Exchange Rate')

    # create widget
    w = MainWindow()
    w.setWindowTitle('Exchange Rate')
    w.show()

    tray = SystemTrayIcon()
    tray.show()

    # execute application
    sys.exit(app.exec_())
