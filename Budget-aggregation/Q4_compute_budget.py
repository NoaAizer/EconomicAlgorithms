import statistics


def compute_budget(total_budget: float, citizen_votes: list[list]) -> list[float]:
    """
    >>> compute_budget(100, [[100, 0, 0], [0, 0, 100]])
    [50.0, 0, 50.0]
    >>> compute_budget(100, [[100, 0, 0]])
    [100, 0, 0]
    >>> compute_budget(100, [[100, 0, 0,0],[0,100,0,0],[0, 0, 100,0],[0, 0, 0,100]])
    [25.0, 25.0, 25.0, 25.0]
    >>> compute_budget(100, [[100, 0, 0,0],[0,100,0,0],[100, 0, 0,0],[0, 0, 0,100]])
    [50.0, 25.0, 0, 25.0]
    >>> compute_budget(30, [[30, 0, 0], [30, 0, 0]])
    [30, 0, 0]
    >>> compute_budget(30, [[30, 0, 0], [0, 30, 0],[0, 0, 30]])
    [10.0, 10.0, 10.0]
      """
    n = len(citizen_votes)
    num_of_subs = len(citizen_votes[0])
    ci_per_subs = {}
    budget = []

    for j in range(num_of_subs):
        ci_per_subs[j] = [item[j] for item in citizen_votes]  # list of votes per subject
        for i in range(1, n):  # constant voters
            ci_per_subs[j].append(i * total_budget / n)  # C *(i/n)

        budget.append(statistics.median(ci_per_subs[j]))
    return budget
