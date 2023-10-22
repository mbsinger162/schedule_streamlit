import csv
from collections import defaultdict
from datetime import datetime
from dateutil.parser import parse

def is_weekend(date_str):
    date_obj = parse(date_str)
    return date_obj.weekday() >= 5

def is_weekday(date_str):
    date_obj = parse(date_str)
    return date_obj.weekday() <= 3

def main(schedule_csv_path, EXCLUDED_DATES_FILENAME, DOCTOR_DATA_FILENAME):
    with open(EXCLUDED_DATES_FILENAME, "r") as f:
        excluded_dates = set(line.strip() for line in f)

    # Read the doctor_data.csv file
    with open(DOCTOR_DATA_FILENAME, "r") as f:
        reader = csv.reader(f)
        doctor_ids = next(reader)  # Read header row with doctor IDs
        doctor_unavailable_dates = defaultdict(set)

        for row in reader:
            for i, date in enumerate(row):
                if date:
                    doctor_unavailable_dates[doctor_ids[i]].add(date)

    # Read and validate the schedule.csv file
    weekday_counts = defaultdict(int)
    weekend_counts = defaultdict(int)
    errors_found = False

    with open("schedule.csv", "r") as f:
        reader = csv.reader(f)
        next(reader)  # Skip header row

        saturday_counts = defaultdict(int)
        sunday_counts = defaultdict(int)

        for row in reader:
            date, doctor_id = row
            date_obj = datetime.strptime(date, "%Y-%m-%d")

            # Check if the date is in the excluded_dates list
            if date in excluded_dates:
                print(f"Error: Date {date} is in excluded_dates.csv but is assigned to doctor {doctor_id}.")
                errors_found = True

            # Check if the doctor is unavailable on the assigned date
            if date in doctor_unavailable_dates[doctor_id]:
                print(f"Error: Doctor {doctor_id} is assigned on {date}, but they are unavailable.")
                errors_found = True

            # Count weekdays, Saturdays, and Sundays for each doctor
            # if is_weekend(date_obj):
            if date_obj.weekday() == 5:  # Saturday
                saturday_counts[doctor_id] += 1
            if date_obj.weekday() == 6:  # Sunday
                sunday_counts[doctor_id] += 1
            if date_obj.weekday() <= 3:  # Weekday
                weekday_counts[doctor_id] += 1  


    if not errors_found:
        validation_results = "No errors found in the schedule!"
        weekday_results = {f"Doctor {doctor_id}": count for doctor_id, count in weekday_counts.items()}
        saturday_results = {f"Doctor {doctor_id}": count for doctor_id, count in saturday_counts.items()}
        sunday_results = {f"Doctor {doctor_id}": count for doctor_id, count in sunday_counts.items()}

    results = {
        "validation_results": validation_results,
        "weekday_counts": weekday_results,
        "saturday_counts": saturday_results,
        "sunday_counts": sunday_results
    }

    return results





