import random

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent, QMediaPlaylist
from PyQt5.QtWidgets import QDesktopWidget
from GUI import Ui_mainmenu, Ui_exit, Ui_lose, Ui_win, Ui_settings, Ui_rule, Ui_level, MyStyledButton


class Mainmenu(QtWidgets.QMainWindow):
    def __init__(self):
        super(Mainmenu, self).__init__()
        self.ui_window = Ui_mainmenu()
        self.ui_window.setupUi(self)

        self.ui_window.play.clicked.connect(self.play)
        self.ui_window.settings.clicked.connect(self.settings)
        self.ui_window.rules.clicked.connect(self.rules)
        self.ui_window.exit.clicked.connect(self.exit)

    @staticmethod
    def play():
        if sound_play:
            sound_player.play()
        global number_level
        number_level = random.randint(1, 5)
        level_screen.generate()
        widget.setCurrentIndex(widget.currentIndex() + 6)

    @staticmethod
    def settings():
        if sound_play:
            sound_player.play()
        widget.setCurrentIndex(widget.currentIndex() + 1)

    @staticmethod
    def rules():
        if sound_play:
            sound_player.play()
        widget.setCurrentIndex(widget.currentIndex() + 2)

    @staticmethod
    def exit():
        if sound_play:
            sound_player.play()
        widget.setCurrentIndex(widget.currentIndex() + 3)


class Settings(QtWidgets.QMainWindow):
    def __init__(self):
        super(Settings, self).__init__()
        self.ui_settings = Ui_settings()
        self.ui_settings.setupUi(self)

        self.ui_settings.btnoff.clicked.connect(self.music_off)
        self.ui_settings.btnon.clicked.connect(self.music_on)
        self.ui_settings.btnon.setEnabled(False)

        self.ui_settings.btnoff_2.clicked.connect(self.sound_off)
        self.ui_settings.btnon_2.clicked.connect(self.sound_on)
        self.ui_settings.btnon_2.setEnabled(False)

        self.ui_settings.btnmainmenu.clicked.connect(self.mainmenu)

    @staticmethod
    def mainmenu():
        if sound_play:
            sound_player.play()
        widget.setCurrentIndex(widget.currentIndex() - 1)

    def music_off(self):
        if sound_play:
            sound_player.play()
        media_player.stop()
        self.ui_settings.btnoff.setEnabled(False)
        self.ui_settings.btnon.setEnabled(True)

    def music_on(self):
        if sound_play:
            sound_player.play()
        media_player.play()
        self.ui_settings.btnon.setEnabled(False)
        self.ui_settings.btnoff.setEnabled(True)

    def sound_off(self):
        global sound_play
        if sound_play:
            sound_player.play()
        sound_play = False
        self.ui_settings.btnoff_2.setEnabled(False)
        self.ui_settings.btnon_2.setEnabled(True)

    def sound_on(self):
        global sound_play
        sound_play = True
        self.ui_settings.btnon_2.setEnabled(False)
        self.ui_settings.btnoff_2.setEnabled(True)


class Rules(QtWidgets.QMainWindow):
    def __init__(self):
        super(Rules, self).__init__()
        self.ui_rule = Ui_rule()
        self.ui_rule.setupUi(self)

        self.ui_rule.btnright.clicked.connect(self.right)
        self.ui_rule.btnleft.clicked.connect(self.left)
        self.ui_rule.btnleft.setEnabled(False)
        self.ui_rule.btnmainmenu.clicked.connect(self.mainmenu)

        self.page = 1

    def right(self):
        if sound_play:
            sound_player.play()

        if self.page != 3:
            self.page += 1
        self.setStyleSheet("QMainWindow{\n"
                           "border-image: url(:/back/resources/sprites/rules-" + str(self.page) + ".png);\n"
                           "border-position: center;\n"
                           "}")

        if self.page > 1:
            self.ui_rule.btnleft.setEnabled(True)
        if self.page == 3:
            self.ui_rule.btnright.setEnabled(False)

    def left(self):
        if sound_play:
            sound_player.play()

        if self.page != 1:
            self.page -= 1
        self.setStyleSheet("QMainWindow{\n"
                           "border-image: url(:/back/resources/sprites/rules-" + str(self.page) + ".png);\n"
                           "border-position: center;\n"
                           "}")

        if self.page < 3:
            self.ui_rule.btnright.setEnabled(True)
        if self.page == 1:
            self.ui_rule.btnleft.setEnabled(False)

    def mainmenu(self):
        if sound_play:
            sound_player.play()
        widget.setCurrentIndex(widget.currentIndex() - 2)
        self.ui_rule.btnleft.setEnabled(False)
        self.ui_rule.btnright.setEnabled(True)
        self.page = 1
        self.setStyleSheet("QMainWindow{\n"
                           "border-image: url(:/back/resources/sprites/rules-1.png);\n"
                           "border-position: center;\n"
                           "}")


