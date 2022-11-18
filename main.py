# -*- coding: utf-8 -*-

import sys
import time

from random import choice

from PyQt5 import QtCore, QtWidgets
from PyQt5.Qt import *

from animatedbutton import AnimatedButton
from lesson_widget import LessonWidget

if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

practice_texts = [f'Practice/text_{i}.txt' for i in range(1, 72)]
practice_texts_eng = [f'Practice_eng/text_{i}.txt' for i in range(1, 55)]
my_styles = ['background-color: rgb(255, 163, 144);', 'background-color: rgb(255, 206, 108);',
             'background-color: rgb(181, 189, 255);', 'background-color: rgb(184, 230, 222);',
             'background-color: rgb(255, 99, 101);', 'background-color: rgb(169, 70, 255);',
             'background-color: rgb(255, 122, 60);', 'background-color: rgb(75, 93, 255);',
             'background-color: rgb(170, 170, 127);', 'background-color: rgb(230, 70, 60);',
             'background-color: rgb(85, 170, 127);', 'background-color: rgb(85, 85, 127);']


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1451, 889)
        MainWindow.setStyleSheet(u"background-color: rgb(77, 77, 77);\n"
                                 "border-radius: 20px;")
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        self.styleSheet.setStyleSheet(u"*{\n"
                                      "	border: none;\n"
                                      "	border-color: transparent;\n"
                                      "	color: #fff;\n"
                                      "}\n"
                                      "#centralwidget{\n"
                                      "	background-color: #040f13;\n"
                                      "}\n"
                                      "side_menu{\n"
                                      "	background-color: #071e26;\n"
                                      "	border-radius: 20 px;\n"
                                      "}\n"
                                      "QPushButton{\n"
                                      "\n"
                                      "	padding: 10 px;\n"
                                      "	background-color: #040f13;\n"
                                      "	border-radius: 5px;\n"
                                      "\n"
                                      "}\n"
                                      "main_body{\n"
                                      "	background-color: #071e26;\n"
                                      "	border-radius: 10px;\n"
                                      "}\n"
                                      "\n"
                                      "/* SCROLL BAR */\n"
                                      "QScrollBar:vertical {\n"
                                      "	border: none;\n"
                                      "    background: rgb(52, 59, 72);\n"
                                      "    width: 6px;\n"
                                      "    margin: 21px 0 21px 0;\n"
                                      "	border-radius: 0px;\n"
                                      " }\n"
                                      " QScrollBar::handle:vertical {	\n"
                                      "	background: rgb(150, 147, 249);\n"
                                      "    min-height: 25px;\n"
                                      "	border-radius: 2px\n"
                                      " }\n"
                                      " QScrollBar::add-line:vertical {\n"
                                      "    border: none;\n"
                                      "    background: rgb(55, 63, 77);\n"
                                      "    height: 20px;\n"
                                      "	border-bottom-left-radius: 4px;\n"
                                      "    border-bottom-right-radius: 4px;\n"
                                      "    subcontrol-position: bottom;\n"
                                      "    subcontrol-origin: margin;\n"
                                      " }\n"
                                      " QScrollBar::sub-li"
                                      "ne:vertical {\n"
                                      "	border: none;\n"
                                      "    background: rgb(55, 63, 77);\n"
                                      "    height: 20px;\n"
                                      "	border-top-left-radius: 4px;\n"
                                      "    border-top-right-radius: 4px;\n"
                                      "    subcontrol-position: top;\n"
                                      "    subcontrol-origin: margin;\n"
                                      " }\n"
                                      " QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
                                      "     background: none;\n"
                                      " }\n"
                                      "\n"
                                      " QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
                                      "     background: none;\n"
                                      " }\n"
                                      "\n"
                                      "\n"
                                      "QPlainTextEdit{\n"
                                      "	color: rgb(232, 232, 232);\n"
                                      "	selection-background-color: rgb(53, 51, 42);\n"
                                      "}\n"
                                      "\n"
                                      "#plainTextEdit_2{\n"
                                      "	background-color: rgb(85, 85, 127);\n"
                                      "}\n"
                                      "\n"
                                      "/*CHECKBOX*/\n"
                                      "QCheckBox::indicator {\n"
                                      "    border: 3px solid rgb(52, 59, 72);\n"
                                      "	width: 15px;\n"
                                      "	height: 15px;\n"
                                      "	border-radius: 10px;\n"
                                      "    background: rgb(44, 49, 60);\n"
                                      "}\n"
                                      "QCheckBox::indicator:hover {\n"
                                      "    border: 3px solid rgb(58, 66, 81);\n"
                                      "}\n"
                                      "QCheckBox::indicator:checked {\n"
                                      "    background: 3px solid #FFB30D;\n"
                                      "	border: 3px solid rgb(5"
                                      "2, 59, 72);	\n"
                                      "}")
        self.verticalLayout = QVBoxLayout(self.styleSheet)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.plainTextEdit = QPlainTextEdit(self.styleSheet)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setMinimumSize(QSize(0, 160))
        font = QFont()
        font.setFamily(u"Roboto Medium")
        font.setPointSize(17)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.plainTextEdit)

        self.plainTextEdit_2 = QPlainTextEdit(self.styleSheet)
        self.plainTextEdit_2.setObjectName(u"plainTextEdit_2")
        self.plainTextEdit_2.setMinimumSize(QSize(0, 160))
        self.plainTextEdit_2.setFont(font)
        self.plainTextEdit_2.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.plainTextEdit_2)

        self.typewriter = QLabel(self.styleSheet)
        self.typewriter.setObjectName(u"typewriter")
        self.typewriter.setMinimumSize(QSize(0, 30))
        font1 = QFont()
        font1.setPointSize(13)
        font1.setBold(True)
        font1.setWeight(75)
        self.typewriter.setFont(font1)
        self.typewriter.setStyleSheet(u"color: rgb(255, 200, 133);\n"
                                      "background-color: rgb(255, 245, 219);\n"
                                      "border-radius: 10px;\n"
                                      "")
        self.typewriter.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.typewriter)

        self.frame_2 = QFrame(self.styleSheet)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setStyleSheet(u"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.side_menu = QFrame(self.frame_2)
        self.side_menu.setObjectName(u"side_menu")
        self.side_menu.setMinimumSize(QSize(160, 0))
        self.side_menu.setStyleSheet(u"QPushButton{\n"
                                     "	background-color: rgb(37, 41, 48);\n"
                                     "	font: 16px Segoe UI;\n"
                                     "}\n"
                                     "\n"
                                     "QPushButton:hover {\n"
                                     "	background-color: rgb(85, 108, 113);\n"
                                     "}\n"
                                     "\n"
                                     "QPushButton:pressed {	\n"
                                     "	background-color: rgb(66, 66, 66);\n"
                                     "	color: rgb(255, 255, 255);\n"
                                     "}")
        self.verticalLayout_2 = QVBoxLayout(self.side_menu)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.side_menu)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy1)
        self.frame_5.setMinimumSize(QSize(0, 0))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_5)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.btn_Practice = QPushButton(self.frame_5)
        self.btn_Practice.setObjectName(u"btn_Practice")
        self.btn_Practice.setEnabled(True)
        self.btn_Practice.setMinimumSize(QSize(0, 50))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setBold(False)
        font2.setItalic(False)
        font2.setWeight(50)
        self.btn_Practice.setFont(font2)
        self.btn_Practice.setCursor(QCursor(Qt.OpenHandCursor))
        self.btn_Practice.setMouseTracking(False)
        self.btn_Practice.setFocusPolicy(Qt.StrongFocus)
        self.btn_Practice.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/icons/icons/chrome.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_Practice.setIcon(icon)
        self.btn_Practice.setCheckable(False)

        self.verticalLayout_3.addWidget(self.btn_Practice)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.btn_Lesson1 = QPushButton(self.frame_5)
        self.btn_Lesson1.setObjectName(u"btn_Lesson1")
        self.btn_Lesson1.setEnabled(True)
        self.btn_Lesson1.setMinimumSize(QSize(0, 37))
        self.btn_Lesson1.setFont(font2)
        self.btn_Lesson1.setCursor(QCursor(Qt.OpenHandCursor))
        self.btn_Lesson1.setMouseTracking(False)
        self.btn_Lesson1.setFocusPolicy(Qt.StrongFocus)
        self.btn_Lesson1.setStyleSheet(u"")
        self.btn_Lesson1.setIcon(icon)
        self.btn_Lesson1.setCheckable(False)

        self.verticalLayout_3.addWidget(self.btn_Lesson1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.btn_Lesson2 = QPushButton(self.frame_5)
        self.btn_Lesson2.setObjectName(u"btn_Lesson2")
        self.btn_Lesson2.setEnabled(True)
        self.btn_Lesson2.setMinimumSize(QSize(0, 37))
        self.btn_Lesson2.setFont(font2)
        self.btn_Lesson2.setCursor(QCursor(Qt.OpenHandCursor))
        self.btn_Lesson2.setMouseTracking(False)
        self.btn_Lesson2.setFocusPolicy(Qt.StrongFocus)
        self.btn_Lesson2.setStyleSheet(u"")
        self.btn_Lesson2.setIcon(icon)
        self.btn_Lesson2.setCheckable(False)

        self.verticalLayout_3.addWidget(self.btn_Lesson2)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_3)

        self.btn_Lesson3 = QPushButton(self.frame_5)
        self.btn_Lesson3.setObjectName(u"btn_Lesson3")
        self.btn_Lesson3.setEnabled(True)
        self.btn_Lesson3.setMinimumSize(QSize(0, 37))
        self.btn_Lesson3.setFont(font2)
        self.btn_Lesson3.setCursor(QCursor(Qt.OpenHandCursor))
        self.btn_Lesson3.setMouseTracking(False)
        self.btn_Lesson3.setFocusPolicy(Qt.StrongFocus)
        self.btn_Lesson3.setStyleSheet(u"")
        self.btn_Lesson3.setIcon(icon)
        self.btn_Lesson3.setCheckable(False)

        self.verticalLayout_3.addWidget(self.btn_Lesson3)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_4)

        self.btn_Lesson4 = QPushButton(self.frame_5)
        self.btn_Lesson4.setObjectName(u"btn_Lesson4")
        self.btn_Lesson4.setEnabled(True)
        self.btn_Lesson4.setMinimumSize(QSize(0, 37))
        self.btn_Lesson4.setFont(font2)
        self.btn_Lesson4.setCursor(QCursor(Qt.OpenHandCursor))
        self.btn_Lesson4.setMouseTracking(False)
        self.btn_Lesson4.setFocusPolicy(Qt.StrongFocus)
        self.btn_Lesson4.setStyleSheet(u"")
        self.btn_Lesson4.setIcon(icon)
        self.btn_Lesson4.setCheckable(False)

        self.verticalLayout_3.addWidget(self.btn_Lesson4)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_5)

        self.btn_Lesson5 = QPushButton(self.frame_5)
        self.btn_Lesson5.setObjectName(u"btn_Lesson5")
        self.btn_Lesson5.setEnabled(True)
        self.btn_Lesson5.setMinimumSize(QSize(0, 37))
        self.btn_Lesson5.setFont(font2)
        self.btn_Lesson5.setCursor(QCursor(Qt.OpenHandCursor))
        self.btn_Lesson5.setMouseTracking(False)
        self.btn_Lesson5.setFocusPolicy(Qt.StrongFocus)
        self.btn_Lesson5.setStyleSheet(u"")
        self.btn_Lesson5.setIcon(icon)
        self.btn_Lesson5.setCheckable(False)

        self.verticalLayout_3.addWidget(self.btn_Lesson5)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_6)

        self.btn_Lesson6 = QPushButton(self.frame_5)
        self.btn_Lesson6.setObjectName(u"btn_Lesson6")
        self.btn_Lesson6.setEnabled(True)
        self.btn_Lesson6.setMinimumSize(QSize(0, 37))
        self.btn_Lesson6.setFont(font2)
        self.btn_Lesson6.setCursor(QCursor(Qt.OpenHandCursor))
        self.btn_Lesson6.setMouseTracking(False)
        self.btn_Lesson6.setFocusPolicy(Qt.StrongFocus)
        self.btn_Lesson6.setStyleSheet(u"")
        self.btn_Lesson6.setIcon(icon)
        self.btn_Lesson6.setCheckable(False)

        self.verticalLayout_3.addWidget(self.btn_Lesson6)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_7)

        self.btn_Lesson7 = QPushButton(self.frame_5)
        self.btn_Lesson7.setObjectName(u"btn_Lesson7")
        self.btn_Lesson7.setEnabled(True)
        self.btn_Lesson7.setMinimumSize(QSize(0, 37))
        self.btn_Lesson7.setFont(font2)
        self.btn_Lesson7.setCursor(QCursor(Qt.OpenHandCursor))
        self.btn_Lesson7.setMouseTracking(False)
        self.btn_Lesson7.setFocusPolicy(Qt.StrongFocus)
        self.btn_Lesson7.setStyleSheet(u"")
        self.btn_Lesson7.setIcon(icon)
        self.btn_Lesson7.setCheckable(False)

        self.verticalLayout_3.addWidget(self.btn_Lesson7)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_8)

        self.btn_Lesson8 = QPushButton(self.frame_5)
        self.btn_Lesson8.setObjectName(u"btn_Lesson8")
        self.btn_Lesson8.setEnabled(True)
        self.btn_Lesson8.setMinimumSize(QSize(0, 37))
        self.btn_Lesson8.setFont(font2)
        self.btn_Lesson8.setCursor(QCursor(Qt.OpenHandCursor))
        self.btn_Lesson8.setMouseTracking(False)
        self.btn_Lesson8.setFocusPolicy(Qt.StrongFocus)
        self.btn_Lesson8.setStyleSheet(u"")
        self.btn_Lesson8.setIcon(icon)
        self.btn_Lesson8.setCheckable(False)

        self.verticalLayout_3.addWidget(self.btn_Lesson8)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_9)

        self.btn_Lesson9 = QPushButton(self.frame_5)
        self.btn_Lesson9.setObjectName(u"btn_Lesson9")
        self.btn_Lesson9.setEnabled(True)
        self.btn_Lesson9.setMinimumSize(QSize(0, 37))
        self.btn_Lesson9.setFont(font2)
        self.btn_Lesson9.setCursor(QCursor(Qt.OpenHandCursor))
        self.btn_Lesson9.setMouseTracking(False)
        self.btn_Lesson9.setFocusPolicy(Qt.StrongFocus)
        self.btn_Lesson9.setStyleSheet(u"")
        self.btn_Lesson9.setIcon(icon)
        self.btn_Lesson9.setCheckable(False)

        self.verticalLayout_3.addWidget(self.btn_Lesson9)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_10)

        self.btn_Lesson10 = QPushButton(self.frame_5)
        self.btn_Lesson10.setObjectName(u"btn_Lesson10")
        self.btn_Lesson10.setEnabled(True)
        self.btn_Lesson10.setMinimumSize(QSize(0, 37))
        self.btn_Lesson10.setFont(font2)
        self.btn_Lesson10.setCursor(QCursor(Qt.OpenHandCursor))
        self.btn_Lesson10.setMouseTracking(False)
        self.btn_Lesson10.setFocusPolicy(Qt.StrongFocus)
        self.btn_Lesson10.setStyleSheet(u"")
        self.btn_Lesson10.setIcon(icon)
        self.btn_Lesson10.setCheckable(False)

        self.verticalLayout_3.addWidget(self.btn_Lesson10)

        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_11)

        self.verticalSpacer_15 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_15)

        self.verticalSpacer_14 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_14)

        self.verticalLayout_2.addWidget(self.frame_5)

        self.horizontalLayout.addWidget(self.side_menu)

        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy2)
        self.frame_4.setMinimumSize(QSize(1273, 467))
        font3 = QFont()
        font3.setPointSize(8)
        self.frame_4.setFont(font3)
        self.frame_4.setStyleSheet(u"")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.groupBox = QGroupBox(self.frame_4)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(0, 0))
        self.groupBox.setMaximumSize(QSize(1200, 500))
        font4 = QFont()
        font4.setFamily(u"Segoe Script")
        font4.setPointSize(16)
        self.groupBox.setFont(font4)
        self.groupBox.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.groupBox.setStyleSheet(u"background-color: rgb(1, 10, 45);\n"
                                    "border-radius: 10px;\n"
                                    "")
        self.btn_sth = AnimatedButton(self.groupBox)
        self.btn_sth.setObjectName(u"btn_sth")
        self.btn_sth.setGeometry(QRect(110, 40, 61, 51))
        font5 = QFont()
        font5.setFamily(u"Bahnschrift SemiBold")
        font5.setPointSize(14)
        font5.setBold(True)
        font5.setWeight(75)
        self.btn_sth.setFont(font5)
        self.btn_sth.setStyleSheet(u"background-color: rgb(255, 206, 108);")
        self.btn_num_1 = AnimatedButton(self.groupBox)
        self.btn_num_1.setObjectName(u"btn_num_1")
        self.btn_num_1.setGeometry(QRect(180, 40, 61, 51))
        self.btn_num_1.setFont(font5)
        self.btn_num_1.setStyleSheet(u"background-color: rgb(255, 206, 108);")
        self.btn_num_2 = AnimatedButton(self.groupBox)
        self.btn_num_2.setObjectName(u"btn_num_2")
        self.btn_num_2.setGeometry(QRect(250, 40, 61, 51))
        self.btn_num_2.setFont(font5)
        self.btn_num_2.setStyleSheet(u"background-color: rgb(255, 206, 108);")
        self.btn_num_3 = AnimatedButton(self.groupBox)
        self.btn_num_3.setObjectName(u"btn_num_3")
        self.btn_num_3.setGeometry(QRect(320, 40, 61, 51))
        self.btn_num_3.setFont(font5)
        self.btn_num_3.setStyleSheet(u"background-color: rgb(255, 206, 108);")
        self.btn_num_4 = AnimatedButton(self.groupBox)
        self.btn_num_4.setObjectName(u"btn_num_4")
        self.btn_num_4.setGeometry(QRect(390, 40, 61, 51))
        self.btn_num_4.setFont(font5)
        self.btn_num_4.setStyleSheet(u"background-color: rgb(255, 206, 108);")
        self.btn_num_5 = AnimatedButton(self.groupBox)
        self.btn_num_5.setObjectName(u"btn_num_5")
        self.btn_num_5.setGeometry(QRect(460, 40, 61, 51))
        self.btn_num_5.setFont(font5)
        self.btn_num_5.setStyleSheet(u"background-color: rgb(255, 206, 108);")
        self.btn_num_6 = AnimatedButton(self.groupBox)
        self.btn_num_6.setObjectName(u"btn_num_6")
        self.btn_num_6.setGeometry(QRect(530, 40, 61, 51))
        self.btn_num_6.setFont(font5)
        self.btn_num_6.setStyleSheet(u"background-color: rgb(255, 206, 108);")
        self.btn_num_7 = AnimatedButton(self.groupBox)
        self.btn_num_7.setObjectName(u"btn_num_7")
        self.btn_num_7.setGeometry(QRect(600, 40, 61, 51))
        self.btn_num_7.setFont(font5)
        self.btn_num_7.setStyleSheet(u"background-color: rgb(255, 206, 108);")
        self.btn_num_8 = AnimatedButton(self.groupBox)
        self.btn_num_8.setObjectName(u"btn_num_8")
        self.btn_num_8.setGeometry(QRect(670, 40, 61, 51))
        self.btn_num_8.setFont(font5)
        self.btn_num_8.setStyleSheet(u"background-color: rgb(255, 206, 108);")
        self.btn_num_9 = AnimatedButton(self.groupBox)
        self.btn_num_9.setObjectName(u"btn_num_9")
        self.btn_num_9.setGeometry(QRect(740, 40, 61, 51))
        self.btn_num_9.setFont(font5)
        self.btn_num_9.setStyleSheet(u"background-color: rgb(255, 206, 108);")
        self.btn_num_0 = AnimatedButton(self.groupBox)
        self.btn_num_0.setObjectName(u"btn_num_0")
        self.btn_num_0.setGeometry(QRect(810, 40, 61, 51))
        self.btn_num_0.setFont(font5)
        self.btn_num_0.setStyleSheet(u"background-color: rgb(255, 206, 108);")
        self.btn_backspace = AnimatedButton(self.groupBox)
        self.btn_backspace.setObjectName(u"btn_backspace")
        self.btn_backspace.setGeometry(QRect(1020, 40, 91, 51))
        font6 = QFont()
        font6.setFamily(u"Bahnschrift SemiBold")
        font6.setPointSize(12)
        font6.setBold(True)
        font6.setWeight(75)
        self.btn_backspace.setFont(font6)
        self.btn_backspace.setStyleSheet(u"background-color: rgb(255, 206, 108);")
        self.btn_tab = AnimatedButton(self.groupBox)
        self.btn_tab.setObjectName(u"btn_tab")
        self.btn_tab.setGeometry(QRect(110, 100, 91, 51))
        self.btn_tab.setFont(font5)
        self.btn_tab.setStyleSheet(u"background-color: rgb(255, 206, 108);")
        self.btn_str_1 = AnimatedButton(self.groupBox)
        self.btn_str_1.setObjectName(u"btn_str_1")
        self.btn_str_1.setGeometry(QRect(210, 100, 61, 51))
        self.btn_str_1.setFont(font5)
        self.btn_str_1.setStyleSheet(u"background-color: rgb(255, 206, 108);")
        self.btn_str_2 = AnimatedButton(self.groupBox)
        self.btn_str_2.setObjectName(u"btn_str_2")
        self.btn_str_2.setGeometry(QRect(280, 100, 61, 51))
        self.btn_str_2.setFont(font5)
        self.btn_str_2.setStyleSheet(u"background-color: rgb(255, 206, 108);")
        self.btn_str_3 = AnimatedButton(self.groupBox)
        self.btn_str_3.setObjectName(u"btn_str_3")
        self.btn_str_3.setGeometry(QRect(350, 100, 61, 51))
        self.btn_str_3.setFont(font5)
        self.btn_str_3.setStyleSheet(u"background-color: rgb(255, 206, 108);")
        self.btn_str_4 = AnimatedButton(self.groupBox)
        self.btn_str_4.setObjectName(u"btn_str_4")
        self.btn_str_4.setGeometry(QRect(420, 100, 61, 51))
        self.btn_str_4.setFont(font5)
        self.btn_str_4.setStyleSheet(u"background-color: rgb(255, 206, 108);")
        self.btn_str_5 = AnimatedButton(self.groupBox)
        self.btn_str_5.setObjectName(u"btn_str_5")
        self.btn_str_5.setGeometry(QRect(490, 100, 61, 51))
        self.btn_str_5.setFont(font5)
        self.btn_str_5.setStyleSheet(u"background-color: rgb(255, 206, 108);")
        self.btn_str_6 = AnimatedButton(self.groupBox)
        self.btn_str_6.setObjectName(u"btn_str_6")
        self.btn_str_6.setGeometry(QRect(560, 100, 61, 51))
        self.btn_str_6.setFont(font5)
        self.btn_str_6.setStyleSheet(u"background-color: rgb(255, 206, 108);")
        self.btn_str_7 = AnimatedButton(self.groupBox)
        self.btn_str_7.setObjectName(u"btn_str_7")
        self.btn_str_7.setGeometry(QRect(630, 100, 61, 51))
        self.btn_str_7.setFont(font5)
        self.btn_str_7.setStyleSheet(u"background-color: rgb(255, 206, 108);")
        self.btn_str_8 = AnimatedButton(self.groupBox)
        self.btn_str_8.setObjectName(u"btn_str_8")
        self.btn_str_8.setGeometry(QRect(700, 100, 61, 51))
        self.btn_str_8.setFont(font5)
        self.btn_str_8.setStyleSheet(u"background-color: rgb(255, 206, 108);")
        self.btn_str_9 = AnimatedButton(self.groupBox)
        self.btn_str_9.setObjectName(u"btn_str_9")
        self.btn_str_9.setGeometry(QRect(770, 100, 61, 51))
        self.btn_str_9.setFont(font5)
        self.btn_str_9.setStyleSheet(u"background-color: rgb(255, 206, 108);")
        self.btn_str_10 = AnimatedButton(self.groupBox)
        self.btn_str_10.setObjectName(u"btn_str_10")
        self.btn_str_10.setGeometry(QRect(840, 100, 61, 51))
        self.btn_str_10.setFont(font5)
        self.btn_str_10.setStyleSheet(u"background-color: rgb(255, 206, 108);")
        self.btn_str_11 = AnimatedButton(self.groupBox)
        self.btn_str_11.setObjectName(u"btn_str_11")
        self.btn_str_11.setGeometry(QRect(910, 100, 61, 51))
        self.btn_str_11.setFont(font5)
        self.btn_str_11.setStyleSheet(u"background-color: rgb(255, 206, 108);")
        self.btn_minus = AnimatedButton(self.groupBox)
        self.btn_minus.setObjectName(u"btn_minus")
        self.btn_minus.setGeometry(QRect(880, 40, 61, 51))
        self.btn_minus.setFont(font5)
        self.btn_minus.setStyleSheet(u"background-color: rgb(255, 206, 108);")
        self.btn_ravno = AnimatedButton(self.groupBox)
        self.btn_ravno.setObjectName(u"btn_ravno")
        self.btn_ravno.setGeometry(QRect(950, 40, 61, 51))
        self.btn_ravno.setFont(font5)
        self.btn_ravno.setStyleSheet(u"background-color: rgb(255, 206, 108);")
        self.btn_str_12 = AnimatedButton(self.groupBox)
        self.btn_str_12.setObjectName(u"btn_str_12")
        self.btn_str_12.setGeometry(QRect(980, 100, 61, 51))
        self.btn_str_12.setFont(font5)
        self.btn_str_12.setStyleSheet(u"background-color: rgb(255, 206, 108);")
        self.btn_str_13 = AnimatedButton(self.groupBox)
        self.btn_str_13.setObjectName(u"btn_str_13")
        self.btn_str_13.setGeometry(QRect(1050, 100, 61, 51))
        self.btn_str_13.setFont(font5)
        self.btn_str_13.setStyleSheet(u"background-color: rgb(255, 206, 108);")
        self.btn_caps = AnimatedButton(self.groupBox)
        self.btn_caps.setObjectName(u"btn_caps")
        self.btn_caps.setGeometry(QRect(110, 160, 111, 51))
        self.btn_caps.setFont(font5)
        self.btn_caps.setStyleSheet(u"background-color: rgb(255, 206, 108);")
        self.btn_str2_1 = AnimatedButton(self.groupBox)
        self.btn_str2_1.setObjectName(u"btn_str2_1")
        self.btn_str2_1.setGeometry(QRect(230, 160, 61, 51))
        self.btn_str2_1.setFont(font5)
        self.btn_str2_1.setStyleSheet(u"background-color: rgb(255, 206, 108);")
        self.btn_str2_2 = AnimatedButton(self.groupBox)
        self.btn_str2_2.setObjectName(u"btn_str2_2")
        self.btn_str2_2.setGeometry(QRect(300, 160, 61, 51))
        self.btn_str2_2.setFont(font5)
        self.btn_str2_2.setStyleSheet(u"background-color: rgb(255, 206, 108);")
        self.btn_str2_3 = AnimatedButton(self.groupBox)
        self.btn_str2_3.setObjectName(u"btn_str2_3")
        self.btn_str2_3.setGeometry(QRect(370, 160, 61, 51))
        self.btn_str2_3.setFont(font5)
        self.btn_str2_3.setStyleSheet(u"background-color: rgb(255, 206, 108);")
        self.btn_str2_4 = AnimatedButton(self.groupBox)
        self.btn_str2_4.setObjectName(u"btn_str2_4")
        self.btn_str2_4.setGeometry(QRect(440, 160, 61, 51))
        self.btn_str2_4.setFont(font5)
        self.btn_str2_4.setStyleSheet(u"background-color: rgb(255, 206, 108);")
        self.btn_str2_5 = AnimatedButton(self.groupBox)
        self.btn_str2_5.setObjectName(u"btn_str2_5")
        self.btn_str2_5.setGeometry(QRect(510, 160, 61, 51))
        self.btn_str2_5.setFont(font5)
        self.btn_str2_5.setStyleSheet(u"background-color: rgb(255, 206, 108);")
        self.btn_str2_6 = AnimatedButton(self.groupBox)
        self.btn_str2_6.setObjectName(u"btn_str2_6")
        self.btn_str2_6.setGeometry(QRect(580, 160, 61, 51))
        self.btn_str2_6.setFont(font5)
        self.btn_str2_6.setStyleSheet(u"background-color: rgb(255, 206, 108);")
        self.btn_str2_7 = AnimatedButton(self.groupBox)
        self.btn_str2_7.setObjectName(u"btn_str2_7")
        self.btn_str2_7.setGeometry(QRect(650, 160, 61, 51))
        self.btn_str2_7.setFont(font5)
        self.btn_str2_7.setStyleSheet(u"background-color: rgb(255, 206, 108);")
        self.btn_str2_8 = AnimatedButton(self.groupBox)
        self.btn_str2_8.setObjectName(u"btn_str2_8")
        self.btn_str2_8.setGeometry(QRect(720, 160, 61, 51))
        self.btn_str2_8.setFont(font5)
        self.btn_str2_8.setStyleSheet(u"background-color: rgb(255, 206, 108);")
        self.btn_str2_9 = AnimatedButton(self.groupBox)
        self.btn_str2_9.setObjectName(u"btn_str2_9")
        self.btn_str2_9.setGeometry(QRect(790, 160, 61, 51))
        self.btn_str2_9.setFont(font5)
        self.btn_str2_9.setStyleSheet(u"background-color: rgb(255, 206, 108);")
        self.btn_str2_10 = AnimatedButton(self.groupBox)
        self.btn_str2_10.setObjectName(u"btn_str2_10")
        self.btn_str2_10.setGeometry(QRect(860, 160, 61, 51))
        self.btn_str2_10.setFont(font5)
        self.btn_str2_10.setStyleSheet(u"background-color: rgb(255, 206, 108);")
        self.btn_str2_11 = AnimatedButton(self.groupBox)
        self.btn_str2_11.setObjectName(u"btn_str2_11")
        self.btn_str2_11.setGeometry(QRect(930, 160, 61, 51))
        self.btn_str2_11.setFont(font5)
        self.btn_str2_11.setStyleSheet(u"background-color: rgb(255, 206, 108);")
        self.btn_enter = AnimatedButton(self.groupBox)
        self.btn_enter.setObjectName(u"btn_enter")
        self.btn_enter.setGeometry(QRect(1000, 159, 111, 51))
        self.btn_enter.setFont(font5)
        self.btn_enter.setStyleSheet(u"background-color: rgb(255, 206, 108);")
        self.btn_Lshift = AnimatedButton(self.groupBox)
        self.btn_Lshift.setObjectName(u"btn_Lshift")
        self.btn_Lshift.setGeometry(QRect(110, 220, 151, 51))
        self.btn_Lshift.setFont(font5)
        self.btn_Lshift.setStyleSheet(u"background-color: rgb(255, 206, 108);")
        self.btn_str3_1 = AnimatedButton(self.groupBox)
        self.btn_str3_1.setObjectName(u"btn_str3_1")
        self.btn_str3_1.setGeometry(QRect(270, 220, 61, 51))
        self.btn_str3_1.setFont(font5)
        self.btn_str3_1.setStyleSheet(u"background-color: rgb(255, 206, 108);\n"
                                      "alternate-background-color: rgb(183, 248, 255);")
        self.btn_str3_2 = AnimatedButton(self.groupBox)
        self.btn_str3_2.setObjectName(u"btn_str3_2")
        self.btn_str3_2.setGeometry(QRect(340, 220, 61, 51))
        self.btn_str3_2.setFont(font5)
        self.btn_str3_2.setStyleSheet(u"background-color: rgb(255, 206, 108);")
        self.btn_str3_3 = AnimatedButton(self.groupBox)
        self.btn_str3_3.setObjectName(u"btn_str3_3")
        self.btn_str3_3.setGeometry(QRect(410, 220, 61, 51))
        self.btn_str3_3.setFont(font5)
        self.btn_str3_3.setStyleSheet(u"background-color: rgb(255, 206, 108);")
        self.btn_str3_4 = AnimatedButton(self.groupBox)
        self.btn_str3_4.setObjectName(u"btn_str3_4")
        self.btn_str3_4.setGeometry(QRect(480, 220, 61, 51))
        self.btn_str3_4.setFont(font5)
        self.btn_str3_4.setStyleSheet(u"background-color: rgb(255, 206, 108);")
        self.btn_str3_5 = AnimatedButton(self.groupBox)
        self.btn_str3_5.setObjectName(u"btn_str3_5")
        self.btn_str3_5.setGeometry(QRect(550, 220, 61, 51))
        self.btn_str3_5.setFont(font5)
        self.btn_str3_5.setStyleSheet(u"background-color: rgb(255, 206, 108);")
        self.btn_str3_6 = AnimatedButton(self.groupBox)
        self.btn_str3_6.setObjectName(u"btn_str3_6")
        self.btn_str3_6.setGeometry(QRect(620, 220, 61, 51))
        self.btn_str3_6.setFont(font5)
        self.btn_str3_6.setStyleSheet(u"background-color: rgb(255, 206, 108);")
        self.btn_str3_7 = AnimatedButton(self.groupBox)
        self.btn_str3_7.setObjectName(u"btn_str3_7")
        self.btn_str3_7.setGeometry(QRect(690, 220, 61, 51))
        self.btn_str3_7.setFont(font5)
        self.btn_str3_7.setStyleSheet(u"background-color: rgb(255, 206, 108);")
        self.btn_str3_8 = AnimatedButton(self.groupBox)
        self.btn_str3_8.setObjectName(u"btn_str3_8")
        self.btn_str3_8.setGeometry(QRect(760, 220, 61, 51))
        self.btn_str3_8.setFont(font5)
        self.btn_str3_8.setStyleSheet(u"background-color: rgb(255, 206, 108);")
        self.btn_str3_9 = AnimatedButton(self.groupBox)
        self.btn_str3_9.setObjectName(u"btn_str3_9")
        self.btn_str3_9.setGeometry(QRect(830, 220, 61, 51))
        self.btn_str3_9.setFont(font5)
        self.btn_str3_9.setStyleSheet(u"background-color: rgb(255, 206, 108);")
        self.btn_str3_10 = AnimatedButton(self.groupBox)
        self.btn_str3_10.setObjectName(u"btn_str3_10")
        self.btn_str3_10.setGeometry(QRect(900, 220, 61, 51))
        font7 = QFont()
        font7.setFamily(u"Bahnschrift SemiBold")
        font7.setPointSize(16)
        font7.setBold(True)
        font7.setWeight(75)
        self.btn_str3_10.setFont(font7)
        self.btn_str3_10.setStyleSheet(u"background-color: rgb(255, 206, 108);")
        self.btn_Rshift = AnimatedButton(self.groupBox)
        self.btn_Rshift.setObjectName(u"btn_Rshift")
        self.btn_Rshift.setGeometry(QRect(970, 220, 141, 51))
        self.btn_Rshift.setFont(font5)
        self.btn_Rshift.setStyleSheet(u"background-color: rgb(255, 206, 108);")
        self.btn_space = AnimatedButton(self.groupBox)
        self.btn_space.setObjectName(u"btn_space")
        self.btn_space.setGeometry(QRect(370, 280, 481, 51))
        font8 = QFont()
        font8.setFamily(u"MS Serif")
        font8.setPointSize(16)
        self.btn_space.setFont(font8)
        self.btn_space.setStyleSheet(u"background-color: rgb(255, 206, 108);")
        self.btn_change_lang = AnimatedButton(self.groupBox)
        self.btn_change_lang.setObjectName(u"btn_change_lang")
        self.btn_change_lang.setGeometry(QRect(10, 340, 111, 61))
        font9 = QFont()
        font9.setFamily(u"Bahnschrift SemiBold")
        font9.setPointSize(10)
        font9.setBold(True)
        font9.setWeight(75)
        self.btn_change_lang.setFont(font9)
        self.btn_change_lang.setCursor(QCursor(Qt.OpenHandCursor))
        self.btn_change_lang.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.btn_change_lang.setStyleSheet(u"background-color: rgb(255, 206, 108);")
        self.columnView = QColumnView(self.groupBox)
        self.columnView.setObjectName(u"columnView")
        self.columnView.setGeometry(QRect(140, 330, 1031, 291))
        self.show_keyboard_checkBox = QCheckBox(self.groupBox)
        self.show_keyboard_checkBox.setObjectName(u"show_keyboard_checkBox")
        self.show_keyboard_checkBox.setGeometry(QRect(10, 304, 161, 21))
        self.show_keyboard_checkBox.setBaseSize(QSize(0, 0))
        font10 = QFont()
        font10.setFamily(u"Roboto Medium")
        font10.setPointSize(10)
        self.show_keyboard_checkBox.setFont(font10)
        self.show_keyboard_checkBox.setStyleSheet(u"")
        self.show_keyboard_checkBox.setIconSize(QSize(16, 16))
        self.timeViewer = QLCDNumber(self.groupBox)
        self.timeViewer.setObjectName(u"timeViewer")
        self.timeViewer.setGeometry(QRect(1010, 440, 200, 30))
        self.timeViewer.setMinimumSize(QSize(200, 30))
        self.timeViewer.setMaximumSize(QSize(16777215, 16777215))
        font11 = QFont()
        font11.setFamily(u"Bahnschrift SemiBold")
        font11.setPointSize(9)
        font11.setBold(True)
        font11.setWeight(75)
        self.timeViewer.setFont(font11)
        self.timeViewer.setLayoutDirection(Qt.LeftToRight)
        self.timeViewer.setFrameShape(QFrame.Box)
        self.btn_str3_11 = AnimatedButton(self.groupBox)
        self.btn_str3_11.setObjectName(u"btn_str3_11")
        self.btn_str3_11.setGeometry(QRect(10, 410, 121, 61))
        self.btn_str3_11.setFont(font9)
        self.btn_str3_11.setCursor(QCursor(Qt.OpenHandCursor))
        self.btn_str3_11.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.btn_str3_11.setStyleSheet(u"background-color: rgb(255, 206, 108);")

        self.horizontalLayout_5.addWidget(self.groupBox)

        self.horizontalLayout.addWidget(self.frame_4)

        self.verticalLayout.addWidget(self.frame_2)

        MainWindow.setCentralWidget(self.styleSheet)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.typewriter.setText(QCoreApplication.translate("MainWindow", u"TYPEWRITER", None))
        self.btn_Practice.setText(
            QCoreApplication.translate("MainWindow", u"\u0422\u0440\u0435\u043d\u0430\u0436\u0435\u0440", None))
        self.btn_Lesson1.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0440\u043e\u043a 1", None))
        self.btn_Lesson2.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0440\u043e\u043a 2", None))
        self.btn_Lesson3.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0440\u043e\u043a 3", None))
        self.btn_Lesson4.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0440\u043e\u043a 4", None))
        self.btn_Lesson5.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0440\u043e\u043a 5", None))
        self.btn_Lesson6.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0440\u043e\u043a 6", None))
        self.btn_Lesson7.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0440\u043e\u043a 7", None))
        self.btn_Lesson8.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0440\u043e\u043a 8", None))
        self.btn_Lesson9.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0440\u043e\u043a 9", None))
        self.btn_Lesson10.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0440\u043e\u043a 10", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"KEYBOARD", None))
        self.btn_sth.setText(QCoreApplication.translate("MainWindow", u"\u0401", None))
        self.btn_num_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.btn_num_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.btn_num_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.btn_num_4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.btn_num_5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.btn_num_6.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.btn_num_7.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.btn_num_8.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.btn_num_9.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.btn_num_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_backspace.setText(QCoreApplication.translate("MainWindow", u"BACKSPACE", None))
        self.btn_tab.setText(QCoreApplication.translate("MainWindow", u"TAB", None))
        self.btn_str_1.setText(QCoreApplication.translate("MainWindow", u"\u0419", None))
        self.btn_str_2.setText(QCoreApplication.translate("MainWindow", u"\u0426", None))
        self.btn_str_3.setText(QCoreApplication.translate("MainWindow", u"\u0423", None))
        self.btn_str_4.setText(QCoreApplication.translate("MainWindow", u"\u041a", None))
        self.btn_str_5.setText(QCoreApplication.translate("MainWindow", u"\u0415", None))
        self.btn_str_6.setText(QCoreApplication.translate("MainWindow", u"\u041d", None))
        self.btn_str_7.setText(QCoreApplication.translate("MainWindow", u"\u0413", None))
        self.btn_str_8.setText(QCoreApplication.translate("MainWindow", u"\u0428", None))
        self.btn_str_9.setText(QCoreApplication.translate("MainWindow", u"\u0429", None))
        self.btn_str_10.setText(QCoreApplication.translate("MainWindow", u"\u0417", None))
        self.btn_str_11.setText(QCoreApplication.translate("MainWindow", u"\u0425", None))
        self.btn_minus.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.btn_ravno.setText(QCoreApplication.translate("MainWindow", u"=", None))
        self.btn_str_12.setText(QCoreApplication.translate("MainWindow", u"\u042a", None))
        self.btn_str_13.setText(QCoreApplication.translate("MainWindow", u"\\", None))
        self.btn_caps.setText(QCoreApplication.translate("MainWindow", u"CAPS", None))
        self.btn_str2_1.setText(QCoreApplication.translate("MainWindow", u"\u0424", None))
        self.btn_str2_2.setText(QCoreApplication.translate("MainWindow", u"\u042b", None))
        self.btn_str2_3.setText(QCoreApplication.translate("MainWindow", u"\u0412", None))
        self.btn_str2_4.setText(QCoreApplication.translate("MainWindow", u"\u0410", None))
        self.btn_str2_5.setText(QCoreApplication.translate("MainWindow", u"\u041f", None))
        self.btn_str2_6.setText(QCoreApplication.translate("MainWindow", u"\u0420", None))
        self.btn_str2_7.setText(QCoreApplication.translate("MainWindow", u"\u041e", None))
        self.btn_str2_8.setText(QCoreApplication.translate("MainWindow", u"\u041b", None))
        self.btn_str2_9.setText(QCoreApplication.translate("MainWindow", u"\u0414", None))
        self.btn_str2_10.setText(QCoreApplication.translate("MainWindow", u"\u0416", None))
        self.btn_str2_11.setText(QCoreApplication.translate("MainWindow", u"\u042d", None))
        self.btn_enter.setText(QCoreApplication.translate("MainWindow", u"ENTER", None))
        self.btn_Lshift.setText(QCoreApplication.translate("MainWindow", u"SHIFT", None))
        self.btn_str3_1.setText(QCoreApplication.translate("MainWindow", u"\u042f", None))
        self.btn_str3_2.setText(QCoreApplication.translate("MainWindow", u"\u0427", None))
        self.btn_str3_3.setText(QCoreApplication.translate("MainWindow", u"\u0421", None))
        self.btn_str3_4.setText(QCoreApplication.translate("MainWindow", u"\u041c", None))
        self.btn_str3_5.setText(QCoreApplication.translate("MainWindow", u"\u0418", None))
        self.btn_str3_6.setText(QCoreApplication.translate("MainWindow", u"\u0422", None))
        self.btn_str3_7.setText(QCoreApplication.translate("MainWindow", u"\u042c", None))
        self.btn_str3_8.setText(QCoreApplication.translate("MainWindow", u"\u0411", None))
        self.btn_str3_9.setText(QCoreApplication.translate("MainWindow", u"\u042e", None))
        self.btn_str3_10.setText(QCoreApplication.translate("MainWindow", u".", None))
        self.btn_Rshift.setText(QCoreApplication.translate("MainWindow", u"SHIFT", None))
        self.btn_space.setText("")
        self.btn_change_lang.setText(QCoreApplication.translate("MainWindow",
                                                                u"\u0410\u043d\u0433\u043b. \u0440\u0430\u0441\u043a\u043b\u0430\u0434\u043a\u0430",
                                                                None))
        self.show_keyboard_checkBox.setText(QCoreApplication.translate("MainWindow",
                                                                       u"\u0421\u043a\u0440\u044b\u0442\u044c \u043a\u043b\u0430\u0432\u0438\u0430\u0442\u0443\u0440\u0443",
                                                                       None))
        self.btn_str3_11.setText(QCoreApplication.translate("MainWindow",
                                                            u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c \u0441\u0442\u0438\u043b\u044c",
                                                            None))
    # retranslateUi


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('TypeWriter')
        self.setWindowIcon(QIcon('../../Desktop/Индивидуальный проект с флешки/Клавиатура/keyboard_icon.ico'))
        # ПОЛЕ ДЛЯ ЧТЕНИЯ ТЕКСТА
        self.plainTextEdit_2.setReadOnly(True)
        # ЧЕКБОКС КЛАВИАТУРЫ
        self.show_keyboard_checkBox.stateChanged.connect(self.check_answer)
        # ТЕКСТ ПО УМОЛЧАНИЮ
        self.plainTextEdit_2.setPlainText('Привет, я помогу тебе научиться печатать вслепую!')
        # РЕЖИМЫ: УРОК И ПРАКТИКА
        self.mode = 'NONE'
        self.btn_Practice.clicked.connect(lambda: self.change_mods('Practice'))
        self.btn_Lesson1.clicked.connect(lambda: self.change_mods('Lesson'))
        self.btn_Lesson2.clicked.connect(lambda: self.change_mods('Lesson'))
        self.btn_Lesson3.clicked.connect(lambda: self.change_mods('Lesson'))
        self.btn_Lesson4.clicked.connect(lambda: self.change_mods('Lesson'))
        self.btn_Lesson5.clicked.connect(lambda: self.change_mods('Lesson'))
        self.btn_Lesson6.clicked.connect(lambda: self.change_mods('Lesson'))
        self.btn_Lesson7.clicked.connect(lambda: self.change_mods('Lesson'))
        self.btn_Lesson8.clicked.connect(lambda: self.change_mods('Lesson'))
        self.btn_Lesson9.clicked.connect(lambda: self.change_mods('Lesson'))
        self.btn_Lesson10.clicked.connect(lambda: self.change_mods('Lesson'))
        #########################################################################################################
        self.btn_Practice.clicked.connect(self.random_practice_text)
        self.now_text = ''
        ##########################################################################################################
        self.btn_Lesson1.clicked.connect(lambda: self.create_widget(1, self.main_style))
        self.btn_Lesson2.clicked.connect(lambda: self.create_widget(2, self.main_style))
        self.btn_Lesson3.clicked.connect(lambda: self.create_widget(3, self.main_style))
        self.btn_Lesson4.clicked.connect(lambda: self.create_widget(4, self.main_style))
        self.btn_Lesson5.clicked.connect(lambda: self.create_widget(5, self.main_style))
        self.btn_Lesson6.clicked.connect(lambda: self.create_widget(6, self.main_style))
        self.btn_Lesson7.clicked.connect(lambda: self.create_widget(7, self.main_style))
        self.btn_Lesson8.clicked.connect(lambda: self.create_widget(8, self.main_style))
        self.btn_Lesson9.clicked.connect(lambda: self.create_widget(9, self.main_style))
        self.btn_Lesson10.clicked.connect(lambda: self.create_widget(10, self.main_style))

        #########################################################################################################
        self.main_style = 'background-color: rgb(85, 85, 127);'
        # 'background-color: rgb(255, 163, 144);'
        self.my_buttons_rus = {'ё': self.btn_sth, '1': self.btn_num_1, '2': self.btn_num_2, '3': self.btn_num_3,
                               '4': self.btn_num_4, '5': self.btn_num_5, '6': self.btn_num_6, '7': self.btn_num_7,
                               '8': self.btn_num_8, '9': self.btn_num_9, '0': self.btn_num_0, '-': self.btn_minus,
                               '=': self.btn_ravno, 'й': self.btn_str_1, 'ц': self.btn_str_2, 'у': self.btn_str_3,
                               'к': self.btn_str_4, 'е': self.btn_str_5, 'н': self.btn_str_6, 'г': self.btn_str_7,
                               'ш': self.btn_str_8, 'щ': self.btn_str_9, 'з': self.btn_str_10, 'х': self.btn_str_11,
                               'ъ': self.btn_str_12, 'ф': self.btn_str2_1, 'ы': self.btn_str2_2, 'в': self.btn_str2_3,
                               'а': self.btn_str2_4, 'п': self.btn_str2_5, 'р': self.btn_str2_6, 'о': self.btn_str2_7,
                               'л': self.btn_str2_8, 'д': self.btn_str2_9, 'ж': self.btn_str2_10, 'э': self.btn_str2_11,
                               'я': self.btn_str3_1, 'ч': self.btn_str3_2, 'с': self.btn_str3_3, 'м': self.btn_str3_4,
                               'и': self.btn_str3_5, 'т': self.btn_str3_6, 'ь': self.btn_str3_7, 'б': self.btn_str3_8,
                               'ю': self.btn_str3_9, '.': self.btn_str3_10, ' ': self.btn_space}
        self.my_buttons_eng = {'`': self.btn_sth, '1': self.btn_num_1, '2': self.btn_num_2, '3': self.btn_num_3,
                               '4': self.btn_num_4, '5': self.btn_num_5, '6': self.btn_num_6, '7': self.btn_num_7,
                               '8': self.btn_num_8, '9': self.btn_num_9, '0': self.btn_num_0, '-': self.btn_minus,
                               '=': self.btn_ravno, 'q': self.btn_str_1, 'w': self.btn_str_2, 'e': self.btn_str_3,
                               'r': self.btn_str_4, 't': self.btn_str_5, 'y': self.btn_str_6, 'u': self.btn_str_7,
                               'i': self.btn_str_8, 'o': self.btn_str_9, 'p': self.btn_str_10, '[': self.btn_str_11,
                               ']': self.btn_str_12, 'a': self.btn_str2_1, 's': self.btn_str2_2, 'd': self.btn_str2_3,
                               'f': self.btn_str2_4, 'g': self.btn_str2_5, 'h': self.btn_str2_6, 'j': self.btn_str2_7,
                               'k': self.btn_str2_8, 'l': self.btn_str2_9, ';': self.btn_str2_10, '"': self.btn_str2_11,
                               'z': self.btn_str3_1, 'x': self.btn_str3_2, 'c': self.btn_str3_3, 'v': self.btn_str3_4,
                               'b': self.btn_str3_5, 'n': self.btn_str3_6, 'm': self.btn_str3_7, ',': self.btn_str3_8,
                               '.': self.btn_str3_9, '/': self.btn_str3_10, ' ': self.btn_space}
        self.all_buttons = [self.btn_sth, self.btn_num_1, self.btn_num_2, self.btn_num_4, self.btn_num_5,
                            self.btn_num_6, self.btn_num_7, self.btn_num_8, self.btn_num_9, self.btn_num_0,
                            self.btn_minus, self.btn_ravno, self.btn_str_1, self.btn_str_2, self.btn_str_3,
                            self.btn_str_4, self.btn_str_5, self.btn_str_6, self.btn_str_7, self.btn_str_8,
                            self.btn_str_9, self.btn_str_10, self.btn_str_11, self.btn_tab, self.btn_str_12,
                            self.btn_Rshift, self.btn_Lshift, self.btn_str2_1, self.btn_str2_2, self.btn_caps,
                            self.btn_str2_3, self.btn_str2_4, self.btn_str2_5, self.btn_str2_6, self.btn_str2_7,
                            self.btn_str2_8, self.btn_str2_9, self.btn_str2_10, self.btn_str2_11, self.btn_str3_1,
                            self.btn_enter, self.btn_str_13, self.btn_str3_2, self.btn_str3_3, self.btn_str3_4,
                            self.btn_str3_5, self.btn_str3_6, self.btn_str3_7, self.btn_str3_8, self.btn_str3_9,
                            self.btn_str3_10, self.btn_space, self.btn_str3_11, self.btn_num_3, self.btn_backspace,
                            self.btn_change_lang]
        self.now_lang_buttons = self.my_buttons_rus

        for elem in self.all_buttons:
            elem.setStyleSheet(self.main_style)

        self.btn_str3_11.clicked.connect(self.change_color)
        #########################################################################################################
        self.plainTextEdit.textChanged.connect(self.find_out_pte_text)
        self.text_in_PTE = ''
        self.plainTextEdit_2.textChanged.connect(self.find_out_pte2_text)
        self.text_in_PTE_2 = self.plainTextEdit_2.toPlainText()

        self.plainTextEdit.textChanged.connect(self.wrong_text)
        self.plainTextEdit.textChanged.connect(self.text_is_printed)
        self.plainTextEdit.textChanged.connect(self.click_change_color)
        self.len_of_text = 0
        # ТАЙМЕР ################################################################################################
        self.btn_Practice.clicked.connect(self.create_timer)
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.show_time)
        self.time = 0
        self.timeInterval = 1000
        ########################################################################################################
        self.btn_Practice.clicked.connect(lambda: self.click_change_color(practice_or_lesson=True))
        # ИЗМЕНЕНИЕ ЯЗЫКА ######################################################################################
        self.btn_change_lang.clicked.connect(self.change_lang)
        self.now_lang = 'rus'

        self.widget_flag = False
        self.wdg = None

        # Plain Text Edit ScrollBar
        self.plainTextEdit.verticalScrollBar().rangeChanged.connect(
            lambda: self.plainTextEdit_2.verticalScrollBar().setValue(self.plainTextEdit.verticalScrollBar().maximum()))

    #########################################################################################################
    # FUNCTIONS #############################################################################################
    #########################################################################################################

    def find_out_pte_text(self):
        self.text_in_PTE = self.plainTextEdit.toPlainText()

    def find_out_pte2_text(self):
        self.text_in_PTE_2 = self.plainTextEdit_2.toPlainText()

    def change_lang(self):
        self.columnView.move(160, 330)
        self.show_keyboard_checkBox.setChecked(False)
        time.sleep(0.1)
        if self.now_lang == 'rus':
            for letter in self.my_buttons_eng:
                self.my_buttons_eng[letter].setText(letter.upper())
            self.now_lang = 'eng'
            self.btn_change_lang.setText('Рус. раскалдка')
            self.now_lang_buttons = self.my_buttons_eng
        elif self.now_lang == 'eng':
            for letter in self.my_buttons_rus:
                self.my_buttons_rus[letter].setText(letter.upper())
            self.now_lang = 'rus'
            self.btn_change_lang.setText('Англ. раскалдка')
            self.now_lang_buttons = self.my_buttons_rus

    def click_change_color(self, practice_or_lesson=False):
        if not self.show_keyboard_checkBox.isChecked():
            old_len = self.len_of_text
            self.len_of_text = len(self.text_in_PTE)
            if self.len_of_text > old_len:
                if self.text_in_PTE[-1].isupper():
                    self.turn_gray_and_return(self.btn_Lshift)
                last_letter = self.text_in_PTE.lower()[-1]
                if last_letter in self.now_lang_buttons:
                    self.turn_gray_and_return(self.now_lang_buttons[last_letter])
            else:
                if not practice_or_lesson:
                    self.turn_gray_and_return(self.btn_backspace)
                else:
                    self.btn_backspace.setStyleSheet(self.main_style)

    def turn_gray_and_return(self, button):
        # button.setStyleSheet("background-color: rgb(115, 115, 115);")
        button.color_clicked()

        # threading.Timer(0.3, lambda: button.setStyleSheet(self.main_style)).start()

    def change_color(self):
        self.columnView.move(160, 330)
        self.show_keyboard_checkBox.setChecked(False)
        time.sleep(0.1)
        style_number = my_styles.index(self.main_style)
        if style_number + 1 <= len(my_styles) - 1:
            self.main_style = my_styles[style_number + 1]
        else:
            self.main_style = my_styles[0]
        for button in self.all_buttons:
            button.setStyleSheet(self.main_style)

    def random_practice_text(self):
        try:
            self.wdg.close()
        except AttributeError:
            pass
        if self.now_lang == 'rus':
            text = choice(practice_texts)
        else:
            text = choice(practice_texts_eng)
        if text != self.now_text:
            time.sleep(0.1)
            file = open(text, encoding='utf-8')
            self.plainTextEdit_2.setPlainText(file.read())
            self.plainTextEdit.setPlainText('')
            self.now_text = text
            file.close()
        else:
            self.random_practice_text()

    def check_answer(self, state):
        if state:
            self.columnView.move(100, 40)
        else:
            self.columnView.move(160, 330)

    def create_timer(self):
        self.time = 0
        self.timer.start(1000)
        self.timeViewer.display(self.time)

    def show_time(self):
        self.time += 1
        self.set_timer(self.time)
        # #print(self.time)

    def set_timer(self, int_):
        self.time = int_
        self.timeViewer.display(self.time)

    def change_mods(self, mode):
        if mode == 'Practice':
            self.mode = 'Practice'
        elif mode == 'Lesson':
            self.mode = 'Lesson'

    def text_is_printed(self):
        if self.text_in_PTE == self.text_in_PTE_2:
            time.sleep(0.1)
            if self.mode == 'Practice':
                speed = round((len(self.text_in_PTE_2) / self.time) * 60, 0)
                end = ''
                if speed % 100 in (11, 12, 13, 14) or speed % 10 in (5, 6, 7, 8, 9, 0):
                    end = 'ов'
                elif speed % 10 in (2, 3, 4):
                    end = 'a'
                self.plainTextEdit_2.setPlainText(
                    f'Ваша скорость печати: {speed} символ{end} в минуту.')
                self.mode = 'NONE'
                self.timer.stop()
                self.time = 0
            elif self.mode == 'Lesson':
                self.plainTextEdit_2.setPlainText('Вы прошли урок!')
            elif self.mode == 'NONE':
                self.plainTextEdit_2.setPlainText('Так держать!')
            self.set_no_text()

    def set_no_text(self):
        self.plainTextEdit.setPlainText('')
        self.click_change_color(practice_or_lesson=True)

    def wrong_text(self):
        if self.text_in_PTE != self.text_in_PTE_2[:len(self.text_in_PTE)]:
            self.plainTextEdit.setStyleSheet('color: rgb(255, 0, 0);')
        else:
            self.plainTextEdit.setStyleSheet('color: rgb(232, 232, 232);')
            if not self.show_keyboard_checkBox.isChecked():
                if len(self.text_in_PTE) < len(self.text_in_PTE_2):
                    next_letter = self.text_in_PTE_2[len(self.text_in_PTE)].lower()
                    if next_letter in self.now_lang_buttons:
                        for letter in self.now_lang_buttons:
                            self.now_lang_buttons[letter].setStyleSheet(self.main_style)
                        self.now_lang_buttons[next_letter].setStyleSheet('background-color: rgb(133, 255, 141);')

    def create_widget(self, num, style):
        try:
            self.wdg.close()
        except AttributeError:
            pass
        self.wdg = LessonWidget(self, num, style, self.now_lang)
        self.wdg.setWindowTitle(f'Урок {num}')
        self.wdg.show()


if __name__ == "__main__":
    try:
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = MyWidget()
        MainWindow.show()
        sys.exit(app.exec_())
    except Exception as e:
        print(e)
