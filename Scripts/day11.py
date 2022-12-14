from copy import deepcopy

monkeys = {
    0: {"items": [50, 70, 89, 75, 66, 66], "op": ["mult", 5], "test": 2, "throw": [2, 1]},
    1: {"items": [85], "op": ["square"], "test": 7, "throw": [3, 6]},
    2: {"items": [66, 51, 71, 76, 58, 55, 58, 60], "op": ["plus", 1], "test": 13, "throw": [1, 3]},
    3: {"items": [79, 52, 55, 51], "op": ["plus", 6], "test": 3, "throw": [6, 4]},
    4: {"items": [69, 92], "op": ["mult", 17], "test": 19, "throw": [7, 5]},
    5: {"items": [71, 76, 73, 98, 67, 79, 99], "op": ["plus", 8], "test": 5, "throw": [0, 2]},
    6: {"items": [82, 76, 69, 69, 57], "op": ["plus", 7], "test": 11, "throw": [7, 4]},
    7: {"items": [65, 79, 86], "op": ["plus", 5], "test": 17, "throw": [5, 0]}
    }

def calculate_monkey_business(monkeys, rounds, reduce):

    throws = {x: 0 for x in range(8)}

    if not reduce:
        mod = 1

        for value in monkeys.values():
            mod *= value["test"]

    for _ in range(rounds):
        for i in range(8):

            throws[i] += len(monkeys[i]["items"])

            for num in monkeys[i]["items"]:

                if monkeys[i]["op"][0] == "mult":
                    num *= monkeys[i]["op"][1]
                elif monkeys[i]["op"][0] == "plus":
                    num += monkeys[i]["op"][1]
                elif monkeys[i]["op"][0] == "square":
                    num *= num
                
                if reduce:
                    num = num//3
                else:
                    num = num % mod

                if num % monkeys[i]["test"] == 0:
                    monkeys[monkeys[i]["throw"][0]]["items"].append(num)
                else:
                    monkeys[monkeys[i]["throw"][1]]["items"].append(num)
            
            monkeys[i]["items"] = []
    
    return sorted(throws.values())[-1] * sorted(throws.values())[-2]

print(f"Part one: {calculate_monkey_business(deepcopy(monkeys), 20, True)}")
print(f"Part two: {calculate_monkey_business(deepcopy(monkeys), 10000, False)}")