class Exit(QtWidgets.QMainWindow):
    def __init__(self):
        super(Exit, self).__init__()
        self.ui_exit = Ui_exit()
        self.ui_exit.setupUi(self)

        self.ui_exit.yes.clicked.connect(self.yes)
        self.ui_exit.no.clicked.connect(self.no)

    @staticmethod
    def yes():
        quit()

    @staticmethod
    def no():
        if sound_play:
            sound_player.play()
        widget.setCurrentIndex(widget.currentIndex() - 3)


class Level(QtWidgets.QMainWindow):
    def __init__(self):
        super(Level, self).__init__()
        self.ui_level = Ui_level()
        self.ui_level.setupUi(self)

        self.guessed = []
        self.double_right = 0
        self.mistake = 0
        self.count_guessed = 0
        self.max_in_column = 0
        self.spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)

        self.ui_level.btnmainmenu.clicked.connect(self.mainmenu)
        self.ui_level.cancel.clicked.connect(self.cancel)
        self.ui_level.confirm.clicked.connect(self.confirm)

    def generate(self):
        match number_level:
            case 1: self.marker()
            case 2: self.pillow()
            case 3: self.mokasin()
            case 4: self.spiral()
            case 5: self.operetta()

    def marker(self):
        self.filling_dictionary("Фломастер")
        self.maxrightWords = 12

        self.ui_level.count.setText("0/12 СЛОВ")
        button_f = MyStyledButton("f", "Ф")
        button_l = MyStyledButton("l", "Л")
        button_o = MyStyledButton("o", "О")
        button_m = MyStyledButton("m", "М")
        button_a = MyStyledButton("a", "А")
        button_s = MyStyledButton("s", "С")
        button_t = MyStyledButton("t", "Т")
        button_e = MyStyledButton("e", "Е")
        button_r = MyStyledButton("r", "Р")

        self.ui_level.box_btnletter.addItem(self.spacerItem1)
        self.ui_level.box_btnletter.addWidget(button_f)
        self.ui_level.box_btnletter.addWidget(button_l)
        self.ui_level.box_btnletter.addWidget(button_o)
        self.ui_level.box_btnletter.addWidget(button_m)
        self.ui_level.box_btnletter.addWidget(button_a)
        self.ui_level.box_btnletter.addWidget(button_s)
        self.ui_level.box_btnletter.addWidget(button_t)
        self.ui_level.box_btnletter.addWidget(button_e)
        self.ui_level.box_btnletter.addWidget(button_r)
        self.ui_level.box_btnletter.addItem(self.spacerItem2)

        button_f.clicked.connect(self.letter_in_layout)
        button_l.clicked.connect(self.letter_in_layout)
        button_o.clicked.connect(self.letter_in_layout)
        button_m.clicked.connect(self.letter_in_layout)
        button_a.clicked.connect(self.letter_in_layout)
        button_s.clicked.connect(self.letter_in_layout)
        button_t.clicked.connect(self.letter_in_layout)
        button_e.clicked.connect(self.letter_in_layout)
        button_r.clicked.connect(self.letter_in_layout)

    def pillow(self):
        self.filling_dictionary("Подушка")
        self.maxrightWords = 11

        self.ui_level.count.setText("0/11 СЛОВ")
        button_p = MyStyledButton("p", "П")
        button_o = MyStyledButton("o", "О")
        button_d = MyStyledButton("d", "Д")
        button_y = MyStyledButton("y", "У")
        button_sh = MyStyledButton("sh", "Ш")
        button_k = MyStyledButton("k", "К")
        button_a = MyStyledButton("a", "А")

        self.ui_level.box_btnletter.addItem(self.spacerItem1)
        self.ui_level.box_btnletter.addWidget(button_p)
        self.ui_level.box_btnletter.addWidget(button_o)
        self.ui_level.box_btnletter.addWidget(button_d)
        self.ui_level.box_btnletter.addWidget(button_y)
        self.ui_level.box_btnletter.addWidget(button_sh)
        self.ui_level.box_btnletter.addWidget(button_k)
        self.ui_level.box_btnletter.addWidget(button_a)
        self.ui_level.box_btnletter.addItem(self.spacerItem2)

        button_p.clicked.connect(self.letter_in_layout)
        button_o.clicked.connect(self.letter_in_layout)
        button_d.clicked.connect(self.letter_in_layout)
        button_y.clicked.connect(self.letter_in_layout)
        button_sh.clicked.connect(self.letter_in_layout)
        button_k.clicked.connect(self.letter_in_layout)
        button_a.clicked.connect(self.letter_in_layout)

    def mokasin(self):
        self.filling_dictionary("Мокасин")
        self.maxrightWords = 11

        self.ui_level.count.setText("0/11 СЛОВ")
        button_m = MyStyledButton("m", "М")
        button_o = MyStyledButton("o", "О")
        button_k = MyStyledButton("k", "К")
        button_a = MyStyledButton("a", "А")
        button_s = MyStyledButton("s", "С")
        button_i = MyStyledButton("i", "И")
        button_n = MyStyledButton("n", "Н")

        self.ui_level.box_btnletter.addItem(self.spacerItem1)
        self.ui_level.box_btnletter.addWidget(button_m)
        self.ui_level.box_btnletter.addWidget(button_o)
        self.ui_level.box_btnletter.addWidget(button_k)
        self.ui_level.box_btnletter.addWidget(button_a)
        self.ui_level.box_btnletter.addWidget(button_s)
        self.ui_level.box_btnletter.addWidget(button_i)
        self.ui_level.box_btnletter.addWidget(button_n)

        self.ui_level.box_btnletter.addItem(self.spacerItem2)

        button_m.clicked.connect(self.letter_in_layout)
        button_o.clicked.connect(self.letter_in_layout)
        button_k.clicked.connect(self.letter_in_layout)
        button_a.clicked.connect(self.letter_in_layout)
        button_s.clicked.connect(self.letter_in_layout)
        button_i.clicked.connect(self.letter_in_layout)
        button_n.clicked.connect(self.letter_in_layout)

    def spiral(self):
        self.filling_dictionary("Спираль")
        self.maxrightWords = 10

        self.ui_level.count.setText("0/10 СЛОВ")
        button_s = MyStyledButton("s", "С")
        button_p = MyStyledButton("p", "П")
        button_i = MyStyledButton("i", "И")
        button_r = MyStyledButton("r", "Р")
        button_a = MyStyledButton("a", "А")
        button_l = MyStyledButton("l", "Л")
        button_soft = MyStyledButton("soft", "Ь")

        self.ui_level.box_btnletter.addItem(self.spacerItem1)
        self.ui_level.box_btnletter.addWidget(button_s)
        self.ui_level.box_btnletter.addWidget(button_p)
        self.ui_level.box_btnletter.addWidget(button_i)
        self.ui_level.box_btnletter.addWidget(button_r)
        self.ui_level.box_btnletter.addWidget(button_a)
        self.ui_level.box_btnletter.addWidget(button_l)
        self.ui_level.box_btnletter.addWidget(button_soft)

        self.ui_level.box_btnletter.addItem(self.spacerItem2)

        button_s.clicked.connect(self.letter_in_layout)
        button_p.clicked.connect(self.letter_in_layout)
        button_i.clicked.connect(self.letter_in_layout)
        button_r.clicked.connect(self.letter_in_layout)
        button_a.clicked.connect(self.letter_in_layout)
        button_l.clicked.connect(self.letter_in_layout)
        button_soft.clicked.connect(self.letter_in_layout)

    def operetta(self):
        self.filling_dictionary("Оперетта")
        self.maxrightWords = 10

        self.ui_level.count.setText("0/10 СЛОВ")
        button_o = MyStyledButton("o", "О")
        button_p = MyStyledButton("p", "П")
        button_e_1 = MyStyledButton("e", "Е")
        button_r = MyStyledButton("r", "Р")
        button_e_2 = MyStyledButton("e", "Е")
        button_t_1 = MyStyledButton("t", "Т")
        button_t_2 = MyStyledButton("t", "Т")
        button_a = MyStyledButton("a", "А")

        self.ui_level.box_btnletter.addItem(self.spacerItem1)
        self.ui_level.box_btnletter.addWidget(button_o)
        self.ui_level.box_btnletter.addWidget(button_p)
        self.ui_level.box_btnletter.addWidget(button_e_1)
        self.ui_level.box_btnletter.addWidget(button_r)
        self.ui_level.box_btnletter.addWidget(button_e_2)
        self.ui_level.box_btnletter.addWidget(button_t_1)
        self.ui_level.box_btnletter.addWidget(button_t_2)
        self.ui_level.box_btnletter.addWidget(button_a)

        self.ui_level.box_btnletter.addItem(self.spacerItem2)

        button_o.clicked.connect(self.letter_in_layout)
        button_p.clicked.connect(self.letter_in_layout)
        button_e_1.clicked.connect(self.letter_in_layout)
        button_r.clicked.connect(self.letter_in_layout)
        button_e_2.clicked.connect(self.letter_in_layout)
        button_t_1.clicked.connect(self.letter_in_layout)
        button_t_2.clicked.connect(self.letter_in_layout)
        button_a.clicked.connect(self.letter_in_layout)

    def mainmenu(self):
        if sound_play:
            sound_player.play()
        widget.setCurrentIndex(widget.currentIndex() - 6)
        self.clear_screen()

    def cancel(self):
        if sound_play:
            sound_player.play()
        self.ui_level.word.setText("")
        self.set_buttons_enabled()

    def confirm(self):
        if sound_play:
            sound_player.play()

        enter_word = self.ui_level.word.text().lower()

        if enter_word in self.words_dictionary and enter_word != "" and enter_word not in self.guessed:
            self.guessed.append(enter_word)
            if self.mistake > 0:
                self.double_right += 1
            self.count_guessed += 1
            self.ui_level.count.setText(str(self.count_guessed) + "/" + str(self.maxrightWords) + " СЛОВ")

            if self.count_guessed == self.maxrightWords:
                widget.setCurrentIndex(widget.currentIndex() - 1)
                self.clear_screen()

            elif self.max_in_column != 6:
                self.ui_level.rightWords.setText(self.ui_level.rightWords.text() + enter_word.upper() + "\n")
                self.max_in_column += 1

            else:
                self.ui_level.rightWords_2.setText(
                    self.ui_level.rightWords_2.text() + enter_word.upper() + "\n")

            if self.double_right == 2:
                self.double_right = 0
                self.mistake -= 1
                self.ui_level.cat.setStyleSheet(
                    "background-image: url(:/back/resources/sprites/cat-" + str(self.mistake) + ".png);")

        elif (self.ui_level.word.text() not in self.words_dictionary and self.ui_level.word.text() != "" and
              enter_word not in self.guessed):
            if self.mistake < 5:
                self.double_right = 0
                self.mistake += 1
                self.ui_level.cat.setStyleSheet(
                    "background-image: url(:/back/resources/sprites/cat-" + str(self.mistake) + ".png);")
            else:
                widget.setCurrentIndex(widget.currentIndex() - 2)
                self.clear_screen()

        self.ui_level.word.setText("")
        self.set_buttons_enabled()

    def filling_dictionary(self, word):
        dictionary = open("resources/Dictionary.txt", "r", encoding="utf-8")
        while True:
            self.words_dictionary = dictionary.readline()
            self.words_dictionary = self.words_dictionary.split()
            if word in self.words_dictionary:
                break
            if not self.words_dictionary:
                self.words_dictionary = []
                break
        dictionary.close()

    def letter_in_layout(self):
        if sound_play:
            sound_player.play()
        sender = self.sender()
        sender.setEnabled(False)

        self.ui_level.word.setText(self.ui_level.word.text() + sender.letter)

    def set_buttons_enabled(self):
        for i in range(self.ui_level.box_btnletter.count()):
            child = self.ui_level.box_btnletter.itemAt(i)
            if child.widget():
                child.widget().setEnabled(True)

    def clear_layout(self):
        while self.ui_level.box_btnletter.count():
            child = self.ui_level.box_btnletter.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

    def clear_screen(self):
        self.clear_layout()
        self.words_dictionary = []
        self.guessed = []
        self.count_guessed = 0
        self.double_right = 0
        self.mistake = 0
        self.max_in_column = 0
        self.ui_level.cat.setStyleSheet(
            "background-image: url(:/back/resources/sprites/cat-0.png);")
        self.ui_level.rightWords.setText("")
        self.ui_level.rightWords_2.setText("")
        self.ui_level.word.setText("")


