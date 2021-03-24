# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UIAjXnOg.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(824, 515)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(2, 43, 58);\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(43, 80, 170);\n"
"}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.pushButton_4 = QPushButton(self.frame_2)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(0, 20))
        self.pushButton_4.setBaseSize(QSize(0, 20))
        self.pushButton_4.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(43, 80, 170);\n"
"	color: rgb(250, 250, 250);\n"
"	font: 10pt \"Gadugi\";\n"
"	border:1px\n"
"}")

        self.verticalLayout_2.addWidget(self.pushButton_4)

        self.toolBox = QToolBox(self.frame_2)
        self.toolBox.setObjectName(u"toolBox")
        self.toolBox.setMinimumSize(QSize(0, 20))
        font = QFont()
        font.setFamily(u"Gadugi")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.toolBox.setFont(font)
        self.toolBox.setCursor(QCursor(Qt.PointingHandCursor))
        self.toolBox.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(43, 80, 10,0);\n"
"	border: 0px;\n"
"	color: rgb(255, 255, 255);\n"
"	border-type: outset;\n"
"	font: 10pt \"Gadugi\";\n"
"	\n"
"}\n"
"QToolBox:tab{\n"
"background-color: rgb(43, 80, 170);\n"
"	border: 0px;\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.system_events = QWidget()
        self.system_events.setObjectName(u"system_events")
        self.system_events.setGeometry(QRect(0, 0, 162, 111))
        self.verticalLayout_3 = QVBoxLayout(self.system_events)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.pushButton = QPushButton(self.system_events)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 20))

        self.verticalLayout_3.addWidget(self.pushButton)

        self.pushButton_3 = QPushButton(self.system_events)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(0, 20))

        self.verticalLayout_3.addWidget(self.pushButton_3)

        self.pushButton_2 = QPushButton(self.system_events)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(0, 20))

        self.verticalLayout_3.addWidget(self.pushButton_2)

        self.toolBox.addItem(self.system_events, u"System Events")
        self.security_events = QWidget()
        self.security_events.setObjectName(u"security_events")
        self.verticalLayout_4 = QVBoxLayout(self.security_events)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.pushButton_5 = QPushButton(self.security_events)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMinimumSize(QSize(0, 20))

        self.verticalLayout_4.addWidget(self.pushButton_5)

        self.pushButton_7 = QPushButton(self.security_events)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setMinimumSize(QSize(0, 20))

        self.verticalLayout_4.addWidget(self.pushButton_7)

        self.pushButton_6 = QPushButton(self.security_events)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMinimumSize(QSize(0, 20))

        self.verticalLayout_4.addWidget(self.pushButton_6)

        self.toolBox.addItem(self.security_events, u"Security Events")

        self.verticalLayout_2.addWidget(self.toolBox)

        self.pushButton_8 = QPushButton(self.frame_2)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setMinimumSize(QSize(0, 20))
        self.pushButton_8.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(43, 80, 170);\n"
"	color: rgb(250, 250, 250);\n"
"	font: 10pt \"Gadugi\";\n"
"	border:1px\n"
"}")

        self.verticalLayout_2.addWidget(self.pushButton_8)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.verticalLayout_2.setStretch(0, 3)
        self.verticalLayout_2.setStretch(1, 3)
        self.verticalLayout_2.setStretch(2, 5)
        self.verticalLayout_2.setStretch(3, 3)
        self.verticalLayout_2.setStretch(4, 6)

        self.horizontalLayout.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.frame_3)

        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 8)

        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.toolBox.setCurrentIndex(0)
        self.toolBox.layout().setSpacing(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Dasboard", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Errors", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Warnings", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Information", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.system_events), QCoreApplication.translate("MainWindow", u"System Events", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Login Events", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Acess Denial", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Others", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.security_events), QCoreApplication.translate("MainWindow", u"Security Events", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"Application Events", None))
    # retranslateUi

