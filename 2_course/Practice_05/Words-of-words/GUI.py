from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QFontDatabase

class Ui_mainmenu(object):
    def setupUi(self, mainmenu):
        mainmenu.setObjectName("mainmenu")
        mainmenu.resize(1440, 1024)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(mainmenu.sizePolicy().hasHeightForWidth())
        mainmenu.setSizePolicy(sizePolicy)
        mainmenu.setMinimumSize(QtCore.QSize(1440, 1024))
        mainmenu.setMaximumSize(QtCore.QSize(16777215, 16777215))
        mainmenu.setFocusPolicy(QtCore.Qt.NoFocus)
        mainmenu.setAutoFillBackground(False)
        mainmenu.setStyleSheet("QMainWindow{\n"
"border-image: url(:/back/resources/sprites/mainmenu.png);\n"
"border-position:center;\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(mainmenu)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(-1, 11, -1, 12)
        self.gridLayout.setHorizontalSpacing(7)
        self.gridLayout.setVerticalSpacing(27)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 4, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 10, 0, 1, 1)
        self.settings = QtWidgets.QPushButton(self.centralwidget)
        self.settings.setMinimumSize(QtCore.QSize(329, 89))
        self.settings.setMaximumSize(QtCore.QSize(329, 89))
        self.settings.setStyleSheet("QPushButton{\n"
"border-image: url(:/back/resources/sprites/btsettings.png);\n"
"border: none;\n"
"border-radus: 9px;}\n"
"QPushButton:hover{\n"
"border-image: url(:/back/resources/sprites/pressbtsettings.png);\n"
"border: none;\n"
"border-radus: 9px;\n"
"}")
        self.settings.setText("")
        self.settings.setObjectName("settings")
        self.gridLayout.addWidget(self.settings, 7, 0, 1, 1)
        self.rules = QtWidgets.QPushButton(self.centralwidget)
        self.rules.setMinimumSize(QtCore.QSize(329, 89))
        self.rules.setMaximumSize(QtCore.QSize(329, 89))
        self.rules.setStyleSheet("QPushButton{\n"
"border-image: url(:/back/resources/sprites/btrules.png);\n"
"border: none;\n"
"border-radus: 9px;}\n"
"QPushButton:hover{\n"
"border-image: url(:/back/resources/sprites/pressbtrules.png);\n"
"border: none;\n"
"border-radus: 9px;\n"
"}")
        self.rules.setText("")
        self.rules.setObjectName("rules")
        self.gridLayout.addWidget(self.rules, 8, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 2, 0, 1, 1)
        self.exit = QtWidgets.QPushButton(self.centralwidget)
        self.exit.setMinimumSize(QtCore.QSize(329, 89))
        self.exit.setMaximumSize(QtCore.QSize(329, 89))
        self.exit.setStyleSheet("QPushButton{\n"
"border-image: url(:/back/resources/sprites/btexit.png);\n"
"border: none;\n"
"border-radus: 9px;}\n"
"QPushButton:hover{\n"
"border-image: url(:/back/resources/sprites/pressbtexit.png);\n"
"border: none;\n"
"border-radus: 9px;\n"
"}")
        self.exit.setText("")
        self.exit.setObjectName("exit")
        self.gridLayout.addWidget(self.exit, 9, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 3, 0, 1, 1)
        self.play = QtWidgets.QPushButton(self.centralwidget)
        self.play.setMinimumSize(QtCore.QSize(329, 89))
        self.play.setMaximumSize(QtCore.QSize(329, 89))
        self.play.setAutoFillBackground(False)
        self.play.setStyleSheet("QPushButton{\n"
"border-image: url(:/back/resources/sprites/btplay.png);\n"
"border: none;\n"
"border-radus: 9px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border-image: url(:/back/resources/sprites/pressbtplay.png);\n"
"border: none;\n"
"border-radus: 9px;\n"
"}\n"
"\n"
"")
        self.play.setText("")
        self.play.setObjectName("play")
        self.gridLayout.addWidget(self.play, 6, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem4, 5, 0, 1, 1)
        mainmenu.setCentralWidget(self.centralwidget)

        self.retranslateUi(mainmenu)
        QtCore.QMetaObject.connectSlotsByName(mainmenu)

    def retranslateUi(self, mainmenu):
        _translate = QtCore.QCoreApplication.translate
        mainmenu.setWindowTitle(_translate("mainmenu", "Подушечки из котиков"))


