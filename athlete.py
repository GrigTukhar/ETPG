import json
import time


days = ("day1", "day2", "day3", "day4", "day5", "day6", "day7")
times =("morning", "lunch", "day", "evening")

def loadData():
    with open('main.json') as data_file:
        schedule = json.load(data_file)
    return schedule

def loadDataForWeekAndDay(full_schedule, week,day):
    week_schedule = full_schedule["schedule"][week][day]
    if (week_schedule["morning"]== -1) and (week_schedule["lunch"]== -1) and (week_schedule["day"]== -1) and (week_schedule["evening"]== -1):
        return(0)
    return(week_schedule)

def loadPredef():
    with open('main.json') as data_file:
        predata = json.load(data_file)
    preworkouts = predata["workouts"]
    return(preworkouts)

def loadFeedback():
    with open('feedback.json') as data_file:
        preFeedback = json.load(data_file)
    return (preFeedback)

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

def feedback(curr_work,day,week, preFeedback):
    answer = "x"
    time_answer = "x"
    date = time.time()
    feedback_work = preFeedback
    if curr_work!=0:
        while (answer != "no"):
            answer = input("Would you like to provide feedback for a workout? yes/no: ")
            if (answer != "yes" and answer != "no"):
                print("Invalid input, try again")
            elif(answer == "yes"):
                while time_answer not in times:
                    time_answer = input("Input time of day (" + (", ").join(times) + "): ")
                    if time_answer not in times:
                        print("That does not exist, try again")
                    else:
                        if curr_work[day][time_answer] == -1:
                            print("No workout for this time of day, cannot provide feedback")
                        else:
                            ifDone = "x"
                            while (ifDone != "yes" and ifDone != "no"):
                                ifDone = str(input("Have you completed the workout? yes/no: "))
                                if (ifDone != "yes" and ifDone != "no"):
                                    print("Invalid input, try again")
                            text_feedback = input("Input feedback (if you did the workout how you felt, if not why): ")
                            feedback_work[date] = {week: {day: {time_answer: {}, "hasCompleted": {}, "feedback": {}}}}
                            feedback_work[date][week][day][time_answer] = curr_work[day][time_answer]
                            feedback_work[date][week][day]["hasCompleted"] = ifDone
                            feedback_work[date][week][day]["feedback"] = text_feedback
                            file = open("feedback.json", "w")
                            file.write(json.dumps(feedback_work ))
                            file.close()

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
                    preWorkouts = loadPredef()
                    preFeedback = loadFeedback()
                    current_workout = currDay(week_schedule,day,preWorkouts)
                    saveWorkouts(current_workout)
                    printWorkouts(current_workout,day)
                    feedback(current_workout,day,week,preFeedback)
main()
