import json
import random

answers = ("randomize", "exit")
sports = ("swimming", "cycling", "running")
loads = ("easy", "medium", "hard")

def loadData():
    with open('main.json') as data_file:
        schedule = json.load(data_file)
    return schedule

def randomizeData(schedule):
    weekcount = 0
    for week in schedule["schedule"]:
        weekcount = weekcount + 1
        for day in schedule["schedule"][week]:
            for key in schedule["schedule"][week][day]:
                sport = random.choice(sports)
                if sport == "swimming":
                    time = random.randrange(30, 91, 10)
                    load = random.choice(loads)
                    if load == "easy":
                        distance = round(time * 0.03, 1)
                        schedule["schedule"][week][day][key] = {"type": sport, "minutes": time, "distance": distance, "load": load}
                    if load == "medium":
                        distance = round(time * 0.06, 1)
                        schedule["schedule"][week][day][key] = {"type": sport, "minutes": time, "distance": distance,
                                                                "load": load}
                    if load == "hard":
                        distance = round(time * 0.08, 1)
                        schedule["schedule"][week][day][key] = {"type": sport, "minutes": time, "distance": distance,
                                                                "load": load}
                elif sport == "cycling":
                    time = random.randrange(45, 600, 15)
                    load = random.choice(loads)
                    if load == "easy":
                        distance = round(time * 0.333, 0)
                        schedule["schedule"][week][day][key] = {"type": sport, "minutes": time, "distance": distance,
                                                                "load": load}
                    if load == "medium":
                        distance = round(time * 0.5, 0)
                        schedule["schedule"][week][day][key] = {"type": sport, "minutes": time, "distance": distance,
                                                                "load": load}
                    if load == "hard":
                        distance = round(time * 0.7, 0)
                        schedule["schedule"][week][day][key] = {"type": sport, "minutes": time, "distance": distance,
                                                                "load": load}
                else:
                    time = random.randrange(20, 120, 10)
                    load = random.choice(loads)
                    if load == "easy":
                        distance = round(time * 0.1, 1)
                        schedule["schedule"][week][day][key] = {"type": sport, "minutes": time, "distance": distance,
                                                                "load": load}
                    if load == "medium":
                        distance = round(time * 0.175, 1)
                        schedule["schedule"][week][day][key] = {"type": sport, "minutes": time, "distance": distance,
                                                                "load": load}
                    if load == "hard":
                        distance = round(time * 0.250, 1)
                        schedule["schedule"][week][day][key] = {"type": sport, "minutes": time, "distance": distance,
                                                                "load": load}

    file = open("main.json", "w")
    file.write(json.dumps(schedule))
    file.close()
    print("\nSchedule has been randomized for",weekcount, "weeks")

def main():
    answer = "x"
    while (answer not in answers) or answer != "exit":
        answer = str(
            input("\nRandom Menu | This will randomize and create workouts for your schedule (" + (", ").join(answers) + "): "))
        if (answer not in answers):
            print("Invalid input, try again")
        elif (answer == "randomize"):
            reply = "x"
            while (reply != "no" and reply != "yes"):
                reply = str(input("\nThis will completely randomize workouts within your schedule, are you sure you want to continue? (yes/no): "))
                if (reply != "no" and reply != "yes"):
                    print("Invalid input, try again")
                elif (reply == "yes"):
                    schedule = loadData()
                    randomizeData(schedule)
