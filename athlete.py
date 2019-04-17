import json

days = ("day1", "day2", "day3", "day4", "day5", "day6", "day7")

def loadData():
    with open('main.json') as data_file:
        schedule = json.load(data_file)
    return schedule

def loadDataForWeekAndDay(full_schedule, week,day):
    week_schedule = full_schedule["schedule"][week][day]
    if len(week_schedule.keys())== 0:
        return(0)
    return(week_schedule)

def loadPredef():
    with open('main.json') as data_file:
        predata = json.load(data_file)
    preworkouts = predata["workouts"]
    return(preworkouts)

def currDay(schedule,day,preworkouts):
    if schedule == 0:
        return 0
    curr_work = {day: {}}
    for key in schedule:
        if (schedule[key] != -1 and "predefinedworkout" in schedule[key].keys()):
            curr_work[day][key] = preworkouts[schedule[key]["predefinedworkout"]]
        else:
            curr_work[day][key] = schedule[key]

    return curr_work

def saveWorkouts(workouts):
    if workouts==0:
        file = open("current_workouts.json", "w")
        file.write('{"info": "No workouts set for today"}')
        file.close()
    else:
        file = open("current_workouts.json", "w")
        file.write(json.dumps(workouts))
        file.close()

def printWorkouts(curr_work,day):
    if curr_work==0:
        print("No workouts set for today")
    else:
        for key in curr_work[day]:
            if curr_work[day][key]== -1:
                print(key, ":", "no excerisize for this time of day")
            else:
                print(key, ":",curr_work[day][key])


def main():
    week = "x"
    full_schedule = loadData()

    while week not in full_schedule["schedule"].keys():
        week = input(str("Input week (" + (", ").join(full_schedule["schedule"].keys()) + "): "))
        if week not in full_schedule["schedule"].keys():
            print("That does not exist, try again")
        else:
            day ="x"
            while day not in days:
                day = input(str("Input day (" + (", ").join(days) + "): "))
                if day not in days:
                    print("That does not exist, try again")
                else:
                    week_schedule =loadDataForWeekAndDay(full_schedule,week,day)
                    preworkouts = loadPredef()
                    current_workout = currDay(week_schedule,day,preworkouts)
                    saveWorkouts(current_workout)
                    printWorkouts(current_workout,day)
main()
