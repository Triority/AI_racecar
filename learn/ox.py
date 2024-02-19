import time
import hashlib
import numpy
import random
import json

class ooxx_machine():
    def __init__(self):
        self.race = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        # 用于表示棋盘 0代表没下过 1 A玩家 2 B玩家

        self.flag = "in_race"
        # all situation is "in_race" or "a_win" or "b_win"
# ----------------------------------------------------------------
        self.learn_rate = 0.1
        self.rand_poss = 0.05
        self.net_values = {}
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
    def refresh_net(self, now_race: list, next_race: list, flag: bool) -> bool:
        # 传参： 赛场情况 需要更新的价值（在此赛场情况之前的价值） （本赛场）是否获胜
        hash_value: int = hash(str(now_race))
        hash_next: int = hash(str(next_race))

        # 如果给下死了就给Value 置于 0
        if self.flag == 'b_win':
            self.net_values[hash_value] = 0
            return False

        # 更新下一次预期之获胜情况
        copy_race = self.race
        self.race = next_race
        self.update_win()
        if self.flag == 'a_win':
            next_value = 1
        else:
            next_value = 0
        self.race = copy_race
        self.update_win()

        if hash_next not in self.net_values:
            if next_value == 0:
                self.net_values[hash_value] = self.default_value
            elif next_value == 1:
                self.net_values[hash_value] = 1
        if hash_value not in self.net_values:
            self.net_values[hash_value] = self.default_value
            value = self.default_value
        else:
            value = self.net_values[hash_value]
        value = value + (next_value - value) * self.learn_rate

        self.net_values[hash_value] = value
        return True

    def save_net(self, filename='net.json'):
        with open(filename, 'w') as file:
            json.dump(self.net_values, file)
        print(f"Net values saved to {filename}.")

    def read_net(self, filename='net.json'):
        with open(filename, 'r') as file:
            self.net_values = json.load(file)
        print(f"Net values loaded from {filename}.")

    def start_train(self, epoch: int = 1000) -> bool:
        self.reset()
        for i in range(1, epoch):
            pass
            # do the race once at here

        return True



if __name__ == "__name__":
    time.sleep(1)
