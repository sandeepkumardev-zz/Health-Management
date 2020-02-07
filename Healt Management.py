import time
import pandas as pd


# food function

mon = time.asctime()[:7]
date = time.asctime()[8:11]
time = time.asctime()[11:16]
t = f"{mon}{date}  {time}  "


def __food__():
    """ this function manage your food activity """
    global t

    items = {"breakfast": "", "lunch": "", "dinner": ""}

    print("Enter time :\n \t 1 - BreakFast\n \t 2 - Lunch\n \t 3 - Dinner")
    food_time = int(input())
    if (food_time == 1):
        food = input("Enter your Breakfast - ")
        items["breakfast"] = food
    elif (food_time == 2):
        food = input("Enter your Lunch - ")
        items["lunch"] = food
    elif (food_time == 3):
        food = input("Enter your Dinner - ")
        items["dinner"] = food
    else:
        print("You Enter Wrong value")

    data = f"{t} {items} \n"
    try:
        my_food = open("my_food.txt", "a")
        my_food.write(data)
        my_food.close()
        print("Successfully added.")
    except:
        print("Somthing went wrong")

    exercise = input(" \n Do you want add your exercise. Y / N ")
    if (exercise == "y"):
        __exercise__()


# exercise


def __exercise__():
    """ this function manage your gym activity """
    global t

    exercise = []
    time = []

    while True:
        exercise_name = input("Enter your exercise :")
        exercise.append(exercise_name)
        exercise_time = input("How much time you spend :")
        time.append(exercise_time)

        period_exercise = [item for item in exercise]
        period_time = [item for item in time]

        data = pd.DataFrame(
            {"Exercise Name": period_exercise,
             "Spend Time": period_time
             }
        )
        data = f" {t}\n {str(data)} \n\n"

        try:
            my_exercise = open("my_exercise.txt", "a")
            my_exercise.write(data)
            my_exercise.close()
            print("Successfully added.")
        except:
            print("Somthing went wrong \n")
        more_exercise = input("\tDo you want add more exercise. Y / N ")
        if more_exercise == "n":
            break

    food = input(" \n Do you want add your food. Y / N ")
    if (food == "y"):
        __food__()


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
