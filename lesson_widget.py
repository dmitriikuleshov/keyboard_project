from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_LessonWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(471, 464)
        MainWindow.setMinimumSize(QSize(471, 464))
        MainWindow.setMaximumSize(QSize(471, 464))
        MainWindow.setStyleSheet(u"QPushButton{\n"
                                 "	padding: 10 px;\n"
                                 "	background-color: #ffc595;\n"
                                 "	border-radius: 5px;\n"
                                 "}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"#centralwidget{\n"
                                         "	background-color: #004F4D;\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton{\n"
                                         "	background-color: #1F2024;\n"
                                         "	color: rgb(200, 200, 200);\n"
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
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.widget_btn_1 = QPushButton(self.centralwidget)
        self.widget_btn_1.setObjectName(u"widget_btn_1")
        self.widget_btn_1.setMinimumSize(QSize(400, 0))
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.widget_btn_1.setFont(font)
        self.widget_btn_1.setCursor(QCursor(Qt.OpenHandCursor))
        self.widget_btn_1.setStyleSheet(u"")

        self.gridLayout.addWidget(self.widget_btn_1, 1, 0, 1, 1)

        self.widget_btn_7 = QPushButton(self.centralwidget)
        self.widget_btn_7.setObjectName(u"widget_btn_7")
        self.widget_btn_7.setFont(font)
        self.widget_btn_7.setCursor(QCursor(Qt.OpenHandCursor))
        self.widget_btn_7.setStyleSheet(u"")

        self.gridLayout.addWidget(self.widget_btn_7, 7, 0, 1, 1)

        self.widget_btn_5 = QPushButton(self.centralwidget)
        self.widget_btn_5.setObjectName(u"widget_btn_5")
        self.widget_btn_5.setFont(font)
        self.widget_btn_5.setCursor(QCursor(Qt.OpenHandCursor))
        self.widget_btn_5.setStyleSheet(u"")

        self.gridLayout.addWidget(self.widget_btn_5, 5, 0, 1, 1)

        self.widget_btn_9 = QPushButton(self.centralwidget)
        self.widget_btn_9.setObjectName(u"widget_btn_9")
        self.widget_btn_9.setFont(font)
        self.widget_btn_9.setCursor(QCursor(Qt.OpenHandCursor))
        self.widget_btn_9.setStyleSheet(u"")

        self.gridLayout.addWidget(self.widget_btn_9, 9, 0, 1, 1)

        self.widget_btn_6 = QPushButton(self.centralwidget)
        self.widget_btn_6.setObjectName(u"widget_btn_6")
        self.widget_btn_6.setFont(font)
        self.widget_btn_6.setCursor(QCursor(Qt.OpenHandCursor))
        self.widget_btn_6.setStyleSheet(u"")

        self.gridLayout.addWidget(self.widget_btn_6, 6, 0, 1, 1)

        self.widget_btn_4 = QPushButton(self.centralwidget)
        self.widget_btn_4.setObjectName(u"widget_btn_4")
        self.widget_btn_4.setFont(font)
        self.widget_btn_4.setCursor(QCursor(Qt.OpenHandCursor))
        self.widget_btn_4.setStyleSheet(u"")

        self.gridLayout.addWidget(self.widget_btn_4, 4, 0, 1, 1)

        self.widget_btn_2 = QPushButton(self.centralwidget)
        self.widget_btn_2.setObjectName(u"widget_btn_2")
        self.widget_btn_2.setFont(font)
        self.widget_btn_2.setCursor(QCursor(Qt.OpenHandCursor))
        self.widget_btn_2.setStyleSheet(u"")

        self.gridLayout.addWidget(self.widget_btn_2, 2, 0, 1, 1)

        self.widget_btn_3 = QPushButton(self.centralwidget)
        self.widget_btn_3.setObjectName(u"widget_btn_3")
        self.widget_btn_3.setFont(font)
        self.widget_btn_3.setCursor(QCursor(Qt.OpenHandCursor))
        self.widget_btn_3.setStyleSheet(u"")

        self.gridLayout.addWidget(self.widget_btn_3, 3, 0, 1, 1)

        self.widget_btn_8 = QPushButton(self.centralwidget)
        self.widget_btn_8.setObjectName(u"widget_btn_8")
        self.widget_btn_8.setFont(font)
        self.widget_btn_8.setCursor(QCursor(Qt.OpenHandCursor))
        self.widget_btn_8.setStyleSheet(u"")

        self.gridLayout.addWidget(self.widget_btn_8, 8, 0, 1, 1)

        self.widget_btn_10 = QPushButton(self.centralwidget)
        self.widget_btn_10.setObjectName(u"widget_btn_10")
        self.widget_btn_10.setFont(font)
        self.widget_btn_10.setCursor(QCursor(Qt.OpenHandCursor))
        self.widget_btn_10.setStyleSheet(u"")

        self.gridLayout.addWidget(self.widget_btn_10, 10, 0, 1, 1)

        self.gridLayout_2.addLayout(self.gridLayout, 0, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 0, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 0, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.widget_btn_1.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.widget_btn_7.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.widget_btn_5.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.widget_btn_9.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.widget_btn_6.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.widget_btn_4.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.widget_btn_2.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.widget_btn_3.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.widget_btn_8.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.widget_btn_10.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
    # retranslateUi


class LessonWidget(QMainWindow, Ui_LessonWindow):
    def __init__(self, obj, num, style, lang):
        super().__init__()
        self.setupUi(self)
        try:
            self.setWindowIcon(QIcon('open-book.ico'))
        except Exception as e:
            print(e)
        self.obj = obj
        self.lesson_number = num
        self.now_lang = lang
        self.main_style = style
        self.all_buttons = [self.widget_btn_1, self.widget_btn_2, self.widget_btn_3,
                            self.widget_btn_4, self.widget_btn_5, self.widget_btn_6,
                            self.widget_btn_7, self.widget_btn_8, self.widget_btn_9,
                            self.widget_btn_10]
        self.set_buttons_text()

        self.widget_btn_1.clicked.connect(lambda: self.set_selected_lesson_part(1))
        self.widget_btn_2.clicked.connect(lambda: self.set_selected_lesson_part(2))
        self.widget_btn_3.clicked.connect(lambda: self.set_selected_lesson_part(3))
        self.widget_btn_4.clicked.connect(lambda: self.set_selected_lesson_part(4))
        self.widget_btn_5.clicked.connect(lambda: self.set_selected_lesson_part(5))
        self.widget_btn_6.clicked.connect(lambda: self.set_selected_lesson_part(6))
        self.widget_btn_7.clicked.connect(lambda: self.set_selected_lesson_part(7))
        self.widget_btn_8.clicked.connect(lambda: self.set_selected_lesson_part(8))
        self.widget_btn_9.clicked.connect(lambda: self.set_selected_lesson_part(9))
        self.widget_btn_10.clicked.connect(lambda: self.set_selected_lesson_part(10))

    def set_buttons_text(self):
        if self.lesson_number == 1:
            self.widget_btn_1.setText('Новые клавиши: Главный ряд')
            self.widget_btn_2.setText('Упражнение «Новые клавиши» 1')
            self.widget_btn_3.setText('Упражнение «Новые клавиши» 2')
            self.widget_btn_4.setText('Упражнение «Клавиши» 1')
            self.widget_btn_5.setText('Упражнение «Клавиши» 2')
            self.widget_btn_6.setText('Упражнение «Слова»')
            self.widget_btn_7.setText('Дополнительные упражнение «Клавиши»')
            self.widget_btn_8.setText('Дополнительные упражнение «Слова»')
            self.widget_btn_9.setText('_')
            self.widget_btn_10.setText('_')
        elif self.lesson_number == 2:
            self.widget_btn_1.setText('Новые клавиши: п и р')
            self.widget_btn_2.setText('Упражнение «Новые клавиши» 1')
            self.widget_btn_3.setText('Упражнение «Новые клавиши» 2')
            self.widget_btn_4.setText('Упражнение «Клавиши» 1')
            self.widget_btn_5.setText('Упражнение «Клавиши» 2')
            self.widget_btn_6.setText('Упражнение «Слова»')
            self.widget_btn_7.setText('Упражнение «Слепые слова» 1')
            self.widget_btn_8.setText('Упражнение «Слепые слова» 2')
            self.widget_btn_9.setText('Упражнение «Текст»')
            self.widget_btn_10.setText('_')
        elif self.lesson_number == 3:
            self.widget_btn_1.setText('Новые клавиши: к и г')
            self.widget_btn_2.setText('Упражнение «Новые клавиши» 1')
            self.widget_btn_3.setText('Упражнение «Новые клавиши» 2')
            self.widget_btn_4.setText('Упражнение «Клавиши» 1')
            self.widget_btn_5.setText('Упражнение «Клавиши» 2')
            self.widget_btn_6.setText('Упражнение «Слова»')
            self.widget_btn_7.setText('Упражнение «Слепые слова»')
            self.widget_btn_8.setText('Упражнение «Текст»')
            self.widget_btn_9.setText('_')
            self.widget_btn_10.setText('_')
        elif self.lesson_number == 4:
            self.widget_btn_1.setText('Новые клавиши: у и ш')
            self.widget_btn_2.setText('Упражнение «Новые клавиши» 1')
            self.widget_btn_3.setText('Упражнение «Новые клавиши» 2')
            self.widget_btn_4.setText('Упражнение «Клавиши» 1')
            self.widget_btn_5.setText('Упражнение «Клавиши» 2')
            self.widget_btn_6.setText('Упражнение «Слова»')
            self.widget_btn_7.setText('Упражнение «Слепые слова» 1')
            self.widget_btn_8.setText('Упражнение «Слепые слова» 2')
            self.widget_btn_9.setText('Упражнение «Текст»')
            self.widget_btn_10.setText('_')
        elif self.lesson_number == 5:
            self.widget_btn_1.setText('Новые клавиши: м, ь и')
            self.widget_btn_2.setText('Упражнение «Новые клавиши» 1')
            self.widget_btn_3.setText('Упражнение «Новые клавиши» 2')
            self.widget_btn_4.setText('Упражнение «Клавиши» 1')
            self.widget_btn_5.setText('Упражнение «Клавиши» 2')
            self.widget_btn_6.setText('Упражнение «Слова»')
            self.widget_btn_7.setText('Упражнение «Слепые слова» 1')
            self.widget_btn_8.setText('Упражнение «Слепые слова» 2')
            self.widget_btn_9.setText('Упражнение «Текст»')
            self.widget_btn_10.setText('_')
        elif self.lesson_number == 6:
            self.widget_btn_1.setText('Заглавные буквы')
            self.widget_btn_2.setText('Упражнение «Новые клавиши» 1')
            self.widget_btn_3.setText('Упражнение «Новые клавиши» 2')
            self.widget_btn_4.setText('Упражнение «Клавиши» 1')
            self.widget_btn_5.setText('Упражнение «Клавиши» 2')
            self.widget_btn_6.setText('Упражнение «Слова»')
            self.widget_btn_7.setText('Упражнение «Слепые слова» 1')
            self.widget_btn_8.setText('Упражнение «Слепые слова» 2')
            self.widget_btn_9.setText('Упражнение «Текст»')
            self.widget_btn_10.setText('_')
        elif self.lesson_number == 7:
            self.widget_btn_1.setText('Новые клавиши: и, т и ,')
            self.widget_btn_2.setText('Упражнение «Новые клавиши» 1')
            self.widget_btn_3.setText('Упражнение «Новые клавиши» 2')
            self.widget_btn_4.setText('Упражнение «Клавиши» 1')
            self.widget_btn_5.setText('Упражнение «Клавиши» 2')
            self.widget_btn_6.setText('Упражнение «Слова»')
            self.widget_btn_7.setText('Упражнение «Слепые слова» 1')
            self.widget_btn_8.setText('Упражнение «Слепые слова» 2')
            self.widget_btn_9.setText('Упражнение «Текст»')
            self.widget_btn_10.setText('_')
        elif self.lesson_number == 8:
            self.widget_btn_1.setText('Новые клавиши: с и б')
            self.widget_btn_2.setText('Упражнение «Новые клавиши» 1')
            self.widget_btn_3.setText('Упражнение «Новые клавиши» 2')
            self.widget_btn_4.setText('Упражнение «Клавиши» 1')
            self.widget_btn_5.setText('Упражнение «Клавиши» 2')
            self.widget_btn_6.setText('Упражнение «Слова»')
            self.widget_btn_7.setText('Упражнение «Слепые слова» 1')
            self.widget_btn_8.setText('Упражнение «Слепые слова» 2')
            self.widget_btn_9.setText('Упражнение «Текст»')
            self.widget_btn_10.setText('_')
        elif self.lesson_number == 9:
            self.widget_btn_1.setText('Новые клавиши: е и н')
            self.widget_btn_2.setText('Упражнение «Новые клавиши» 1')
            self.widget_btn_3.setText('Упражнение «Новые клавиши» 2')
            self.widget_btn_4.setText('Упражнение «Клавиши» 1')
            self.widget_btn_5.setText('Упражнение «Клавиши» 2')
            self.widget_btn_6.setText('Упражнение «Слова»')
            self.widget_btn_7.setText('Упражнение «Слепые слова» 1')
            self.widget_btn_8.setText('Упражнение «Слепые слова» 2')
            self.widget_btn_9.setText('Упражнение «Текст» 1')
            self.widget_btn_10.setText('Упражнение «Текст» 2')
        elif self.lesson_number == 10:
            self.widget_btn_1.setText('Новые клавиши: й и з')
            self.widget_btn_2.setText('Упражнение «Новые клавиши» 1')
            self.widget_btn_3.setText('Упражнение «Новые клавиши» 2')
            self.widget_btn_4.setText('Упражнение «Клавиши» 1')
            self.widget_btn_5.setText('Упражнение «Клавиши» 2')
            self.widget_btn_6.setText('Упражнение «Слова»')
            self.widget_btn_7.setText('Упражнение «Слепые слова» 1')
            self.widget_btn_8.setText('Упражнение «Слепые слова» 2')
            self.widget_btn_9.setText('Упражнение «Текст» 1')
            self.widget_btn_10.setText('Упражнение «Текст» 2')

    @pyqtSlot()
    def set_selected_lesson_part(self, num):
        try:
            file = open(f'Lessons_{self.now_lang}/Lesson_{self.lesson_number}/Part_{num}.txt', encoding='utf-8')
            self.obj.plainTextEdit_2.setPlainText(file.read())
            self.obj.plainTextEdit.setPlainText('')
            file.close()
            self.close()
        except FileNotFoundError:
            pass
