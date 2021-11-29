import numpy as np

def payments(values: list[float], choice_rule) -> list[float]:
    values.sort()
    values.reverse()
    payment = values.copy()  # list of payment for each player
    temp_values = values.copy()
    chosen_list = choice_rule(values)
    flag = False  # Someone was not chosen
    for i, is_chosen in enumerate(chosen_list):
        if is_chosen and flag:  # The previous player (with lower value) was chosen - not monotonic
            raise Exception("The rule is not monotonic")
        else:
            if not is_chosen:
                payment[i] = 0
                flag = True
            else:
                while is_chosen:  # Calculates the threshold value for each player.
                    temp_values[i] -= 0.01
                    updated_list = choice_rule(temp_values)
                    is_chosen = updated_list[i]
                    payment[i] = temp_values[i]
                payment[i] += 0.01
                payment[i] = round(payment[i], 2)
    return payment


def max_value(values: list[float]) -> list[bool]:
    max_val = max(values)
    return [x == max_val for x in values]


def greater_than_5(values: list[float]) -> list[bool]:
    return [x > 5 for x in values]


def three_highest_values(values: list[float]) -> list[bool]:
    temp = values.copy()
    is_chosen = [False] * len(values)
    for i in range(3):
        index = np.argmax(temp)
        temp[index] = -1
        is_chosen[index] = True
    return is_chosen


if __name__ == '__main__':
    players_1 = [5, 11, 2, 10, 8]
    players_2 = [2, 5, 5, 12, 3]

    players_1.sort()
    players_1.reverse()
    print("Players:", players_1)
    print("The player with the highest value: ", payments(players_1, max_value))
    print("The players with value greater than 5: ", payments(players_1, greater_than_5))
    print("Three players with the highest value: ", payments(players_1, three_highest_values))

    print("--------------------------------------------------------------------------------------")
    players_2.sort()
    players_2.reverse()
    print("Players:", players_2)
    print("The player with the highest value: ", payments(players_2, max_value))
    print("The players with value greater than 5: ", payments(players_2, greater_than_5))
    print("Three players with the highest value: ", payments(players_2, three_highest_values))


