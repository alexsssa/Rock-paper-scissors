import sys
import time
import config

from PyQt5 import uic
from random import choice
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QApplication


class StartGame(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('start_window.ui', self)
        self.setWindowIcon(QIcon('icon.png'))
        self.setWindowTitle('Камень-ножницы-бумага [by drammma] - 2022')

        self.button_done.clicked.connect(self.click_button)

    def click_button(self):
        config.level = self.spinBox.value()
        config.rounds = self.spinBox_2.value()
        self.second_class = HelpClass()
        self.second_class.show()
        self.hide()


class HelpClass(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('help_window.ui', self)
        self.setWindowIcon(QIcon('icon.png'))
        self.setWindowTitle('Камень-ножницы-бумага [by drammma] - 2022')

        self.button_done.clicked.connect(self.click_button)

    def click_button(self):
        self.third_class = GameClass()
        self.third_class.show()
        self.hide()


class GameClass(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('design.ui', self)
        self.setWindowIcon(QIcon('icon.png'))
        self.setWindowTitle('Камень-ножницы-бумага [by drammma] - 2022')

        self.button_stone.clicked.connect(self.run_game)
        self.button_scissors.clicked.connect(self.run_game)
        self.button_papers.clicked.connect(self.run_game)
        self.button_well.clicked.connect(self.run_game)
        self.button_lizard.clicked.connect(self.run_game)
        self.button_spock.clicked.connect(self.run_game)

        self.user_score.display(0)
        self.computer_score.display(0)

        if config.level == 1:
            self.button_well.hide()
            self.button_lizard.hide()
            self.button_spock.hide()
        if config.level == 2:
            self.button_lizard.hide()
            self.button_spock.hide()

        self.count = 1

    def run_game(self):
        if self.count < config.rounds:
            self.user = self.user_click()
            self.computer = self.computer_click()
            self.text = 'Раунд: '
            self.design_label4_2.setText(f'{self.text}{self.count}/{config.rounds}')
            self.move_comparison(self.user, self.computer)
            self.count += 1
        else:
            time.sleep(0.5)
            self.update_player_win()
            self.win_window = DialogWindowClass()
            self.win_window.show()
            self.hide()

    def user_click(self):
        self.user_change.setText(self.sender().text())
        return self.sender().text()

    def computer_click(self):
        self.options = config.options[config.level]
        self.computer_choice = choice(self.options)
        self.computer_change.setText(self.computer_choice)
        return self.computer_choice

    def move_comparison(self, user, computer):
        if f'{user}-{computer}' in config.wins_word:
            self.win = 1
            self.design_label_tablo.setText(config.wins_word[f'{user}-{computer}'])
        else:
            if f'{user}-{computer}' in config.lose_word:
                self.win = 2
                self.design_label_tablo.setText(config.lose_word[f'{user}-{computer}'])
            else:
                self.win = 0
                self.design_label_tablo.setText('Ничья')
        self.score_update(self.win)

    def score_update(self, win):
        if self.win == 1:
            self.user_score.display(int(self.user_score.value() + 1))
        elif self.win == 0:
            pass
        else:
            self.computer_score.display(int(self.computer_score.value() + 1))

    def update_player_win(self):
        if self.user_score.value() > self.computer_score.value():
            config.win_player = 'Пользователь!'
        elif self.user_score.value() == self.computer_score.value():
            config.win_player = 'каждый из игроков!'
        else:
            config.win_player = 'Компьютер!!!!!!!!!'


class DialogWindowClass(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('dialog_window.ui', self)
        self.setWindowIcon(QIcon('icon.png'))
        self.setWindowTitle('Камень-ножницы-бумага [by drammma] - 2022')

        self.win_label.setText(f'Победил {config.win_player}')
        self.update()

        self.button_done.clicked.connect(self.button_click)
        self.button_done_2.clicked.connect(self.button_click)

    def button_click(self):
        if self.sender().text() == 'Выход':
            quit()
        else:
            self.class_ = StartGame()
            self.class_.show()
            self.hide()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    class_ = StartGame()
    class_.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
