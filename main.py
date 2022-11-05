import csv
import time
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
            self.solved
            + " "
            + self.secs
            + " "
            + self.year
            + " "
            + self.number
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
        choice = input()

        if choice == "s":
            self.sleep = not self.sleep
        elif choice == "k":
            self.kill = True
            return 0

        return 1

    def stopwatch(self):
        t = Thread(target=self.counter, args=(10,))
        t.start()

        while self.askinput():
            pass

        t.join()


class CSV:
    def getData(self):
        csv_categories = []
        with open("input.txt", encoding="utf-8", mode="r") as f:
            lines = f.readlines()
            for line in lines:
                csv_categories.append(line[:-1])

        return csv_categories

    def initCSV(self, csv_categories):
        with open("data.csv", encoding="utf-8", mode="a") as csv_file:
            fieldnames = ["solved", "secs", "year", "number", "category"]
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            # writer.writeheader()
            line_num = 1
            for csv_category in csv_categories:

                writer.writerow(
                    {
                        "solved": False,
                        "secs": -1,
                        "year": 2017,
                        "number": line_num,
                        "category": csv_category,
                    }
                )
                line_num += 1

    def writeCSV(self, problem_list):
        with open("data.csv", encoding="utf-8", mode="w") as csv_file:
            fieldnames = ["solved", "secs", "year", "number", "category"]
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()

            for problem_csv in problem_list:
                writer.writerow(
                    {
                        "solved": problem_csv["solved"],
                        "secs": problem_csv["secs"],
                        "year": problem_csv["year"],
                        "number": problem_csv["number"],
                        "category": problem_csv["category"],
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
                        row["solved"],
                        row["secs"],
                        row["year"],
                        row["number"],
                        row["category"],
                    )
                )

        return probs_input

    def readCSVlist(self):
        probs_input = []
        with open("data.csv", encoding="utf-8", mode="r") as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                probs_input.append(
                    Problem(
                        row["solved"],
                        row["secs"],
                        row["year"],
                        row["number"],
                        row["category"],
                    )
                )

        return probs_input


if __name__ == "__main__":
    # implement problem dispenser and time updater
    # implement last 10 problem archive

    csv_obj = CSV()
    problems = csv_obj.readCSVdict()
    # problems = sorted(problems, key=lambda x: x.category)

    is_quit = False
    while not is_quit:
        category = input()
        category_problems = problems[Problem.problem_categories[int(category)]]
        for category_problem in category_problems:
            print(category_problem)
