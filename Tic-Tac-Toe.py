import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QLabel, QMessageBox
from PyQt5.QtCore import Qt

class TicTacToe(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Tic-Tac-Toe')
        self.setGeometry(100, 100, 300, 300)

        self.current_player = 'X'
        self.board = [' '] * 9

        self.buttons = [QPushButton('') for _ in range(9)]
        for i, button in enumerate(self.buttons):
            button.setFixedSize(90, 90)
            button.clicked.connect(lambda _, index=i: self.on_button_click(index))

        layout = QGridLayout(self)
        for i in range(3):
            for j in range(3):
                layout.addWidget(self.buttons[i * 3 + j], i, j)

        self.status_label = QLabel('Player {}\'s turn'.format(self.current_player))
        layout.addWidget(self.status_label, 3, 0, 1, 3)
        layout.setAlignment(self.status_label, Qt.AlignCenter)

        self.show()

    def on_button_click(self, index):
        if self.board[index] == ' ':
            self.board[index] = self.current_player
            self.buttons[index].setText(self.current_player)

            if self.check_winner():
                self.show_winner_message()
                self.reset_board()
            elif ' ' not in self.board:
                self.show_draw_message()
                self.reset_board()
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'
                self.status_label.setText('Player {}\'s turn'.format(self.current_player))

    def check_winner(self):
        for i in range(0, 3):
            if (self.board[i] == self.board[i + 3] == self.board[i + 6] != ' ') or \
               (self.board[i * 3] == self.board[i * 3 + 1] == self.board[i * 3 + 2] != ' '):
                return True
        if (self.board[0] == self.board[4] == self.board[8] != ' ') or \
           (self.board[2] == self.board[4] == self.board[6] != ' '):
            return True
        return False

    def show_winner_message(self):
        winner = 'X' if self.current_player == 'X' else 'O'
        QMessageBox.information(self, 'Game Over', 'Player {} wins!'.format(winner))

    def show_draw_message(self):
        QMessageBox.information(self, 'Game Over', 'It\'s a draw!')

    def reset_board(self):
        self.current_player = 'X'
        self.board = [' '] * 9

        for button in self.buttons:
            button.setText('')

        self.status_label.setText('Player {}\'s turn'.format(self.current_player))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    game = TicTacToe()
    sys.exit(app.exec_())