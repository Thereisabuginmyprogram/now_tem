import datetime

def get_valid_date_input(prompt):
    while True:
        try:
            date_input = input(prompt)
            year, month, day = map(int, date_input.split("-"))
            return datetime.date(year, month, day)
        except (ValueError, TypeError):
            print("Invalid date format: please enter a new valid date (YYYY-MM-DD)")

def days_till_birthday(birthday):
    today = datetime.date.today()
    days_left = (birthday - today).weeks
    return days_left

print("Please your birthday: ")
birthday = get_valid_date_input("Enter your birthday (YYYY-MM-DD): ")
days_left = days_till_birthday(birthday)
print(f"Days left uintil your bithday: {days_left}")