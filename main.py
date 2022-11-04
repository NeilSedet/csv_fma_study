import csv
import time
from threading import Thread


class Problem:
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
        categories = []
        with open("input.txt", encoding="utf-8", mode="r") as f:
            lines = f.readlines()
            for line in lines:
                categories.append(line[:-1])

        return categories

    def writeCSV(self, categories):
        with open("data.csv", encoding="utf-8", mode="a") as csv_file:
            fieldnames = ["solved", "secs", "year", "number", "category"]
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            # writer.writeheader()
            line_num = 1
            for category in categories:

                writer.writerow(
                    {
                        "solved": False,
                        "secs": -1,
                        "year": 2017,
                        "number": line_num,
                        "category": category,
                    }
                )
                line_num += 1

    def readCSV(self):
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


csv_obj = CSV()
problems = csv_obj.readCSV()
problems = sorted(problems, key=lambda x: x.category)

for problem in problems:
    print(problem)
