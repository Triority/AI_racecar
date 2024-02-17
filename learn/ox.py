import time
import hashlib
import numpy
import random

class ooxx_machine():
    def __init__(self):
        self.race = [[0,0,0],[0,0,0],[0,0,0]]
        # 用于表示棋盘 0代表没下过 1 A玩家 2 B玩家
        self.a_win_situation =  [[[1,1,1],[0,0,0],[0,0,0]],[[0,0,0],[1,1,1],[0,0,0]],[[0,0,0],[0,0,0],[1,1,1]]
                                ,[[1,0,0],[1,0,0],[1,0,0]],[[0,1,0],[0,1,0],[0,1,0]],[[0,0,1],[0,0,1],[0,0,1]]
                                ,[[1,0,0],[0,1,0],[0,0,1]],[[0,0,1],[0,1,0],[1,0,0]]]
        self.b_win_situation =  [[[2,2,2],[0,0,0],[0,0,0]],[[0,0,0],[2,2,2],[0,0,0]],[[0,0,0],[0,0,0],[2,2,2]]
                                ,[[2,0,0],[2,0,0],[2,0,0]],[[0,2,0],[0,2,0],[0,2,0]],[[0,0,2],[0,0,2],[0,0,2]]
                                ,[[2,0,0],[0,2,0],[0,0,2]],[[0,0,2],[0,2,0],[2,0,0]]]

        self.flag = "in_race"
        # all situation is "in_race" or "a_win" or "b_win"
    def update_win(self):
        if self.race in self.a_win_situation:
            self.flag = "a_win"
        elif self.race in self.b_win_situation:
            self.flag = "b_win"
        else:
            pass

    def reset(self):
        self.race = [[0,0,0],[0,0,0],[0,0,0]]

    def do_once(self,racer: "str == a or b",location: list) -> str:
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


class DlModel:
    def __init__(self):
        self.learn_rate = 0.1
        self.rand_poss = 0.05
        self.net_values = []
    def refresh_net(self,race:list,value:float):
        hash_value = hash(race)
        if hash_value in self.net_values:
            pass






if __name__ == "__name__":


    time.sleep(1)