import csv
from itertools import combinations
from typing import List

csv_file = './data/dataset-forcebrut.csv'
# csv_file = './data/dataset1_Python+P7.csv'


class Action:
    list_action: List = []

    def __init__(self, name, price, profit) -> None:
        self.price = price
        self.name = name
        self.profit = profit
        self.list_action.append(self)

    def __repr__(self) -> str:
        return self.name + ", " + str(self.price) + ", " + str(self.profit)


def rSubset(array, r):
    """Browse all combinations

    Args:
        array (list): brows this list to extract all possible combinaisons
        r (int): number of element per combinaison

    Returns:
        list: list des combinaisons possibles
    """
    return list(combinations(array, r))


def read_file(file):
    """Open a csv file and create actions instances

    Args:
        file (string): path to csv file
    """
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            Action(row['name'], float(row['price']), float(row['profit']))


def search_all_possibilities(max_cost):
    """Extract all combinaisons under max_price

    Args:
        max_cost (int): combinaison's cost must be lower than max_cost

    Returns:
        list: list of combinaison with a cost under max_cost
    """
    combi_actions_possible = []
    for l in range(len(Action.list_action)+1):
        combinaisons = rSubset(Action.list_action, l)
        for combinaison in combinaisons:
            price_sum = 0
            for el in combinaison:
                price_sum += el.price
            if price_sum <= max_cost:
                combi_actions_possible.append(combinaison)
    return combi_actions_possible


def search_max_profit(combi_actions_possible):
    """Extract max profit from possible combinaison

    Args:
        combi_actions_possible (list): list of tuple, each tuple is a possible combinaison of stocks

    Returns:
        tutple: max_benefit => higthest benefit in list, benefit_array => list of all benefit for all combinaisons
    """
    benefit_array = []
    for combinaison in combi_actions_possible:
        benefit_sum = 0
        for el in combinaison:
            benefit_sum += (el.profit * el.price)/100
        benefit_array.append(benefit_sum)
    max_benefit = max(benefit_array)
    return (max_benefit, benefit_array)


def search_max_profitable_combinaison(combi_actions_possible, benefit_array, max_benefit):
    """extract the best combinaison with the max benefit

    Args:
        combi_actions_possible (list): list of all possible combinaisons
        benefit_array (list): list of benefit per combinaison
        max_benefit (float): heightest benefit in benefit_array

    Returns:
        tutple: best_combinaison, price of this best combinaison
    """
    for i in range(len(benefit_array)):
        if benefit_array[i] == max_benefit:
            price = 0
            for action in combi_actions_possible[i]:
                price += action.price

            return (combi_actions_possible[i], price)


def display_result(most_profitable_combinaison, price, max_benefit):
    """Print result : Actions, total cost and total return

    Args:
        most_profitable_combinaison (list): list of stocks to buy
        price (float): total cost
        max_benefit (float): total return
    """
    for action in most_profitable_combinaison:
        print(action)
    print("total cost : ", round(price, 2),"€")
    print("Total return : ", round(max_benefit, 2),"€")


def main(file):
    """Main function

    Args:
        file (string): Path to csv file
    """

    read_file(file)
    combi_actions_possible = search_all_possibilities(500)
    max_benefit, benefit_array = search_max_profit(combi_actions_possible)
    most_profitable_combinaison, price = search_max_profitable_combinaison(combi_actions_possible, benefit_array, max_benefit)

    display_result(most_profitable_combinaison, price, max_benefit)



if __name__ == "__main__":
    main(csv_file)