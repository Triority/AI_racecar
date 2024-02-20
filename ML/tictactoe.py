import numpy as np


class Chessboard:
    def __init__(self, size):
        """
        初始化棋盘，空位为0，先手落子为1，后手-1
        """
        self.size = size
        self.state = np.zeros((size, size))
        self.last_state = self.state.copy
        self.winner = []

    def action(self, player, position):
        self.last_state = self.state.copy
        self.state[position] = player
        # 棋盘占满和棋
        if len(np.where(self.state == 0)[0]) == 0:
            self.winner = [0]
        # 判断是否赢棋
        if 3 in self.state.sum(1) or 3 in self.state.sum(0):
            self.winner = [1]
        if -3 in self.state.sum(1) or -3 in self.state.sum(0):
            self.winner = [-1]
        if self.state[0, 0] + self.state[1, 1] + self.state[2, 2] == 3:
            self.winner = [1]
        if self.state[0, 2] + self.state[1, 1] + self.state[2, 0] == -3:
            self.winner = [-1]

    def restart(self):
        self.state = np.zeros((self.size, self.size))
        self.last_state = self.state.copy
        self.winner = []


class Player:
    def __init__(self):
        pass
