import csv
import time
import pandas as pd
from threading import Thread


class Problem:
    problem_categories = [
        "Kinematics",
        "Dynamics",
        "Energy",
        "Collisions",
        "System of Masses",
        "Rigid Bodies",
        "Oscillatory Motion",
        "Gravity",
        "Fluids",
        "Other",
        "Elasticity",
        "Experiment",
        "Dimensional Analysis",
        "Graphs",
        "Waves",
    ]

    def __init__(self, solved, secs, year, number, category):
        self.solved = solved
        self.secs = secs
        self.year = year
        self.number = number
        self.category = category

    def __repr__(self):
        return (
            str(self.solved)
            + " "
            + str(self.secs)
            + " "
            + str(self.year)
            + " "
            + str(self.number)
            + " "
            + self.category
        )


class Stopwatch:
    def __init__(self):
        self.kill = False
        self.sleep = False
        self.value = 0

    def counter(self, n):
        while True:
            while not self.sleep:
                if self.kill == True:
                    return

                time.sleep(1)
                self.value += 1

    def askinput(self):
        choice = input("sleep, time, kill\n")

        if choice == "s":
            self.sleep = not self.sleep
        elif choice == "t":
            print(self.value)
        elif choice == "k":
            self.kill = True
            return 0

        return 1

    def start(self):
        t = Thread(target=self.counter, args=(10,))
        t.start()

        while self.askinput():
            pass

        t.join()


class CSV:
    fieldnames = ["solved", "secs", "year", "number", "category"]

    def getData(self):
        csv_categories = []
        with open("input.txt", encoding="utf-8", mode="r") as f:
            lines = f.readlines()
            for line in lines:
                csv_categories.append(line[:-1])

        return csv_categories

    def initCSV(self, csv_categories):
        solved = False
        secs = -1
        year = 2017

        with open("data.csv", encoding="utf-8", mode="a") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=CSV.fieldnames)

            line_num = 1
            for csv_category in csv_categories:

                writer.writerow(
                    {
                        "solved": solved,
                        "secs": secs,
                        "year": year,
                        "number": line_num,
                        "category": csv_category,
                    }
                )
                line_num += 1

    def writeCSV(self, csv_problem_list):
        with open("data.csv", encoding="utf-8", mode="w") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=CSV.fieldnames)
            writer.writeheader()

            for key, csv_problems in csv_problem_list.items():
                for csv_problem in csv_problems:
                    writer.writerow(
                        {
                            "solved": ("True" if csv_problem.solved else "False"),
                            "secs": csv_problem.secs,
                            "year": csv_problem.year,
                            "number": csv_problem.number,
                            "category": csv_problem.category,
                        }
                    )

    def readCSVdict(self):
        probs_input = dict()

        for csv_category in Problem.problem_categories:
            probs_input[csv_category] = list()

        with open("data.csv", encoding="utf-8", mode="r") as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                probs_input[row["category"]].append(
                    Problem(
                        (row["solved"] == "True"),
                        int(row["secs"]),
                        int(row["year"]),
                        int(row["number"]),
                        row["category"],
                    )
                )

        return probs_input

    def writeStatsCSV(self, time_list):
        with open("stats.txt", encoding="utf-8", mode="w") as txt_file:
            pcats = Problem.problem_categories
            for i in range(len(pcats)):
                write_list = list()
                write_list.append(pcats[i])
                for item in time_list[pcats[i]]:
                    write_list.append(str(item))

                txt_file.write(",".join(write_list))
                txt_file.write("\n")

    def readStatsCSV(self):
        probs_input = dict()
        for csv_category in Problem.problem_categories:
            probs_input[csv_category] = list()

        with open("stats.txt", encoding="utf-8", mode="r") as txt_file:
            for line in txt_file:
                times = line.split(",")
                probs_input[times[0]] = [int(x) for x in times[1:]]

        return probs_input


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


if __name__ == "__main__":
    # TODO make pylint warnings go away
    # TODO add quitting without saving

    csv_obj = CSV()
    problems = csv_obj.readCSVdict()
    times = csv_obj.readStatsCSV()

    option = input("doProblems, getStats? p or s: ")
    if option == "p":
        problems, times = doProblems(problems, times)
    elif option == "s":
        getStats(times)

    csv_obj.writeStatsCSV(times)
    csv_obj.writeCSV(problems)
