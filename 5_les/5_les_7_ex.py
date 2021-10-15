import json

result_dict = dict()
average_profit = 0
num_num_profit_over_zero = 0
with open('ex_7.txt', encoding='utf-8') as f_7:
    for line in f_7:
        name, type_of_ownership, proceeds, costs = line.split()
        profit = int(proceeds) - int(costs)
        if profit >= 0:
            average_profit += profit
            num_num_profit_over_zero += 1
        result_dict[name] = profit
average_profit = average_profit / num_num_profit_over_zero
print(average_profit)
with open("json7.json", "w", encoding="utf-8") as f_7:
    json.dump([result_dict, {"average_profit": average_profit}], f_7)
