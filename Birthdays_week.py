from datetime import datetime, timedelta



list_birth = [
    {"name": "Bob", "birthday": datetime(year=1985, month=11, day=22)},
    {"name": "Jack", "birthday": datetime(year=1986, month=11, day=20)},
    {"name": "Serj", "birthday": datetime(year=1987, month=11, day=18)},
    {"name": "Sam", "birthday": datetime(year=1988, month=11, day=21)},
    {"name": "Kate", "birthday": datetime(year=1989, month=12, day=13)},
    {"name": "Ilona", "birthday": datetime(year=1990, month=11, day=14)},
    {"name": "Arina", "birthday": datetime(year=1991, month=11, day=13)},
    {"name": "Val", "birthday": datetime(year=1992, month=11, day=12)},
    {"name": "Mihey", "birthday": datetime(year=1993, month=11, day=29)},
    {"name": "Nick", "birthday": datetime(year=1994, month=11, day=15)},
    {"name": "Max", "birthday": datetime(year=1995, month=11, day=15)}
]

def get_birthdays_per_week(users):

    current_day = datetime.now()
    days_interval = define_days_interval(current_day)   # виклик функції - розрахунок поточного тижня
    new_time_line = current_day + days_interval

    user_list = {
        "Monday": [],
        "Tuesday": [],
        "Wednesday": [],
        "Thursday": [],
        "Friday": []
    }

    for user in users:
        new_date_for_user = datetime(
            year=current_day.year,
            month=user.get('birthday').month,
            day=user.get('birthday').day
        )
        if current_day < new_date_for_user <= new_time_line:
            weekday_string = new_date_for_user.strftime("%A")
            print(user)
            if weekday_string in ['Saturday', 'Sunday']:
                weekday_string = 'Monday'
            user_list.get(weekday_string).append(user.get('name'))

    print_users_list(user_list)


def define_days_interval(current_day: datetime) -> timedelta:

    if current_day.weekday() == 5:
        days_interval = timedelta(days=6)
    elif current_day.weekday() == 6:
        days_interval = timedelta(days=5)
    else:
        days_interval = timedelta(days=7)

    return days_interval

def print_users_list(user_list):
    for key, value in user_list.items():
        if value != False:
            print(f"{key}: {', '.join(value)}")


get_birthdays_per_week(list_birth)