import csv
from problem import Problem

class IO:
    fieldnames = ["solved", "secs", "year", "number", "category"]
    CSV_data = "./bin/data.csv"
    stats_data = "./bin/stats.txt"

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

        with open(IO.CSV_data, encoding="utf-8", mode="a") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=IO.fieldnames)

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
        with open(IO.CSV_data, encoding="utf-8", mode="w") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=IO.fieldnames)
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

        with open(IO.CSV_data, encoding="utf-8", mode="r") as csv_file:
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
        with open(IO.stats_data, encoding="utf-8", mode="w") as txt_file:
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

        with open(IO.stats_data, encoding="utf-8", mode="r") as txt_file:
            for line in txt_file:
                times = line.split(",")
                probs_input[times[0]] = [int(x) for x in times[1:]]

        return probs_input
