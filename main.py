# Pickle module allows you to save data after program closes
import pickle

week = {"Sunday": [], "Monday": [], "Tuesday": [],
        "Wednesday": [], "Thursday": [], "Friday": [], "Saturday": []}


def agenda():
    option = input(
        "What would you like to do?  (A - look at agenda, B - create task, C - clear list, or D - quit) ").upper()
    if option == "A":
        look_at_agenda()
    if option == "B":
        create_task()
    if option == "C":
        clear_list()
    if option == "D":
        print("Have a nice day!")
    else:
        print("Invalid option.")
        agenda()

# global allows day variable in other functions to work even without declaring it


def valid_days():
    global day
    day = input("Which day? ")
    week_list = [day_list for day_list in week.keys()]
    if day not in week_list:
        print("Invalid day.")
        look_at_agenda()


# Loads whatever string from week.dat file
def look_at_agenda():
    see_all = input("See entire week? Y - yes, N - no. ").upper()
    if see_all == "Y":
        week = pickle.load(open("week.dat", "rb"))
        print(week)
    elif see_all == "N":
        valid_days()
        week = pickle.load(open("week.dat", "rb"))
        print(week[day])
    else:
        print("Invalid option.")
        look_at_agenda()
    agenda()


def create_task():
    valid_days()
    task = input("Describe your task. ")
    # Loads string from week.dat file; when program restarts, it allows you to create a task without deleting the saved ones
    week = pickle.load(open("week.dat", "rb"))
    week[day].append(task)
    # Saves string into week.dat file
    pickle.dump(week, open("week.dat", "wb"))
    agenda()


def clear_list():
    clear_all = input("Clear all lists? Y - yes, N - no ").upper()
    if clear_all == "N":
        valid_days()
        week[day].clear()
        print(f"List cleared for {day}!")
        pickle.dump(week, open("week.dat", "wb"))
    elif clear_all == "Y":
        [week[day].clear() for day in week]
        pickle.dump(week, open("week.dat", "wb"))
    else:
        print("Invalid option.")
        clear_list()
    agenda()


agenda()
