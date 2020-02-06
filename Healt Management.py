import datetime


# food function


def __food__():
    """ this function manage your food activity """
    print("Enter time :\n \t 1 - BreakFast\n \t 2 - Lunch\n \t 3 - Dinner")
    food_time = int(input())
    t = datetime.datetime.today().date()
    if (food_time == 1):
        f = " Breakfast "
    elif (food_time == 2):
        f = " Lunch     "
    elif (food_time == 3):
        f = " Dinner    "
    else:
        print("You Enter Wrong value")

    food = input("Enter your meel - ")
    data = f"{t} {f} {food} \n"
    try:
        my_food = open("my_food.txt", "a")
        my_food.write(data)
        my_food.close()
        print("Successfully added.")
    except:
        print("Somthing went wrong")


# exercise


def __exercise__():
    """ this function manage your gym activity """
    # collection = {} # make a dictonary
    l = input("Enter your exercise :")
    exercise_time = input("How much time you spend :")
    t = datetime.datetime.today().date()
    data = f"{t} {l} {exercise_time} min\n"
    try:
        my_exercise = open("my_exercise.txt", "a")
        my_exercise.write(data)
        my_exercise.close()
        print("Successfully added.")
    except:
        print("Somthing went wrong")


# main function
if __name__ == "__main__":
    print("Enter your Choice :\n \t 1 - Food\n \t 2 - Exercise")
    choice = int(input())
    if (choice == 1):
        __food__()
    elif (choice == 2):
        __exercise__()
    else:
        print("Plz enter valid choise")
