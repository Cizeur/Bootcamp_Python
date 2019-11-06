import time
from datetime import timedelta
from datetime import datetime
import getpass


def log(func):

    username = getpass.getuser()
    if not hasattr(log, "used"):
        setattr(log, "used", 1)
        with open('machine.log', 'w+') as f:
            f.write("")

    def time_formater(time):
        if time.days:
            return str(time.days) + "d " + str(time.seconds // 3600) + "h"
        if time.seconds > 3600:
            hours, seconds = divmod(time.seconds, 3600)
            minutes = seconds // 60
            return "{:d} h {:02d} min".format(hours, minutes)
        if time.seconds > 60:
            minutes, seconds = divmod(time.seconds, 60)
            return "{:d} min {:02d} s".format(minutes, seconds)
        if time.seconds:
            seconds = time.seconds + time.microseconds / 1000000
            return "{:.3f} s".format(seconds)
        else:
            return "{:.3f} ms".format(time.microseconds / 1000)

    def function_wrapper(*args):
        start = time.time()
        output = func(*args)
        end = timedelta(seconds=time.time() - start)
        end = time_formater(end)
        name = " ".join(list(map(str.capitalize, func.__name__.split("_"))))
        logs = "({:s})Running: {:<30s}[ exec-time = {:s} ]\n".format(
            username, name, end)
        with open('machine.log', 'a+') as f:
            f.write(logs)
        return output
    return function_wrapper


if __name__ == "__main__":

    from random import randint

    class CoffeeMachine():
        water_level = 100

        @log
        def start_machine(self):
            if self.water_level > 20:
                return True
            else:
                print("Please add water!")
                return False

        @log
        def boil_water(self):
            return "boiling..."

        @log
        def make_coffee(self):
            if self.start_machine():
                for _ in range(20):
                    time.sleep(0.1)
                    self.water_level -= 1
                print(self.boil_water())
                print("Coffee is ready!")

        @log
        def add_water(self, water_level):
            time.sleep(randint(1, 5))
            self.water_level += water_level
            print("Blub blub blub...")

    machine = CoffeeMachine()
    for i in range(0, 5):
        machine.make_coffee()
    machine.make_coffee()
    machine.add_water(70)
