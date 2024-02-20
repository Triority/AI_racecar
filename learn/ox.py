
import copy
import random
import json
import matplotlib.pyplot as plt
class ooxx_machine():
    def __init__(self):
        self.race = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        # 用于表示棋盘 0代表没下过 1 A玩家 2 B玩家

        self.flag = "in_race"
        # all situation is "in_race" or "a_win" or "b_win" or "all_lose"
# ----------------------------------------------------------------
        self.learn_rate = 0.05
        self.rand_poss = 0
        self.net_values = {}
        self.default_value = 0.5


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

        all_chess =0
        for i in range(0, 3):
            for j in range(0, 3):
                if self.race[i][j] != 0:
                    all_chess += 1
                    # print(all_chess)
        if all_chess == 8 and self.flag == "in_race":
            self.flag = "all_lose"
            return False

    def reset(self):
        self.race = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.flag ="in_race"
    def do_once(self, racer: "str == a or b", location: list) -> str:
        could_do = True
        for i in range(0,3):
            if 0 in self.race[i]:
                could_do = True
            else:
                pass
        if not could_do:
            self.flag = 'all_lose'
            return "fin"

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
        """
                # 如果给下死了就给Value 置于 0
                if self.flag == 'b_win' or self.flag == 'all_lose':
                    self.net_values[hash_value] = 0
                    return False

                # 更新下一次预期之获胜情况
                copy_race = self.race
                self.race = next_race
                self.update_win()
                if self.flag == 'a_win':
                    next_value = 1
                    self.net_values[hash_value] = 1
                elif self.flag == 'b_win' or "all_lose":
                    next_value = 0
                    self.net_values[hash_value] = 0
                self.race = copy_race
                self.update_win()
        """
        next_value = self.net_values[hash_next]
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

    def random_player(self,player:str):
        possible_location = []
        race_copy = self.race
        for i in range (0,3):
            for j in range(0,3):
                if race_copy[i][j] == 0:
                    possible_location.append([i, j])
        if not possible_location:
            self.flag = "all_lose"

            return False
        location = random.choice(possible_location)
        self.do_once(player, location)
    def start_train(self, epoch: int = 1000) -> bool:
        self.reset()
        a_win_times = 1
        b_win_times = 1
        win_rate = []
        for times in range(1, epoch):
            win_rate.append( a_win_times / (a_win_times + b_win_times))
            plt.plot(win_rate)
            #print(self.race)

            if self.flag == "a_win":
                a_win_times += 1
            elif self.flag == "b_win":
                b_win_times += 1

            # print(times)
            # print(self.net_values)

            self.reset()
            if random.randint(0,1):


                while self.flag == "in_race":
                    self.update_win()
                    if random.random() >= self.rand_poss:
                        next_races = []
                        for i in range(0, 3):
                            for j in range(0, 3):
                                if self.race[i][j] == 0:
                                    races_copy = copy.deepcopy(self.race)
                                    races_copy[i][j] = 1
                                    next_races.append(races_copy)
                                else:
                                    pass

                        values = []
                        for next_race in next_races:
                            copy_race = copy.deepcopy(self.race)
                            self.race = copy.deepcopy(next_race)
                            self.update_win()
                            if self.flag == 'a_win':
                                self.net_values[hash(str(next_race))] = 1

                            elif self.flag == 'b_win' or "all_lose":
                                self.net_values[hash(str(next_race))] = 0
                            self.race = copy.deepcopy(copy_race)
                            self.update_win()

                            next_hash = hash(str(next_race))
                            if next_hash not in self.net_values:
                                self.net_values[next_hash] = self.default_value
                                values.append(self.default_value)
                            else:
                                values.append(self.net_values[next_hash])

                        max_value = max(values)
                        max_indices = [index for index, value in enumerate(values) if value == max_value]

                        random_max_index = random.choice(max_indices)
                        next_race = next_races[random_max_index]
                        # print(next_races)
                        self.refresh_net(self.race, next_race, True)

                        self.race = next_race
                        #print(self.race)
                    else:
                        # print("random")
                        if self.random_player("a"):
                            pass
                        else:
                            break
                    self.random_player("b")

            else:

                while self.flag == "in_race":
                    self.update_win()
                    self.random_player("b")

                    if random.random() >= self.rand_poss:
                        next_races = []
                        for i in range(0, 3):
                            for j in range(0, 3):
                                if self.race[i][j] == 0:
                                    races_copy = copy.deepcopy(self.race)
                                    races_copy[i][j] = 1
                                    next_races.append(races_copy)
                                else:
                                    pass

                        values = []
                        for next_race in next_races:
                            copy_race = copy.deepcopy(self.race)
                            self.race = copy.deepcopy(next_race)
                            self.update_win()
                            if self.flag == 'a_win':
                                self.net_values[hash(str(next_race))] = 1

                            elif self.flag == 'b_win' or "all_lose":
                                self.net_values[hash(str(next_race))] = 0
                            self.race = copy.deepcopy(copy_race)
                            self.update_win()

                            next_hash = hash(str(next_race))
                            if next_hash not in self.net_values:
                                self.net_values[next_hash] = self.default_value
                                values.append(self.default_value)

                            else:

                                values.append(self.net_values[next_hash])
                        try:
                            max_value = max(values)
                        except:
                            print(self.race)
                            print(self.flag)
                        max_indices = [index for index, value in enumerate(values) if value == max_value]

                        random_max_index = random.choice(max_indices)
                        next_race = next_races[random_max_index]
                        # print(next_races)
                        self.refresh_net(self.race, next_race, True)

                        self.race = next_race
                        # print(self.race)
                    else:
                        # print("random")
                        if self.random_player("a"):
                            pass
                        else:
                            break







            # do the race once at here
        print(f"a wins {str(a_win_times)} b wins {str(b_win_times)}")
        print(f"A的胜率是{str(a_win_times/(a_win_times+b_win_times))}")
        plt.show()
        return True



if __name__ == "__main__":

    aa = ooxx_machine()
    aa.read_net()
    aa.start_train(10000)
    aa.save_net()