class Lose(QtWidgets.QMainWindow):
    def __init__(self):
        super(Lose, self).__init__()
        self.ui_lose = Ui_lose()
        self.ui_lose.setupUi(self)

        self.ui_lose.btnmainmenu.clicked.connect(self.mainmenu)
        self.ui_lose.btnreturne.clicked.connect(self.returne)

    @staticmethod
    def mainmenu():
        if sound_play:
            sound_player.play()
        widget.setCurrentIndex(widget.currentIndex() - 4)


    @staticmethod
    def returne():
        if sound_play:
            sound_player.play()
        level_screen.generate()
        widget.setCurrentIndex(widget.currentIndex() + 2)


class Win(QtWidgets.QMainWindow):
    def __init__(self):
        super(Win, self).__init__()
        self.ui_win = Ui_win()
        self.ui_win.setupUi(self)

        self.ui_win.btnmainmenu.clicked.connect(self.mainmenu)
        self.ui_win.btnreturn.clicked.connect(self.returne)

    @staticmethod
    def mainmenu():
        if sound_play:
            sound_player.play()
        widget.setCurrentIndex(widget.currentIndex() - 5)

    @staticmethod
    def returne():
        if sound_play:
            sound_player.play()
        level_screen.generate()
        widget.setCurrentIndex(widget.currentIndex() + 1)


