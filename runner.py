from problem import Problem
from stopwatch import Stopwatch
from storedIO import IO
import pandas as pd

def getCategory():
    print("\n")
    for number in range(len(Problem.problem_categories)):
        print(number, Problem.problem_categories[number])

    category = input("category:\n")
    category_str = Problem.problem_categories[int(category)]
    print(category_str, "\n")
    return category_str


def doProblems(problems, times):
    is_quit = False
    while not is_quit:
        choice = getCategory()
        category_problems = problems[choice]

        quit_problems = False
        for category_problem in category_problems:
            print(category_problem, "\n")
            stopwatch = Stopwatch()
            stopwatch.start()

            category_problem.secs = stopwatch.value
            category_problem.solved = True
            times[choice].append(stopwatch.value)

            quit_problems = "q" == input("\nquit category? q or n: \n")
            if quit_problems:
                break

        problems[choice] = category_problems
        is_quit = "q" == input("\nquit problems? q or n: \n")

    return problems, times


def getStats(times):
    is_quit = False
    while not is_quit:
        choice = getCategory()
        category_times = times[choice]

        s = pd.Series(category_times)
        print("lifetime stats")
        print(s.describe())

        while len(category_times) > 10:
            category_times.pop(0)

        s = pd.Series(category_times)
        print("last 10 stats")
        print(s.describe())

        is_quit = "q" == input("q or n: \n")

    return times

