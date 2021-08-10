""" Optimized module """

import csv
from os import sendfile
from typing import List

from utilities import time_it

# csv_file = './data/dataset-forcebrut.csv'
csv_file = './data/dataset1_Python+P7.csv'
# csv_file = './data/dataset2_Python+P7.csv'

class Action:
    list_action: List = []

    def __init__(self, name, price, profit) -> None:
        self.price = price
        self.name = name
        self.profit = profit
        if price == 0:
            self.gain_in_euro = 0
        else :
            self.gain_in_euro = (price * profit) / 100

        # Calcule du ratio : Gain/prix
        if price ==  0:
            self.ratio = 0
        else :
            self.ratio = self.gain_in_euro / self.price
        self.list_action.append(self)

    def __repr__(self) -> str:
        return self.name + ", price : " + str(self.price) + "€ , profit : " + str(self.gain_in_euro) +"€, ratio : "+ str(self.ratio)


def read_file(file):
    """Open a csv file and create actions instances

    Args:
        file (string): path to csv file
    """
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            Action(row['name'], float(row['price']), float(row['profit']))


def display_result(stocks, total_cost, total_benefit):
    """print result : Stocks combinaisons, total cost, total benefit

    Args:
        actions (lits): stock to buy
        total_cost (float): total stock's cost
        total_benefit (float): total stocks benefit
    """
    for el in stocks:
        print(el)
    print("total cost : ", round(total_cost,2),"€")
    print("total return : ", round(total_benefit, 2),"€")


@time_it
def main(file):
    read_file(file)

    sorted_list = sorted(Action.list_action, key=lambda action: action.ratio, reverse=True)

    total_cost = 0
    total_benefit = 0
    stocks = []
    for el in sorted_list:
        if (total_cost + el.price) <= 500 and (el.price > 0):
            stocks.append(el)
            total_cost += el.price
            total_benefit += (el.price * el.profit)/100
        if total_cost >= 500:
            break

    display_result(stocks, total_cost, total_benefit)



if __name__ == "__main__":
    main(csv_file)