import emoji
import XOExceptions


class XOGame:
    SYMBOLS = {1: emoji.emojize(':one:', use_aliases=True),
               2: emoji.emojize(':two:', use_aliases=True),
               3: emoji.emojize(':three:', use_aliases=True),
               4: emoji.emojize(':four:', use_aliases=True),
               5: emoji.emojize(':five:', use_aliases=True),
               6: emoji.emojize(':six:', use_aliases=True),
               7: emoji.emojize(':seven:', use_aliases=True),
               8: emoji.emojize(':eight:', use_aliases=True),
               9: emoji.emojize(':nine:', use_aliases=True),
               0: emoji.emojize(':o:', use_aliases=True),
               -1: emoji.emojize(':x:', use_aliases=True),
               }
    X_FIG = -1
    O_FIG = 0

    def __init__(self):
        self._playground = [[((i * 3) + j) for j in range(1, 4)] for i in range(3)]
        self._player = XOGame.X_FIG

    @staticmethod
    def get_coordinate(n):
        return (n - 1) // 3, (n % 3) - 1

    def put_figure(self, x, y):
        if self._player == 0:
            self._playground[x][y] = XOGame.O_FIG
        else:
            self._playground[x][y] = XOGame.X_FIG

    def show_playground(self):
        for i in range(3):
            print("\t", end="")
            print(*["   " + XOGame.SYMBOLS[self._playground[i][j]] for j in range(3)], sep="\t|",
                  end=" \n" if i == 2 else " \n\t{}\n".format("|".join(["  ----\t", "  ----\t", "  ----\t"])))

    def have_winner(self):
        for i in range(3):
            raw_check = {x for x in self._playground[i]}
            column_check = {x for x in self._playground[:][i]}
            if len(raw_check) == 1:
                return raw_check.pop()
            if len(column_check) == 1:
                return column_check.pop()
        diag_check = {self._playground[j][j] for j in range(3)}
        if len(diag_check) == 1:
            return diag_check.pop()
        diag_check = {self._playground[2 - j][j] for j in range(3)}
        if len(diag_check) == 1:
            return diag_check.pop()
        draw = None
        for i in range(1, 10):
            for c in self._playground:
                if i in c:
                    draw = False
                    break
        return draw

    def validate(self, data):
        try:
            data = int(data)
        except ValueError:
            raise XOExceptions.BadInput("Incorrect input.\nEnter a correct number:")
        if 1 <= data <= 9:
            x, y = XOGame.get_coordinate(data)
            if self._playground[x][y] in (0, -1):
                raise XOExceptions.BadInput("This number of the field is already occupied.\nEnter another one:")
            return x, y
        else:
            raise XOExceptions.BadInput("This number of the field doesn't exist.\nEnter a correct one:")

    def change_turn(self):
        self._player = - ((self._player + 1) % 2)

    def start_game(self):
        print("Let's start playing {x} {o} -game!".format(x=XOGame.SYMBOLS[-1], o=XOGame.SYMBOLS[0]))

        winner = False
        while winner is False:
            self.show_playground()
            print("Enter number of the field to put {} ".format(XOGame.SYMBOLS[self._player]))
            ok = False
            while not ok:
                data = input()
                ok = True
                try:
                    x, y = self.validate(data)
                except XOExceptions.BadInput as ex:
                    ok = False
                    print(ex)
            self.put_figure(x, y)
            self.change_turn()
            winner = self.have_winner()

        self.show_playground()
        if winner is None:
            print("It draw guys, try again")
        else:
            print("{player}!!!We have WINNER!!! {player}".format(player=(XOGame.SYMBOLS[winner] + " ") * 3))
