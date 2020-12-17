from collections import deque
import curses
from curses.textpad import Textbox, rectangle
from itertools import cycle
import re
import time
from Constants import *

INDEX_ACC_WINDOW_WIDTH = 27
OP_WINDOW_WIDTH = 11
VISITED_WINDOW_WIDTH = 5
CELL = '00000'
MN_WIN_COL = 100
ADD_WIN_COL = 101
ACC_WIN_COL = 102
VIS_WIN_COL = 103
UNKNOWN_NUM = 104
PARAM = 105
OP_COLOR = 106
OP_HIGHLIGHT = 107
DELAY = .05


def delayed(iter, delay=DELAY):
    for item in iter:
        yield item
        time.sleep(delay)


class Display:
    def __init__(self):
        self.chars = {}
        return
        # self.computer = computer
        # self.init_scr()
        # self.setup_windows()
        # self.display("Booting int code computer, please wait")
        # self.draw_data_window()/
        # self.run()
        # self.end_curses()

    def boot(self, int_code):
        self.init_scr()
        self.setup_windows()
        self.display("Booting int code computer, please wait")
        self.draw_data_window(int_code)

    def init_scr(self):
        self.screen = curses.initscr()
        self.screen.clear()
        self.screen.keypad(True)
        curses.cbreak()
        curses.noecho()
        curses.curs_set(0)
        curses.start_color()
        curses.init_pair(MN_WIN_COL, curses.COLOR_GREEN, curses.COLOR_BLACK)
        curses.init_pair(ACC_WIN_COL, curses.COLOR_BLACK, curses.COLOR_CYAN)
        curses.init_pair(ADD_WIN_COL, curses.COLOR_BLACK, curses.COLOR_YELLOW)
        curses.init_pair(VIS_WIN_COL, curses.COLOR_YELLOW, curses.COLOR_BLACK)
        curses.init_pair(OP_COLOR, curses.COLOR_CYAN, curses.COLOR_BLACK)
        curses.init_pair(OP_HIGHLIGHT, curses.COLOR_YELLOW, curses.COLOR_BLACK)
        curses.init_pair(PARAM, curses.COLOR_GREEN, curses.COLOR_BLACK)
        curses.init_pair(UNKNOWN_NUM, curses.COLOR_WHITE, curses.COLOR_BLACK)
        curses.init_pair(99, curses.COLOR_RED, curses.COLOR_BLACK)
        self.screen.attron(curses.color_pair(MN_WIN_COL))

    def setup_windows(self):

        screen = self.screen
        height, width = self.screen.getmaxyx()

        # Title
        rectangle(screen, 0, 0, 2, width - 2)
        self.title_win = curses.newwin(1, width - 4, 1, 2)

        # Data Vis
        rectangle(screen, 3, 0, height - 4, width - 2)
        self.vis_win = curses.newwin(height - 8, width - 4, 4, 2)
        self.vis_win.attron(curses.color_pair(1))

        # Input
        rectangle(screen, height - 3,  0, height - 1, width - 2)
        self.input_win = curses.newwin(1, width - 4, height - 2, 2)
        self.text_in = Textbox(self.input_win)

        self.screen.refresh()
        curses.doupdate()

    def draw_data_window(self, int_code):
        # Draw cell for each instruction in data
        _, w = self.vis_win.getmaxyx()
        cell_per_row = w // len(CELL)
        for i, op in enumerate(int_code):
            row, col = divmod(i, cell_per_row)
            char = str(op).center(5)
            self.chars[i] = (row, col)
            self.vis_win.addstr(row, col * len(CELL), char,
                                curses.color_pair(UNKNOWN_NUM))
            self.vis_win.refresh()
            time.sleep(.003)

    def end_curses(self):
        curses.nocbreak()
        self.screen.keypad(False)
        curses.echo()
        curses.flushinp()
        curses.endwin()

    def run(self):
        time.sleep(1)
        self.display(
            'Beginning run of boot code. Any key to continue...')
        self.input_win.getch()
        self.computer.run()
        self.network_win.getch()

    def highlight(self, i):
        row, col = self.chars[i]
        curses.echo()
        self.vis_win.chgat(row, col, curses.color_pair(OP_HIGHLIGHT))
        # row, col = divmod(indx, cell_per_row)
        # self.vis_win.chgat(row, col * len(CELL) + 1, 1, OP_HIGHLIGHT)
        curses.noecho()

        # old_index = 0
        # while True:
        #     index = yield

        #     row, col = divmod(old_index, cell_per_row)
        #     self.vis_win.chgat(row, col * len(CELL) + 1, 1,
        #                     OP_COLOR[DATA[old_index][0]])

        #     row, col = divmod(index, cell_per_row)
        #     self.vis_win.chgat(row, col * len(CELL) + 1, 1,
        #                     OP_HIGHLIGHT[DATA[index][0]])

        #     old_index = index
        #     self.vis_win.noutrefresh()

    def display(self, out, with_dots=False):
        self.title_win.erase()
        for col, char in enumerate(out):
            self.title_win.addstr(0, col, char)
            self.title_win.refresh()
            time.sleep(.01)
        if with_dots:
            now = time.time()
            while time.time() - now < 3:
                self.dots(self.title_win, 0, len(out))
                # for i in range(5):
                #     self.dots(self.network_win, self.top + 3,
                #               self.left + 12 + 20 * i, 2, curses.A_BOLD)
            # return self.dots(len(out))

    def dots(self, win, row, column, n=3, attributes=None):
        dots = n - round(2 * time.time()) % (n + 1)
        dot_str = '.' * n + ' ' * n
        if attributes is None:
            win.addstr(row, column, dot_str[dots:dots + n])
        else:
            win.addstr(row, column, dot_str[dots:dots + n], attributes)
        win.refresh()

    def ask(self, question):
        self.display(question)
        self.input_win.refresh()
        curses.curs_set(1)
        self.text_in.edit()
        answer = self.text_in.gather()
        curses.curs_set(0)
        self.input_win.erase()
        self.input_win.refresh()
        return answer


# if __name__ == "__main__":
#     computer = Computer(fileinput.input())
#     Display(computer)
