# Pickle module allows you to save data after program closes
import pickle
from typing import List

week = {"Sunday": [], "Monday": [], "Tuesday": [],
        "Wednesday": [], "Thursday": [], "Friday": [], "Saturday": []}


class Agenda(object):
    def __init__(self):
        self.week = week

    def main(self):
        OPTION_TO_FUNCTION = {
            "A": self.look_at_agenda,
            "B": self.create_task,
            "C": self.clear_list,
            "D": self.quit_program,
        }
        option = self.read_user_input_from_options(
            """
            What would you like to do?
            A - look at agenda
            B - create task
            C - clear list
            D - quit
            """,
            valid_inputs=["a", "b", "c", "d"],
        )
        return OPTION_TO_FUNCTION[option]()

    def read_user_input_from_options(self, message: str, valid_inputs: List = None):
        """
        Show `message` in the console while asking for user input.

        If `valid_inputs` is not provided, returns the value from user as is.
        """
        if valid_inputs:
            valid_inputs = list(map(lambda x: x.upper(), valid_inputs))
        while True:
            user_input = input(message)
            user_input = user_input.upper()
            if not valid_inputs:
                return user_input
            if user_input in valid_inputs:
                return user_input
            print("Invalid option chosen. Try again.")

    def valid_days(self):
        self.day = input("What day? ").capitalize()
        week_list = [day_list for day_list in week.keys()]
        if self.day not in week_list:
            print("Invalid day.")
            self.valid_days()

    """ Loads whatever string from week.dat file """

    def look_at_agenda(self):
        see_all = input("See entire week? Y - yes, N - no. ").upper()
        if see_all == "Y":
            week = pickle.load(open("week.dat", "rb"))
            print(week)
        elif see_all == "N":
            self.valid_days()
            week = pickle.load(open("week.dat", "rb"))
            print(week[self.day])
        else:
            print("Invalid option.")
            self.look_at_agenda()
        self.main()

    def create_task(self):
        self.valid_days()
        task = input("Describe your task. ")
        """ Loads string from week.dat file; when program restarts, it allows you to create a task without deleting the saved ones """
        week = pickle.load(open("week.dat", "rb"))
        week[self.day].append(task)
        """ Saves string into week.dat file so it remembers when you open the program again """
        pickle.dump(week, open("week.dat", "wb"))
        self.main()

    def clear_list(self):
        clear_all = input("Clear all lists? Y - yes, N - no ").upper()
        if clear_all == "N":
            self.valid_days()
            week[self.day].clear()
            print(f"List cleared for {self.day}!")
            """ saves the new list into a week.dat file """
            pickle.dump(week, open("week.dat", "wb"))
        elif clear_all == "Y":
            [week[day].clear() for day in week]
            print("All lists cleared!")
            """ saves the now empty list into a week.dat file """
            pickle.dump(week, open("week.dat", "wb"))
        else:
            print("Invalid option.")
            self.clear_list()
        self.main()

    def quit_program(self):
        print("Have a nice day!")
        return


if __name__ == "__main__":
    Agenda().main()
