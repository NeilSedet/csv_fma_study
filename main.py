from runner import doProblems, getStats
from storedIO import IO

if __name__ == "__main__":
    # TODO make pylint warnings go away
    # TODO add quitting without saving

    csv_obj = IO()
    problems = csv_obj.readCSVdict()
    times = csv_obj.readStatsCSV()

    option = input("doProblems, getStats? p or s: ")
    if option == "p":
        problems, times = doProblems(problems, times)
    elif option == "s":
        getStats(times)

    csv_obj.writeStatsCSV(times)
    csv_obj.writeCSV(problems)
