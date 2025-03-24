import pandas as pd
from datetime import datetime
def format_time(time_str):
    try:
        # Parse the time string to a datetime object
        time_obj = datetime.strptime(time_str, '%I:%M:%S %p')
        # Return the time formatted without seconds
        return time_obj.strftime('%I:%M %p')
    except ValueError:
        # If the time is NaN or not in the expected format, return None
        return None
    
    
# Load the data from Google Sheets (exported as CSV or via API)
data = pd.read_csv('Employee Schedule (Responses) - Form Responses 1.csv')

EXPECTED_SCHEDULE = []

# Iterate through each row of the data
for index, row in data.iterrows():
    schedule = {}
    
    # Iterate through the days of the week and assign shift start and end times
    for day in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']:
        # Format the start and end times, replacing NaN with None
        start_time = format_time(row[f'{day} Shift Start']) if pd.notna(row[f'{day} Shift Start']) else None
        end_time = format_time(row[f'{day} Shift End']) if pd.notna(row[f'{day} Shift End']) else None
        
        schedule[day] = (start_time, end_time)
    
    # Append the formatted data for each employee
    EXPECTED_SCHEDULE.append({
        "first_name": row['First Name'],
        "last_name": row['Last Name'],
        "Schedule": schedule
    })

# Print the formatted schedule
print(EXPECTED_SCHEDULE)