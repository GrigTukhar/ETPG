import json

days = ("day1", "day2", "day3", "day4", "day5", "day6", "day7")
times =("morning", "lunch", "day", "evening")
sports = {"swimming", "cycling", "running"}
loads = ("easy", "medium", "hard")
answers = ("week", "workout", "exit")
replies_week = ("add", "remove", "exit")
replies_workout = ("edit", "remove", "exit")

def loadData():
    with open('main.json') as data_file:
        schedule = json.load(data_file)
    return schedule

def loadPredef():
    with open('main.json') as data_file:
        predata = json.load(data_file)
    preworkouts = predata["workouts"]
    return(preworkouts)

def editWeek(data):
    count = 1
    reply = "x"
    print("Current weeks in schedule :(" + (", ").join(data["schedule"].keys()) + ")")
    for key in data["schedule"]:
        count = count + 1

    while (reply not in replies_week):
        reply = str(input("What would you like to do with the weeks (" + (", ").join(replies_week) + "): "))
        if (reply not in replies_week):
            print("Invalid input, try again")

    if (reply == "add"):
        count = str(count)
        print("week"+count, "has been added")
        data["schedule"]["week"+count] = { "day1": { "morning": -1, "lunch": -1, "day": -1, "evening": -1 }, "day2": { "morning": -1, "lunch": -1, "day": -1, "evening": -1 }, "day3": { "morning": -1, "lunch": -1, "day": -1, "evening": -1 }, "day4": { "morning": -1, "lunch": -1, "day": -1, "evening": -1 }, "day5": { "morning": -1, "lunch": -1, "day": -1, "evening": -1 }, "day6": { "morning": -1, "lunch": -1, "day": -1, "evening": -1 }, "day7": { "morning": -1, "lunch": -1, "day": -1, "evening": -1 } }

    if (reply == "remove"):
        count = count - 1
        count = str(count)
        print("week"+count, "has been removed")
        del data["schedule"]["week" + count]
    file = open("main.json", "w")
    file.write(json.dumps(data))
    file.close()

def editWorkout(data,preworkouts):
    week = "x"
    time = "x"
    reply = "x"
    while week not in data["schedule"].keys():
        week = input(str("Input week (" + (", ").join(data["schedule"].keys()) + "): "))
        if week not in data["schedule"].keys():
            print("That does not exist, try again")
        else:
            day ="x"
            while day not in days:
                day = input(str("Input day (" + (", ").join(days) + "): "))
                if day not in days:
                    print("That does not exist, try again")

    week_schedule = data["schedule"][week][day]
    print("Currently looking at workouts on",day, "in",week, ":", week_schedule)
    while time not in times:
        time =input(str("Input time of day (" + (", ").join(times) + "): "))
        if time not in times:
            print("That does not exist, try again")
    if (week_schedule[time]==-1):
        print("No workout planned for",time)
    else:
        print("Workout planned for",time,"=",week_schedule[time])
    while (reply not in replies_workout):
        reply = str(input("Choose an option to perform on this workout (" + (", ").join(replies_workout) + "): "))
        if (reply not in replies_workout):
            print("Invalid input, try again")

    if(reply == "remove"):
        if (week_schedule[time]==-1):
            print(time, "is already empty")
        else:
            data["schedule"][week][day][time]=-1
            print("Workout during", time, "on", day,"in",week,"has been removed")

    if(reply == "edit"):
        ask = "x"
        workout = "x"
        while (ask != "yes" and ask != "no"):
            ask = str(input("Would you like to add a predefined workout? yes/no: "))
            if (ask != "yes" and ask != "no"):
                print("Invalid input, try again")

        if (ask == "yes"):
            while (workout not in preworkouts.keys()) or workout == "test":
                workout = input(str("Input premade workout, except for 'test' (" + (", ").join(preworkouts.keys()) + "): "))
                if workout == "test":
                    print("Cannot use test")
                elif (workout not in preworkouts.keys()):
                    print("That does not exist, try again")
                else:
                    data["schedule"][week][day][time] = {"predefinedworkout": workout}
                    print("Premade workout",workout,"has been placed during",time,"on", day,"in",week)

        if (ask == "no"):
            sport = "x"
            load = "x"
            while (sport not in sports):
                sport = str(input("Choose sport type (" + (", ").join(sports) + "): "))
                if (sport not in sports):
                    print("Invalid input, try again")

            isMinutesSet = False
            while (not isMinutesSet):
                minutes = input("Input amount of time in minutes from 0 to 240: ")
                try:
                    minutes = float(minutes)
                    if (minutes > 0 and minutes <= 240):
                        isMinutesSet = True
                    else:
                        print("Wrong Input: Please type a positive integer number above 0 and below 240")
                except ValueError:
                    print("Wrong Input: Please input a number")

            isDistanceSet = False
            while (not isDistanceSet):
                distance = input("Input the distance in kilometers from 0 to 200: ")
                try:
                    distance = float(distance)
                    if (distance > 0 and distance <= 200):
                        isDistanceSet = True
                    else:
                        print("Wrong Input: Please type a positive integer number above 0 and below 200")
                except ValueError:
                    print("Wrong Input: Please input a number")

            while (load not in loads):
                load = str(input("Choose sport type (" + (", ").join(loads) + "): "))
                if (load not in loads):
                    print("Invalid input, try again")
            data["schedule"][week][day][time] = {"type": sport, "minutes": minutes, "distance": distance, "load": load}
            print("Workout has been made during",time,"on",day,"in",week,":", week_schedule[time])
    file = open("main.json", "w")
    file.write(json.dumps(data))
    file.close()

def main():
    data = loadData()
    preworkouts = loadPredef()
    answer = "x"
    while (answer not in answers) or answer !="exit":
        answer = str(input("Coach Menu | What would you like to edit in the schedule (" + (", ").join(answers) + "): "))
        if (answer not in answers):
            print("Invalid input, try again")
        elif (answer=="week"):
            editWeek(data)
        elif (answer=="workout"):
            editWorkout(data,preworkouts)

