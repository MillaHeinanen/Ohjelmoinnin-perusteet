# library.py
MONTHS: list[str] = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

WEEKDAYS: list[str] = [
    "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"
]

def count_by_year(timestamps: list[str], year: str) -> int:
    return sum(1 for ts in timestamps if ts.startswith(year))

def count_by_month(timestamps: list[str], month: str) -> int:
    from datetime import datetime
    month_index = MONTHS.index(month) + 1
    return sum(1 for ts in timestamps if datetime.fromisoformat(ts).month == month_index)

def count_by_weekday(timestamps: list[str], weekday: str) -> int:
    from datetime import datetime
    weekday_index = WEEKDAYS.index(weekday)
    return sum(1 for ts in timestamps if datetime.fromisoformat(ts).weekday() == weekday_index)