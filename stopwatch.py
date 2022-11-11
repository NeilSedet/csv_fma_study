import time
from threading import Thread

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
