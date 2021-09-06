# Standard Python libraries
from calendar import monthrange
from datetime import date
from datetime import datetime
import sys


def check_if_start_before_end(start: date, end: date) -> None:
    """Validates if start date is before end date."""
    if start > end:
        print("Start date can't be after end date.")
        sys.exit()


def convert_end_date(end_date: date) -> date:
    """Returns modified date e.g. 2020-02-01 -> 2020-02-29."""
    num_days = last_day_of_month(end_date)
    end_date = end_date.replace(day=num_days)
    return end_date


def date_pattern(input_date: str, format_="%Y-%m-%d") -> date:
    """Validates input date and converts to date object."""
    try:
        converted_date = datetime.strptime(input_date, format_)
    except ValueError:
        print("Invalid date pattern")
        sys.exit()
    else:
        return converted_date.date()


def last_day_of_month(end_date: date) -> int:
    """Returns number of days in month for given year and month."""
    num_days = monthrange(end_date.year, end_date.month)[1]
    return num_days


def limit_validation(start_date: date, end_date: date) -> None:
    """Coinpaprika API allows to fetch max 366 result rows in one request."""
    num_days = end_date - start_date
    if num_days.days > 366:
        print("You can fetch max 366 rows in one request. Change date range.")
        sys.exit()


def main():
    pass


if __name__ == "__main__":
    main()
