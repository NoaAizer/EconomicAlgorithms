def division(parties, y, num_of_seats):
    """
    Calculate the division of seats for each party according to voting/f(s)=s+y
    :param parties: A list with the voting for each party
    :param y: The value added to the function in the denominator (f(s)=s+y)
    :param num_of_seats: Amount of seats the divide
    :return: A dictionary with the division
    """
    remain_seats = num_of_seats
    # Define a dictionary represents the seats for each party
    # [key = number of votes , value = current amount of seats]
    res = dict.fromkeys(parties, 0)
    while remain_seats > 0:
        values = []
        # Calculates the function value for each party
        for votes, seats in zip(parties, res.items()):
            denominator = (seats[1] + y)
            if denominator != 0:
                values.append(votes / (seats[1] + y))
            else:
                # All the parties have the same value
                values = [1] * len(parties)
        # Finds all the indexes of the parties with the highest value
        max_val = max(values)
        indexes = []
        for i, val in enumerate(values):
            if val == max_val:
                indexes.append(i)
        max_parties = []
        # Finds the parties with the highest value
        for i in indexes:
            max_parties.append(parties[i])
        # Updates the seats amount
        for pr in max_parties:
            res[pr] = res[pr] + 1
        remain_seats = remain_seats - len(indexes)
    return res


def main():
    print('--------------------------------- Example from class ---------------------------------\n')
    all_parties = [210, 50, 40]
    print('################################## Adams ##################################')
    res = division(all_parties, 0, 3)  # Adams
    print(res)
    print('################################## Webster ##################################')
    res = division(all_parties, 0.5, 3)  # Webster
    print(res)
    print('################################## Jefferson ##################################')
    res = division(all_parties, 1, 3)  # Jefferson
    print(res)

    all_parties = [1066892, 614112, 316008, 292257, 273836, 268767, 248391, 248370, 225641, 212583, 209161,
                   202218, 167064, 34883, 17346, 1309, 1291, 1189, 811, 729, 663, 592, 514, 486, 463, 443,
                   441, 429, 429, 408, 395, 395, 385, 256, 253, 226, 220, 196, 0]
    print('\n--------------------------------- Without blocking percentage ---------------------------------\n')
    print('################################## Adams ##################################')
    res = division(all_parties, 0, 120)  # Adams
    print(res)
    print('################################## Webster ##################################')
    res = division(all_parties, 0.5, 120)  # Webster
    print(res)
    print('################################## Jeferson ##################################')
    res = division(all_parties, 1, 120)  # Jeferson
    print(res)
    blocking = [1066892, 614112, 316008, 292257, 273836, 268767, 248391,
                248370, 225641, 212583, 209161, 202218, 167064]
    print('\n--------------------------------- With blocking percentage ---------------------------------\n')
    print('################################## Adams ##################################')
    res = division(blocking, 0, 120)  # Adams
    print(res)
    print('################################## Webster ##################################')
    res = division(blocking, 0.5, 120)  # Webster
    print(res)
    print('################################## Jefferson ##################################')
    res = division(blocking, 1, 120)  # Jefferson
    print(res)


if __name__ == '__main__':
    main()