class Ui_exit(object):
    def setupUi(self, exit):
        exit.setObjectName("exit")
        exit.resize(1440, 1024)
        exit.setMinimumSize(QtCore.QSize(1440, 1024))
        exit.setMaximumSize(QtCore.QSize(16777215, 16777215))
        exit.setStyleSheet("QMainWindow{\n"
"border-image: url(:/back/resources/sprites/exit.png);\n"
"border-position: center;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(exit)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(-1, 140, -1, 0)
        self.gridLayout.setHorizontalSpacing(80)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 0, 0, 1, 1)
        self.yes = QtWidgets.QPushButton(self.centralwidget)
        self.yes.setMinimumSize(QtCore.QSize(144, 67))
        self.yes.setMaximumSize(QtCore.QSize(144, 67))
        self.yes.setStyleSheet("QPushButton{\n"
"background-image: url(:/back/resources/sprites/Yes.png);\n"
"border: none;\n"
"border-radus: 9px;}\n"
"\n"
"QPushButton:hover{\n"
"background-image: url(:/back/resources/sprites/pressYes.png);\n"
"border: none;\n"
"border-radus: 9px;\n"
"}\n"
"\n"
"")
        self.yes.setText("")
        self.yes.setObjectName("yes")
        self.gridLayout.addWidget(self.yes, 1, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 1, 3, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 2, 0, 1, 1)
        self.no = QtWidgets.QPushButton(self.centralwidget)
        self.no.setMinimumSize(QtCore.QSize(144, 67))
        self.no.setMaximumSize(QtCore.QSize(144, 67))
        self.no.setStyleSheet("QPushButton{\n"
"background-image: url(:/back/resources/sprites/No.png);\n"
"border: none;\n"
"border-radus: 9px;}\n"
"\n"
"QPushButton:hover{\n"
"background-image: url(:/back/resources/sprites/pressNo.png);\n"
"border: none;\n"
"border-radus: 9px;\n"
"}\n"
"\n"
"")
        self.no.setText("")
        self.no.setObjectName("no")
        self.gridLayout.addWidget(self.no, 1, 2, 1, 1)
        exit.setCentralWidget(self.centralwidget)

        self.retranslateUi(exit)
        QtCore.QMetaObject.connectSlotsByName(exit)

    def retranslateUi(self, exit):
        _translate = QtCore.QCoreApplication.translate
        exit.setWindowTitle(_translate("exit", "MainWindow"))


class Ui_rule(object):
    def setupUi(self, rule):
        rule.setObjectName("rule")
        rule.resize(1440, 1024)
        rule.setMinimumSize(QtCore.QSize(1440, 1024))
        rule.setStyleSheet("QMainWindow{\n"
"border-image: url(:/back/resources/sprites/rules-1.png);\n"
"border-position: center;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(rule)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(31)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btnleft = QtWidgets.QPushButton(self.centralwidget)
        self.btnleft.setMinimumSize(QtCore.QSize(85, 77))
        self.btnleft.setMaximumSize(QtCore.QSize(85, 77))
        self.btnleft.setStyleSheet("QPushButton{\n"
"background-image: url(:/back/resources/sprites/left.png);\n"
"border: none;\n"
"border-radus: 9px;}\n"
"\n"
"QPushButton:hover{\n"
"background-image: url(:/back/resources/sprites/pressleft.png);\n"
"border: none;\n"
"border-radus: 9px;\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"background-image: url(:/back/resources/sprites/leftoff.png);\n"
"border: none;\n"
"border-radus: 9px;\n"
"}")
        self.btnleft.setText("")
        self.btnleft.setObjectName("btnleft")
        self.horizontalLayout.addWidget(self.btnleft)
        self.btnright = QtWidgets.QPushButton(self.centralwidget)
        self.btnright.setMinimumSize(QtCore.QSize(85, 77))
        self.btnright.setMaximumSize(QtCore.QSize(85, 77))
        self.btnright.setStyleSheet("QPushButton{\n"
"background-image: url(:/back/resources/sprites/right.png);\n"
"border: none;\n"
"border-radus: 9px;}\n"
"\n"
"QPushButton:hover{\n"
"background-image: url(:/back/resources/sprites/pressright.png);\n"
"border: none;\n"
"border-radus: 9px;\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"background-image: url(:/back/resources/sprites/rightoff.png);\n"
"border: none;\n"
"border-radus: 9px;\n"
"}\n"
"")
        self.btnright.setText("")
        self.btnright.setObjectName("btnright")
        self.horizontalLayout.addWidget(self.btnright)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btnmainmenu = QtWidgets.QPushButton(self.centralwidget)
        self.btnmainmenu.setMinimumSize(QtCore.QSize(107, 95))
        self.btnmainmenu.setMaximumSize(QtCore.QSize(107, 95))
        self.btnmainmenu.setStyleSheet("QPushButton{\n"
"background-image: url(:/back/resources/sprites/btmainmenu.png);\n"
"border: none;\n"
"border-radus: 9px;}\n"
"\n"
"QPushButton:hover{\n"
"background-image: url(:/back/resources/sprites/pressbtmainmenu.png);\n"
"border: none;\n"
"border-radus: 9px;\n"
"}\n"
"")
        self.btnmainmenu.setText("")
        self.btnmainmenu.setObjectName("btnmainmenu")
        self.horizontalLayout_2.addWidget(self.btnmainmenu)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 1, 0, 1, 1)
        rule.setCentralWidget(self.centralwidget)

        self.retranslateUi(rule)
        QtCore.QMetaObject.connectSlotsByName(rule)

    def retranslateUi(self, rule):
        _translate = QtCore.QCoreApplication.translate
        rule.setWindowTitle(_translate("rule", "MainWindow"))
        self.btnmainmenu.setToolTip(_translate("rule", "меню"))


