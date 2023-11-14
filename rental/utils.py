import datetime
import math


def calculate_rental_sum(start_date: datetime.datetime, end_date: datetime.datetime, price_per_hour: float):
    """Calculate the total price of a rental."""
    duration = end_date - start_date
    hours_counted = math.ceil(duration.total_seconds() / 3600)
    return hours_counted * price_per_hour, hours_counted
