# CODE_RUNNER: 3.07 Homework - Student daily routine
def daily_routine(student):
    recommendations = []
    if student["logged_in"]:
        recommendations.append("Account ready: review today's schedule.")
        if student["homework_finished"]:
            if student["practice_today"]:
                recommendations.append("Homework finished: attend practice, then dinner.")
            else:
                recommendations.append("Homework finished: enjoy free time before dinner.")
        else:
            if student["practice_today"]:
                recommendations.append("Finish homework before practice; leave time for dinner.")
            else:
                recommendations.append("Finish homework before dinner and free time.")
        if student["lunch_packed"]:
            if student["practice_today"]:
                recommendations.append("Bring packed lunch and an extra practice snack.")
            else:
                recommendations.append("Bring packed lunch; plan dinner after homework.")
        else:
            if student["practice_today"]:
                recommendations.append("Buy lunch and an extra practice snack.")
            else:
                recommendations.append("Buy lunch; plan dinner after homework.")
    else:
        recommendations.append("Log in first to view the student schedule.")
    return recommendations

student = {"logged_in": True, "homework_finished": False,
           "lunch_packed": True, "practice_today": True}
for recommendation in daily_routine(student):
    print(recommendation)