class Ui_settings(object):
    def setupUi(self, settings):
        settings.setObjectName("settings")
        settings.resize(1440, 1024)
        settings.setMinimumSize(QtCore.QSize(1440, 1024))
        settings.setStyleSheet("QMainWindow{\n"
"border-image: url(:/back/resources/sprites/settings.png);\n"
"border-position: center;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(settings)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(440, 5, 440, 200)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnon = QtWidgets.QPushButton(self.centralwidget)
        self.btnon.setMinimumSize(QtCore.QSize(182, 84))
        self.btnon.setMaximumSize(QtCore.QSize(182, 84))
        self.btnon.setStyleSheet("QPushButton{\n"
"border-image: url(:/back/resources/sprites/On.png);\n"
"border: none;\n"
"border-radus: 9px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border-image: url(:/back/resources/sprites/pressOn.png);\n"
"border: none;\n"
"border-radus: 9px;\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"border-image: url(:/back/resources/sprites/Onoff.png);\n"
"border: none;\n"
"border-radus: 9px;\n"
"}\n"
"")
        self.btnon.setText("")
        self.btnon.setObjectName("btnon")
        self.horizontalLayout.addWidget(self.btnon)
        self.btnoff = QtWidgets.QPushButton(self.centralwidget)
        self.btnoff.setMinimumSize(QtCore.QSize(182, 84))
        self.btnoff.setMaximumSize(QtCore.QSize(182, 84))
        self.btnoff.setStyleSheet("QPushButton{\n"
"border-image: url(:/back/resources/sprites/Off.png);\n"
"border: none;\n"
"border-radus: 9px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border-image: url(:/back/resources/sprites/pressOff.png);\n"
"border: none;\n"
"border-radus: 9px;\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"border-image: url(:/back/resources/sprites/Offoff.png);\n"
"border: none;\n"
"border-radus: 9px;\n"
"}\n"
"\n"
"\n"
"")
        self.btnoff.setText("")
        self.btnoff.setObjectName("btnoff")
        self.horizontalLayout.addWidget(self.btnoff)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(11, 0, 0, 6)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.btnmainmenu = QtWidgets.QPushButton(self.centralwidget)
        self.btnmainmenu.setMinimumSize(QtCore.QSize(107, 95))
        self.btnmainmenu.setMaximumSize(QtCore.QSize(107, 95))
        self.btnmainmenu.setStyleSheet("QPushButton{\n"
"background-image: url(:/back/resources/sprites/btmainmenu.png);\n"
"border: none;\n"
"border-radus: 9px;}\n"
"\n"
"QPushButton:hover{\n"
"background-image: url(:/back/resources/sprites/pressbtmainmenu.png);\n"
"border: none;\n"
"border-radus: 9px;\n"
"}\n"
"")
        self.btnmainmenu.setText("")
        self.btnmainmenu.setObjectName("btnmainmenu")
        self.horizontalLayout_4.addWidget(self.btnmainmenu)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.gridLayout.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 4, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 1, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(440, 80, 440, -1)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btnon_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btnon_2.setMinimumSize(QtCore.QSize(182, 84))
        self.btnon_2.setMaximumSize(QtCore.QSize(182, 84))
        self.btnon_2.setStyleSheet("QPushButton{\n"
"border-image: url(:/back/resources/sprites/On.png);\n"
"border: none;\n"
"border-radus: 9px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border-image: url(:/back/resources/sprites/pressOn.png);\n"
"border: none;\n"
"border-radus: 9px;\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"border-image: url(:/back/resources/sprites/Onoff.png);\n"
"border: none;\n"
"border-radus: 9px;\n"
"}\n"
"\n"
"\n"
"")
        self.btnon_2.setText("")
        self.btnon_2.setObjectName("btnon_2")
        self.horizontalLayout_3.addWidget(self.btnon_2)
        self.btnoff_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btnoff_2.setMinimumSize(QtCore.QSize(182, 84))
        self.btnoff_2.setMaximumSize(QtCore.QSize(182, 84))
        self.btnoff_2.setStyleSheet("QPushButton{\n"
"border-image: url(:/back/resources/sprites/Off.png);\n"
"border: none;\n"
"border-radus: 9px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border-image: url(:/back/resources/sprites/pressOff.png);\n"
"border: none;\n"
"border-radus: 9px;\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"border-image: url(:/back/resources/sprites/Offoff.png);\n"
"border: none;\n"
"border-radus: 9px;\n"
"}\n"
"\n"
"\n"
"")
        self.btnoff_2.setText("")
        self.btnoff_2.setObjectName("btnoff_2")
        self.horizontalLayout_3.addWidget(self.btnoff_2)
        self.gridLayout.addLayout(self.horizontalLayout_3, 3, 0, 1, 1)
        settings.setCentralWidget(self.centralwidget)

        self.retranslateUi(settings)
        QtCore.QMetaObject.connectSlotsByName(settings)

    def retranslateUi(self, settings):
        _translate = QtCore.QCoreApplication.translate
        settings.setWindowTitle(_translate("settings", "MainWindow"))
        self.btnmainmenu.setToolTip(_translate("settings", "меню"))


class Ui_level(object):
    def setupUi(self, level):
        QFontDatabase.addApplicationFont(":font/resources/AmaticSC-Bold.ttf")

        level.setObjectName("level")
        level.resize(1440, 1024)
        level.setMinimumSize(QtCore.QSize(1440, 1024))
        font = QtGui.QFont()
        font.setFamily("Amatic SC")
        font.setBold(True)
        font.setWeight(75)
        level.setFont(font)
        level.setToolTip("")
        level.setStyleSheet("QMainWindow{\n"
"border-image: url(:/back/resources/sprites/level.png);\n"
"border-position: center;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(level)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 6, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 2, 0, 1, 1)
        self.box_word_btnconfirmcancel = QtWidgets.QHBoxLayout()
        self.box_word_btnconfirmcancel.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.box_word_btnconfirmcancel.setContentsMargins(-1, 0, -1, 0)
        self.box_word_btnconfirmcancel.setSpacing(0)
        self.box_word_btnconfirmcancel.setObjectName("box_word_btnconfirmcancel")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.box_word_btnconfirmcancel.addItem(spacerItem2)
        self.word = QtWidgets.QLabel(self.centralwidget)
        self.word.setMinimumSize(QtCore.QSize(360, 95))
        self.word.setMaximumSize(QtCore.QSize(360, 95))
        font = QtGui.QFont()
        font.setFamily("Amatic SC")
        font.setPointSize(48)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(9)
        self.word.setFont(font)
        self.word.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.word.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 48pt \"Amatic SC\";")
        self.word.setAlignment(QtCore.Qt.AlignCenter)
        self.word.setObjectName("word")
        self.box_word_btnconfirmcancel.addWidget(self.word)
        self.box_btn_confirm_cancel = QtWidgets.QHBoxLayout()
        self.box_btn_confirm_cancel.setContentsMargins(27, 0, 27, 0)
        self.box_btn_confirm_cancel.setSpacing(34)
        self.box_btn_confirm_cancel.setObjectName("box_btn_confirm_cancel")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.box_btn_confirm_cancel.addItem(spacerItem3)
        self.confirm = QtWidgets.QPushButton(self.centralwidget)
        self.confirm.setMinimumSize(QtCore.QSize(107, 95))
        self.confirm.setMaximumSize(QtCore.QSize(107, 95))
        self.confirm.setStyleSheet("QPushButton{\n"
"background-image: url(:/back/resources/sprites/confirm.png);\n"
"border: none;\n"
"border-radus: 9px;}\n"
"\n"
"QPushButton:hover{\n"
"background-image: url(:/back/resources/sprites/pressconfirm.png);\n"
"border: none;\n"
"border-radus: 9px;\n"
"}\n"
"")
        self.confirm.setText("")
        self.confirm.setObjectName("confirm")
        self.box_btn_confirm_cancel.addWidget(self.confirm)
        self.cancel = QtWidgets.QPushButton(self.centralwidget)
        self.cancel.setMinimumSize(QtCore.QSize(107, 95))
        self.cancel.setMaximumSize(QtCore.QSize(107, 95))
        self.cancel.setToolTipDuration(-1)
        self.cancel.setStyleSheet("QPushButton{\n"
"background-image: url(:/back/resources/sprites/cancel.png);\n"
"border: none;\n"
"border-radus: 9px;}\n"
"\n"
"QPushButton:hover{\n"
"background-image: url(:/back/resources/sprites/presscancel.png);\n"
"border: none;\n"
"border-radus: 9px;\n"
"}\n"
"")
        self.cancel.setText("")
        self.cancel.setObjectName("cancel")
        self.box_btn_confirm_cancel.addWidget(self.cancel)
        self.box_word_btnconfirmcancel.addLayout(self.box_btn_confirm_cancel)
        self.gridLayout.addLayout(self.box_word_btnconfirmcancel, 3, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.box_rightWords = QtWidgets.QGridLayout()
        self.box_rightWords.setContentsMargins(10, 43, -1, -1)
        self.box_rightWords.setObjectName("box_rightWords")
        self.rightWords = QtWidgets.QLabel(self.centralwidget)
        self.rightWords.setMinimumSize(QtCore.QSize(200, 525))
        self.rightWords.setMaximumSize(QtCore.QSize(200, 525))
        font = QtGui.QFont()
        font.setFamily("Amatic SC")
        font.setPointSize(36)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.rightWords.setFont(font)
        self.rightWords.setMouseTracking(False)
        self.rightWords.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 36pt \"Amatic SC\";")
        self.rightWords.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.rightWords.setObjectName("rightWords")
        self.box_rightWords.addWidget(self.rightWords, 1, 0, 2, 1)
        self.rightWords_2 = QtWidgets.QLabel(self.centralwidget)
        self.rightWords_2.setMinimumSize(QtCore.QSize(200, 525))
        self.rightWords_2.setMaximumSize(QtCore.QSize(200, 525))
        font = QtGui.QFont()
        font.setFamily("Amatic SC")
        font.setPointSize(36)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.rightWords_2.setFont(font)
        self.rightWords_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 36pt \"Amatic SC\";")
        self.rightWords_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.rightWords_2.setObjectName("rightWords_2")
        self.box_rightWords.addWidget(self.rightWords_2, 1, 1, 2, 1)
        self.label_rightWords = QtWidgets.QLabel(self.centralwidget)
        self.label_rightWords.setMinimumSize(QtCore.QSize(400, 60))
        self.label_rightWords.setMaximumSize(QtCore.QSize(16777215, 60))
        font = QtGui.QFont()
        font.setFamily("Amatic SC")
        font.setPointSize(36)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_rightWords.setFont(font)
        self.label_rightWords.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 36pt \"Amatic SC\";")
        self.label_rightWords.setObjectName("label_rightWords")
        self.box_rightWords.addWidget(self.label_rightWords, 0, 0, 1, 3)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.box_rightWords.addItem(spacerItem4, 1, 2, 2, 1)
        self.horizontalLayout_3.addLayout(self.box_rightWords)
        self.cat = QtWidgets.QLabel(self.centralwidget)
        self.cat.setMinimumSize(QtCore.QSize(627, 636))
        self.cat.setMaximumSize(QtCore.QSize(627, 636))
        self.cat.setStyleSheet("background-image: url(:/back/resources/sprites/cat-0.png);")
        self.cat.setText("")
        self.cat.setObjectName("cat")
        self.horizontalLayout_3.addWidget(self.cat)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem5)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)
        self.box_btnletter = QtWidgets.QHBoxLayout()
        self.box_btnletter.setContentsMargins(-1, 7, -1, -1)
        self.box_btnletter.setSpacing(34)
        self.box_btnletter.setObjectName("box_btnletter")
        self.gridLayout.addLayout(self.box_btnletter, 5, 0, 1, 1)
        self.box_mainmenu_count = QtWidgets.QHBoxLayout()
        self.box_mainmenu_count.setObjectName("box_mainmenu_count")
        self.btnmainmenu = QtWidgets.QPushButton(self.centralwidget)
        self.btnmainmenu.setMinimumSize(QtCore.QSize(107, 95))
        self.btnmainmenu.setMaximumSize(QtCore.QSize(107, 95))
        self.btnmainmenu.setStyleSheet("QPushButton{\n"
"background-image: url(:/back/resources/sprites/btmainmenu.png);\n"
"border: none;\n"
"border-radus: 9px;}\n"
"\n"
"QPushButton:hover{\n"
"background-image: url(:/back/resources/sprites/pressbtmainmenu.png);\n"
"border: none;\n"
"border-radus: 9px;\n"
"}\n"
"")
        self.btnmainmenu.setText("")
        self.btnmainmenu.setObjectName("btnmainmenu")
        self.box_mainmenu_count.addWidget(self.btnmainmenu)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.box_mainmenu_count.addItem(spacerItem7)
        self.count = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Amatic SC")
        font.setPointSize(40)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.count.setFont(font)
        self.count.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 40pt \"Amatic SC\";")
        self.count.setObjectName("count")
        self.box_mainmenu_count.addWidget(self.count)
        self.gridLayout.addLayout(self.box_mainmenu_count, 0, 0, 1, 1)
        level.setCentralWidget(self.centralwidget)

        self.retranslateUi(level)
        QtCore.QMetaObject.connectSlotsByName(level)

    def retranslateUi(self, level):
        _translate = QtCore.QCoreApplication.translate
        level.setWindowTitle(_translate("level", "MainWindow"))
        self.confirm.setToolTip(_translate("level", "подтверждение"))
        self.cancel.setToolTip(_translate("level", "отмена"))
        self.label_rightWords.setText(_translate("level", "ОТГАДАНО:"))
        self.count.setText(_translate("level", "0/10 СЛОВ"))


