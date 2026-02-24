from datetime import datetime

# Get the current time in Utah's timezone and have it as a function 
def current_time():
    # Return current time in Utah (Mountain Time) with timezone name.
    current_time = datetime.now()

    year = current_time.year
    month = current_time.month
    day = current_time.day

    date = f"{year}-{month}-{day}"

    hour = current_time.hour
    minute = current_time.minute
    second = current_time.second

    time = f"{hour}:{minute}:{second}"
   
    date_time = f"Last updated: {date} {time}"


    return date_time