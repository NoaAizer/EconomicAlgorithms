import cvxpy
import numpy as np

def calcAegliterary(mat):
    agents_num, res_num = len(mat), len(mat[0])
    # Define a matrix of fractions of each resource for each agent
    frac_resources = [[cvxpy.Variable() for r in range(res_num)] for a in range(agents_num)]
    # Define a list of the sum of all fractions of a resource
    sum_fracs = np.sum(frac_resources, axis=0)
    # Define a constraints list.
    constraints = []

    # ############################### Constrains ###############################
    # All fractions of each resource sum to 1
    for res_fracs in sum_fracs:
        constraints.append(res_fracs == 1)
    # All fractions must be between 0 to 1
    for agent in frac_resources:
        for frac in agent:
            constraints.append(frac >= 0)
            constraints.append(frac <= 1)

    # All utilities should be greater than the min utility
    min_utility = cvxpy.Variable()
    constraints.append(min_utility >= 0)

    for agent in range(agents_num):
        agent_utility = 0
        for res in range(res_num):
            agent_utility += mat[agent][res] * frac_resources[agent][res]
        constraints.append(agent_utility >= min_utility)

    # ############################### Problem ###############################
    prob = cvxpy.Problem(
        cvxpy.Maximize(min_utility),  # Maximize the minimal value
        constraints=constraints)
    prob.solve()

    # Print
    print("status:", prob.status)
    print("optimal value", prob.value)
    for agent in range(agents_num):
        print("Agent #{} ".format(agent + 1), end='')
        for res in range(res_num):
            print(" gets {:.2f} of resource #{}".format(frac_resources[agent][res].value, res + 1), end= "")
            print(', ' if res != res_num-1 else '.\n', end='')


def main():
    mat = [
        [81, 19, 1],
        [70, 1, 29],
    ]

    calcAegliterary(mat)


if __name__ == '__main__':
    main()