class Ui_lose(object):
    def setupUi(self, lose):
        lose.setObjectName("lose")
        lose.resize(1440, 1024)
        lose.setMinimumSize(QtCore.QSize(1440, 1024))
        lose.setStyleSheet("QMainWindow{\n"
"border-image: url(:/back/resources/sprites/goLose.png);\n"
"border-position:center;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(lose)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 300, -1, 0)
        self.horizontalLayout.setSpacing(143)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnreturne = QtWidgets.QPushButton(self.centralwidget)
        self.btnreturne.setMinimumSize(QtCore.QSize(107, 95))
        self.btnreturne.setMaximumSize(QtCore.QSize(107, 95))
        self.btnreturne.setStyleSheet("QPushButton{\n"
"border-image: url(:/back/resources/sprites/repeat.png);\n"
"border: none;\n"
"border-radus: 9px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border-image: url(:/back/resources/sprites/pressrepeat.png);\n"
"border: none;\n"
"border-radus: 9px;\n"
"}\n"
"")
        self.btnreturne.setText("")
        self.btnreturne.setObjectName("btnreturne")
        self.horizontalLayout.addWidget(self.btnreturne)
        self.btnmainmenu = QtWidgets.QPushButton(self.centralwidget)
        self.btnmainmenu.setMinimumSize(QtCore.QSize(107, 95))
        self.btnmainmenu.setMaximumSize(QtCore.QSize(107, 95))
        self.btnmainmenu.setStyleSheet("QPushButton{\n"
"border-image: url(:/back/resources/sprites/btmainmenu.png);\n"
"border: none;\n"
"border-radus: 9px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border-image: url(:/back/resources/sprites/pressbtmainmenu.png);\n"
"border: none;\n"
"border-radus: 9px;\n"
"}\n"
"")
        self.btnmainmenu.setText("")
        self.btnmainmenu.setObjectName("btnmainmenu")
        self.horizontalLayout.addWidget(self.btnmainmenu)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 2, 0, 1, 1)
        lose.setCentralWidget(self.centralwidget)

        self.retranslateUi(lose)
        QtCore.QMetaObject.connectSlotsByName(lose)

    def retranslateUi(self, lose):
        _translate = QtCore.QCoreApplication.translate
        lose.setWindowTitle(_translate("lose", "MainWindow"))
        self.btnmainmenu.setToolTip(_translate("lose", "меню"))
        self.btnreturne.setToolTip(_translate("lose", "повторить"))


