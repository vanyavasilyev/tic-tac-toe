from random import choice


class TicTacToe:
    def __init__(self, name1, name2):
        self.name1 = name1
        self.name2 = name2
        self.field = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
        self.first_player = choice([name1, name2])
        self.active_player = self.first_player
        self.symbol1 = choice(['0', '+'])
        self.symbol2 = '0' if self.symbol1 == '+' else '+'
        self.first_symbol = self.symbol1 if self.first_player == self.name1 else self.symbol2
        self.WINNING_LINES = [{(0, 0), (0, 1), (0, 2)}, {(1, 0), (1, 1), (1, 2)}, {(2, 0), (2, 1), (2, 2)},
                              {(0, 0), (1, 0), (2, 0)}, {(0, 1), (1, 1), (2, 1)}, {(0, 2), (1, 2), (2, 2)},
                              {(0, 0), (1, 1), (2, 2)}, {(2, 0), (1, 1), (0, 2)}]
        print(self.first_player + ' goes first with ' + self.first_symbol)

    def print_field(self):
        print('\n'.join((' '.join(line)) for line in self.field))

    def print_active_player(self):
        print(self.active_player)

    def move(self, symbol, line, column):
        self.field[int(line) - 1][int(column) - 1] = symbol
        self.active_player = self.name1 if self.active_player == self.name2 else self.name2

    def winner(self):
        for winning_line in self.WINNING_LINES:
            if not sum(self.symbol1 != self.field[line][column] for line, column in winning_line):
                return self.name1
        for winning_line in self.WINNING_LINES:
            if not sum(self.symbol2 != self.field[line][column] for line, column in winning_line):
                return self.name2
        return 'Nobody'

    def check_game_if_finished(self):
        if self.winner() == 'Nobody':
            return 'No!'
        else:
            return 'Yes!'


if __name__ == '__main__':
    action = ''
    game = TicTacToe('anon1', 'anon2')
    while action != 'finish':
        action = input()

        if action == 'new_game':
            name1, name2 = input().split(' ')
            game = TicTacToe(name1, name2)

        if action == 'move':
            symbol, line, column = input().split(' ')
            game.move(symbol, line, column)

        if action == 'print_field':
            game.print_field()

        if action == 'print_winner':
            print(game.winner())

        if action == 'print_active_player':
            print(game.active_player)

        if action == 'print_is_the_game_over':
            print(game.check_game_if_finished())
