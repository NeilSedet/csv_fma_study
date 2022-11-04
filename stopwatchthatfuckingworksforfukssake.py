from threading import Thread, Lock
import time


kill = False
sleep = False
value = 0


class Stopwatch:
    def counter(n):
        global kill, sleep, value
        while True:
            while not sleep:
                if kill == True:
                    return

                time.sleep(1)
                value += 1

    def askinput():
        global kill, sleep
        choice = input()

        if choice == "s":
            sleep = not sleep
        elif choice == "k":
            kill = True
            return 0

        return 1

    def stopwatch():
        t = Thread(target=Stopwatch.counter, args=(10,))
        t.start()

        while Stopwatch.askinput():
            pass

        t.join()


Stopwatch.stopwatch()
print(value)
