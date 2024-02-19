import time
import hashlib
import numpy
import random


class ooxx_machine():
    def __init__(self):
        self.race = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        # 用于表示棋盘 0代表没下过 1 A玩家 2 B玩家

        self.flag = "in_race"
        # all situation is "in_race" or "a_win" or "b_win"
# ----------------------------------------------------------------
        self.learn_rate = 0.1
        self.rand_poss = 0.05
        self.net_values = []
        self.default_value = 0.8
        self.need_been_change_value = 0.8


    def update_win(self):

        """

        [[2,1,1][1,1,0][1,2,0]]
        be like:
              0   1   2
            -------------
         0  | x | o | o |
         1  | x | x |   |
         2  | x | o |   |
            -------------

        """

        if self.race[0][0] == self.race[0][1] == self.race[0][2]:
            if self.race[0][0] == 1:
                self.flag = "a_win"
            elif self.race[0][0] == 2:
                self.flag = "b_win"
            else:
                pass
        if self.race[1][0] == self.race[1][1] == self.race[1][2]:
            if self.race[1][0] == 1:
                self.flag = "a_win"
            elif self.race[1][0] == 2:
                self.flag = "b_win"
            else:
                pass
        if self.race[2][0] == self.race[2][1] == self.race[2][2]:
            if self.race[2][0] == 1:
                self.flag = "a_win"
            elif self.race[2][0] == 2:
                self.flag = "b_win"
            else:
                pass
        if self.race[0][0] == self.race[1][0] == self.race[2][0]:
            if self.race[0][0] == 1:
                self.flag = "a_win"
            elif self.race[0][0] == 2:
                self.flag = "b_win"
            else:
                pass
        if self.race[0][1] == self.race[1][1] == self.race[2][1]:
            if self.race[0][1] == 1:
                self.flag = "a_win"
            elif self.race[0][1] == 2:
                self.flag = "b_win"
            else:
                pass
        if self.race[0][2] == self.race[1][2] == self.race[2][2]:
            if self.race[0][2] == 1:
                self.flag = "a_win"
            elif self.race[0][2] == 2:
                self.flag = "b_win"
            else:
                pass
        if self.race[0][0] == self.race[1][1] == self.race[2][2]:
            if self.race[2][2] == 1:
                self.flag = "a_win"
            elif self.race[2][2] == 2:
                self.flag = "b_win"
            else:
                pass
        if self.race[0][2] == self.race[1][1] == self.race[2][0]:
            if self.race[0][2] == 1:
                self.flag = "a_win"
            elif self.race[0][2] == 2:
                self.flag = "b_win"
            else:
                pass

    def reset(self):
        self.race = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    def do_once(self, racer: "str == a or b", location: list) -> str:
        if racer == "a":
            if self.race[location[0]][location[1]] == 0:
                self.race[location[0]][location[1]] = 1
            else:
                raise ValueError("this location has been used")
        if racer == "b":
            if self.race[location[0]][location[1]] == 0:
                self.race[location[0]][location[1]] = 2
            else:
                raise ValueError("this location has been used")
        return "fin"


    # 我对强化学习的理解还不够透彻
    def refresh_net(self, now_race: list, next_race: list, value: float, flag: bool) -> bool:
        # 传参： 赛场情况 需要更新的价值（在此赛场情况之前的价值） （本赛场）是否获胜
        hash_value = hash(str(now_race))
        hash_next = hash(str(next_race))

        if hash_next not in self.net_values:
            self.net_values.append([hash_next, self.default_value])

        if hash_value not in self.net_values:
            self.net_values.append([hash_value, self.default_value])
        else:
            now_value = self.net_values[hash_value]
            now_value = now_value + (now_value - self.last_value) / self.learn_rate

        return True


if __name__ == "__name__":
    time.sleep(1)
