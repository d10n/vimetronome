import textwrap

from colored import fg, bg, attr


class Metronome(object):
    def __init__(self):
        self.tock = False
        self.art = '   \n   \n   '.splitlines()

    def tick(self):
        if self.tock:
            lines = f'{attr("reset")}\n{fg("black")}{bg("black")}'.join(self.art)
            print(f'{fg("black")}{bg("black")}{lines}{attr("reset")}\x1b[{len(self.art)-1}F', end='')
            # print(f'\r[s{fg("black")}{bg("black")}__{attr("reset")}', end='')
        else:
            lines = f'{attr("reset")}\n{fg("white")}{bg("white")}'.join(self.art)
            print(f'{fg("white")}{bg("white")}{lines}{attr("reset")}\x1b[{len(self.art)-1}F', end='')
            # print(f'\r[s{fg("white")}{bg("white")}__{attr("reset")}', end='')
        self.tock = not self.tock
