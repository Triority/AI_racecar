"""
to learn the Gradient Bandit

"""

import numpy
import random

def roll_1():
    x = numpy.random.normal(loc=500, scale=50, size=(1,1))
    x = int(x)

    return x

def roll_2():
    x = numpy.random.normal(loc=550, scale=150, size=(1,1))
    x = int(x)
    return x


# 两个老虎机的学习期望奖励与投掷次数
expect_a = 1000
times_a = 1
expect_b = 1000
times_b = 1
def learn():
    global expect_b, expect_a, times_a, times_b

    luck = random.randint(0,10) #有十分之一的概率会瞎几把选择老虎机
    if expect_a == expect_b or not luck:
        if random.randint(0,1):

            expect_a = (expect_a*times_a + roll_1())/(times_a+1)
            times_a += 1
        else:
            expect_b = (expect_b * times_b + roll_2()) / (times_b + 1)
            times_b += 1
    elif expect_a > expect_b:
        expect_a = (expect_a * times_a + roll_1()) / (times_a + 1)
        times_a += 1
    elif expect_a < expect_b:
        expect_b = (expect_b * times_b + roll_2()) / (times_b + 1)
        times_b += 1

if __name__ == "__main__":
    a = 1
    while a <= 10000:
        a += 1
        learn()
        print("a"+str(expect_a))
        print("b"+str(expect_b))
    if expect_a > expect_b:
        print("we choose A and the expect of a is "+ str(expect_a)+"the expect b is" + str(expect_b))
    elif expect_a < expect_b:
        print("we choose B and the expect of b is "+ str(expect_b)+"the expect a is" + str(expect_a))