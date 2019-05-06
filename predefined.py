import json

answers = ("add", "remove", "edit", "exit")
sports = {"swimming", "cycling", "running"}
loads = ("easy", "medium", "hard")

def loadData():
    with open('main.json') as data_file:
        schedule = json.load(data_file)
    return schedule

def loadPredef():
    with open('main.json') as data_file:
        predata = json.load(data_file)
    preworkouts = predata["workouts"]
    return(preworkouts)

def editPredef(preworkouts,workout,data):
    print(workout, "=", preworkouts[workout])
    sport = "x"
    load = "x"
    while (sport not in sports):
        sport = str(input("Choose sport type (" + (", ").join(sports) + "): "))
        if (sport not in sports):
            print("Invalid input, try again")

    isTimeSet = False
    while (not isTimeSet):
        time = input("Input amount of time in minutes from 0 to 240: : ")
        try:
            time = float(time)
            if (time > 0 and time <= 240):
                isTimeSet = True
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

    data["workouts"][workout]= {"type": sport, "minutes": time, "distance": distance, "load": load}
    file = open("main.json", "w")
    file.write(json.dumps(data))
    file.close()
    print(workout, "=", data["workouts"][workout])

def addPredef(preworkouts,data):
    print("Existing workouts (" + (", ").join(preworkouts.keys()) + ") ")
    workout = "test"
    while workout in preworkouts.keys():
        workout = input(str("Input a name that does not exist: "))
        if workout in preworkouts.keys():
            print("That already exists, try again")
    sport = "x"
    load = "x"
    while (sport not in sports):
        sport = str(input("Choose sport type (" + (", ").join(sports) + "): "))
        if (sport not in sports):
            print("Invalid input, try again")

    isTimeSet = False
    while (not isTimeSet):
        time = input("Input amount of time in minutes from 0 to 240: : ")
        try:
            time = float(time)
            if (time > 0 and time <= 240):
                isTimeSet = True
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

    data["workouts"][workout] = {"type": sport, "minutes": time, "distance": distance, "load": load}
    file = open("main.json", "w")
    file.write(json.dumps(data))
    file.close()
    print(workout, "=", data["workouts"][workout])

def removePredef(workout,data):
    reply = "x"
    while (reply!="no" and reply!="yes"):
        reply = str(input("Are you sure you want to delete, if workout is in schedule it will be removed, yes/no: "))
        if (reply!="no" and reply!="yes"):
            print("Invalid input, try again")
    if (reply == "yes"):
        del data["workouts"][workout]
        for week in data["schedule"]:
            for day in data["schedule"][week]:
                for key in data["schedule"][week][day]:
                    if data["schedule"][week][day][key] == {"predefinedworkout": workout}:
                        data["schedule"][week][day][key] = -1
                        print(workout, "has been found in", week,"-",day,"-",key, "and has been removed")

        file = open("main.json", "w")
        file.write(json.dumps(data))
        file.close()

def main():

    workout = "x"
    full_predefined = loadPredef()
    data = loadData()
    answer = "x"
    while (answer not in answers) or answer !="exit":
        answer = str(input("Predefined Menu | What would you like to do with a predefined workout (" + (", ").join(answers) + "): "))
        if (answer not in answers):
            print("Invalid input, try again")
        elif (answer == "edit"):
            while (workout not in full_predefined.keys()) or workout=="test":
                workout = input(str("Input workout to edit except for 'test' (" + (", ").join(full_predefined.keys()) + "): "))
                if workout == "test":
                    print ("Cannot edit test")
                elif (workout not in full_predefined.keys()):
                    print("That does not exist, try again")
                else:
                    editPredef(full_predefined,workout,data)
        elif (answer == "add"):
            addPredef(full_predefined,data)
        elif (answer == "remove"):
            while (workout not in full_predefined.keys()) or workout == "test":
                workout = input(
                    str("Input workout to delete except for 'test' (" + (", ").join(full_predefined.keys()) + "): "))
                if workout == "test":
                    print("Cannot delete test")
                elif (workout not in full_predefined.keys()):
                    print("That does not exist, try again")
                else:
                    removePredef(workout,data)