def center_widget():
    desktop = QDesktopWidget().screenGeometry()
    x = (desktop.width() - widget.width()) // 2
    y = (desktop.height() - widget.height()) // 2 - 30
    widget.move(x, y)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    widget = QtWidgets.QStackedWidget()

    number_level = 0
    sound_play = True

    sound_player = QMediaPlayer()
    sound_player.setMedia(QMediaContent(QtCore.QUrl.fromLocalFile("resources\\audio\\click.mp3")))

    media_player = QMediaPlayer()
    background_music = QMediaPlaylist()
    background_music.addMedia(QMediaContent(QtCore.QUrl.fromLocalFile("resources\\audio\\Colorful Cat - Rurikon.mp3")))
    background_music.setPlaybackMode(QMediaPlaylist.Loop)
    media_player.setPlaylist(background_music)
    media_player.play()

    mainmenu_screen = Mainmenu()
    settings_screen = Settings()
    rules_screen = Rules()
    exit_screen = Exit()
    lose_screen = Lose()
    win_screen = Win()
    level_screen = Level()

    widget.addWidget(mainmenu_screen)   # 0
    widget.addWidget(settings_screen)   # 1
    widget.addWidget(rules_screen)     # 2
    widget.addWidget(exit_screen)   # 3
    widget.addWidget(lose_screen)   # 4
    widget.addWidget(win_screen)    # 5
    widget.addWidget(level_screen)  #6


    widget.show()
    center_widget()
    app.exec()
