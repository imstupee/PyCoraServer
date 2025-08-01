# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designerAFUhxX.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QListWidget, QListWidgetItem,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStatusBar, QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(742, 632)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.listClients = QListWidget(self.centralwidget)
        self.listClients.setObjectName(u"listClients")

        self.horizontalLayout.addWidget(self.listClients)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.listUsers = QListWidget(self.centralwidget)
        self.listUsers.setObjectName(u"listUsers")

        self.verticalLayout_3.addWidget(self.listUsers)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.buttonCreateUser = QPushButton(self.centralwidget)
        self.buttonCreateUser.setObjectName(u"buttonCreateUser")

        self.horizontalLayout_2.addWidget(self.buttonCreateUser)

        self.buttonUpdateListUser = QPushButton(self.centralwidget)
        self.buttonUpdateListUser.setObjectName(u"buttonUpdateListUser")

        self.horizontalLayout_2.addWidget(self.buttonUpdateListUser)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)


        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.buttonStartServer = QPushButton(self.centralwidget)
        self.buttonStartServer.setObjectName(u"buttonStartServer")

        self.verticalLayout_2.addWidget(self.buttonStartServer)

        self.buttonStopServer = QPushButton(self.centralwidget)
        self.buttonStopServer.setObjectName(u"buttonStopServer")

        self.verticalLayout_2.addWidget(self.buttonStopServer)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.horizontalLayout.addLayout(self.verticalLayout_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.textLog = QTextEdit(self.centralwidget)
        self.textLog.setObjectName(u"textLog")

        self.verticalLayout.addWidget(self.textLog)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
            MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
            self.buttonCreateUser.setText(QCoreApplication.translate("MainWindow", u"Create user", None))
            self.buttonUpdateListUser.setText(QCoreApplication.translate("MainWindow", u"Update list", None))
            self.buttonStartServer.setText(QCoreApplication.translate("MainWindow", u"Start", None))
            self.buttonStopServer.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        # retranslateUi