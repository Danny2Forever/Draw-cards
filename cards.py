import random
from traceback import print_tb
num =["A","1","2","3","4","5","6","7","8","9","10","J","Q","K"]

suit = ["♠","♥","♦","♣"]

def random_num():
    num_ran = random.randint(0,12)
    _num = num[num_ran]
    return _num

def random_suit():
    suit_ran = random.randint(0,3)
    _suit = suit[suit_ran]
    return _suit

def make_card(a ,b):
    print("---")
    for i in range (2):
        if i == 0 :
            print(f"|{a}|")
        if i == 1 :
            print(f"|{b}|")
    print("---")

card = int(input("How many card(s) you want : "))

def cards(time) :
    for i in range(time):
        make_card(random_num(),random_suit())

cards(card)