class Ui_win(object):
    def setupUi(self, win):
        win.setObjectName("win")
        win.resize(1440, 1024)
        win.setMinimumSize(QtCore.QSize(1440, 1024))
        win.setStyleSheet("QMainWindow{\n"
"border-image: url(:/back/resources/sprites/goWin.png);\n"
"border-position: center;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(win)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 300, -1, -1)
        self.horizontalLayout.setSpacing(143)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnreturn = QtWidgets.QPushButton(self.centralwidget)
        self.btnreturn.setMinimumSize(QtCore.QSize(107, 95))
        self.btnreturn.setMaximumSize(QtCore.QSize(107, 95))
        self.btnreturn.setStyleSheet("QPushButton{\n"
"border-image: url(:/back/resources/sprites/repeat.png);\n"
"border: none;\n"
"border-radus: 9px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border-image: url(:/back/resources/sprites/pressrepeat.png);\n"
"border: none;\n"
"border-radus: 9px;\n"
"}\n"
"")
        self.btnreturn.setText("")
        self.btnreturn.setObjectName("btnreturn")
        self.horizontalLayout.addWidget(self.btnreturn)
        self.btnmainmenu = QtWidgets.QPushButton(self.centralwidget)
        self.btnmainmenu.setMinimumSize(QtCore.QSize(107, 95))
        self.btnmainmenu.setMaximumSize(QtCore.QSize(107, 95))
        self.btnmainmenu.setStyleSheet("QPushButton{\n"
"border-image: url(:/back/resources/sprites/btmainmenu.png);\n"
"border: none;\n"
"border-radus: 9px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border-image: url(:/back/resources/sprites/pressbtmainmenu.png);\n"
"border: none;\n"
"border-radus: 9px;\n"
"}\n"
"")
        self.btnmainmenu.setText("")
        self.btnmainmenu.setObjectName("btnmainmenu")
        self.horizontalLayout.addWidget(self.btnmainmenu)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 2, 0, 1, 1)
        win.setCentralWidget(self.centralwidget)

        self.retranslateUi(win)
        QtCore.QMetaObject.connectSlotsByName(win)

    def retranslateUi(self, win):
        _translate = QtCore.QCoreApplication.translate
        win.setWindowTitle(_translate("win", "MainWindow"))
        self.btnmainmenu.setToolTip(_translate("win", "меню"))
        self.btnreturn.setToolTip(_translate("win", "повторить"))


class MyStyledButton(QtWidgets.QPushButton):
    def __init__(self, btn_letter, letter):
        super(MyStyledButton, self).__init__()
        self.setMinimumSize(QtCore.QSize(107, 95))
        self.setMaximumSize(QtCore.QSize(107, 95))
        self.setStyleSheet("QPushButton{\n"
"background-image: url(:/back/resources/sprites/" + btn_letter + ".png);\n"
"border: none;\n"
"border-radus: 9px;}\n"
"\n"
"QPushButton:hover{\n"
"background-image: url(:/back/resources/sprites/press" + btn_letter + ".png);\n"
"border: none;\n"
"border-radus: 9px;\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"background-image: url(:/back/resources/sprites/disable" + btn_letter + ".png);\n"
"border: none;\n"
"border-radus: 9px;\n"
"}\n"
"")
        self.letter = letter
        self.setObjectName("btnletter")


import background
