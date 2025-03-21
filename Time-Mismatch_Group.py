from datetime import datetime, timedelta
import os

EXPECTED_SCHEDULE = [
    {
        "first_name": "Alma",
        "last_name": "Landaverde",
        "Schedule": {
            "Monday": ("9:00 AM", "1:00 PM"),
            "Tuesday": (None, None),
            "Wednesday": ("9:00 AM", "1:00 PM"),
            "Thursday": ("9:00 AM", "1:00 PM"),
            "Friday": (None, None)
        }
    },
    {
        "first_name": "MeherSuneel",
        "last_name": "Meesala",
        "Schedule": {
            "Monday": ("9:00 AM", "4:00 PM"),
            "Tuesday": (None, None),
            "Wednesday": ("9:00 AM", "4:00 PM"),
            "Thursday": (None, None),
            "Friday": ("9:00 AM", "4:00 PM")
        }
    }
]


# Your existing JSON body
json_body ={
  "response": "success",
  "employee": 0,
  "date_range_start": "2025-02-24 00:00:00",
  "date_range_end": "2025-02-28 22:00:00",
  "report_action": "generate_report",
  "shifts": {
    "response": "success",
    "shift_count": 9,
    "shift_total_time": "33:02",
    "wage_total": "0.00",
    "shift_array": [
      {
        "shift_id": 27492,
        "employee_clock_in_time": "February 26, 2025 9:00 am",
        "employee_clock_out_time": "February 26, 2025 1:00 pm",
        "first_name": "Alma",
        "last_name": "Landaverde",
        "shift_sum": "4:00"
      },
      {
        "shift_id": 27462,
        "employee_clock_in_time": "February 27, 2025 9:00 am",
        "employee_clock_out_time": "February 27, 2025 1:02 pm",
        "first_name": "Alma",
        "last_name": "Landaverde",
        "shift_sum": "4:02"
      },
      {
        "shift_id": 27436,
        "employee_clock_in_time": "February 24, 2025 9:00 am",
        "employee_clock_out_time": "February 24, 2025 1:00 pm",
        "first_name": "Alma",
        "last_name": "Landaverde",
        "shift_sum": "4:00"
      },
      {
        "shift_id": 27421,
        "employee_clock_in_time": "February 26, 2025 12:59 pm",
        "employee_clock_out_time": "February 26, 2025 12:59 pm",
        "first_name": "Alma",
        "last_name": "Landaverde",
        "shift_sum": "0:00"
      },
      {
        "shift_id": 27406,
        "employee_clock_in_time": "February 26, 2025 9:01 am",
        "employee_clock_out_time": None,
        "first_name": "Alma",
        "last_name": "Landaverde",
        "shift_sum": "00:00"
      },
      {
        "shift_id": 27309,
        "employee_clock_in_time": "February 24, 2025 11:29 pm",
        "employee_clock_out_time": "February 24, 2025 11:29 pm",
        "first_name": "Alma",
        "last_name": "Landaverde",
        "shift_sum": "0:00"
      },
      {
        "shift_id": 27779,
        "employee_clock_in_time": "February 28, 2025 9:00 am",
        "employee_clock_out_time": "February 28, 2025 4:00 pm",
        "first_name": "MeherSuneel",
        "last_name": "Meesala",
        "shift_sum": "7:00"
      },
      {
        "shift_id": 27460,
        "employee_clock_in_time": "February 27, 2025 9:00 am",
        "employee_clock_out_time": "February 27, 2025 4:00 pm",
        "first_name": "MeherSuneel",
        "last_name": "Meesala",
        "shift_sum": "7:00"
      },
      {
        "shift_id": 27398,
        "employee_clock_in_time": "February 26, 2025 9:00 am",
        "employee_clock_out_time": "February 26, 2025 4:00 pm",
        "first_name": "MeherSuneel",
        "last_name": "Meesala",
        "shift_sum": "7:00"
      }
    ]
  }
}# Helper function to calculate the time difference


def calculate_time_diff(start_time, end_time):
    time_diff = end_time - start_time
    hours, remainder = divmod(time_diff.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return hours, minutes, seconds

# Collect shifts data
shifts = json_body["shifts"]["shift_array"]
shift_dates = {datetime.strptime(shift["employee_clock_in_time"], "%B %d, %Y %I:%M %p").date(): shift for shift in shifts}

start_date = datetime.strptime(json_body["date_range_start"], "%Y-%m-%d %H:%M:%S")
print(start_date)
end_date = datetime.strptime(json_body["date_range_end"], "%Y-%m-%d %H:%M:%S")

# Create a dictionary to store results for each day
employee_reports = {}

# Loop through each day in the date range
# Loop through each day in the date range
# Loop through each day in the date range
current_day = start_date
while current_day <= end_date:
    day_name = current_day.strftime('%A')
    
    for employee in EXPECTED_SCHEDULE:
        expected_in, expected_out = employee["Schedule"].get(day_name, (None, None))

        if expected_in is not None and expected_out is not None:
            # Employee is scheduled
            shift_found = None
            for shift in shifts:
                shift_date = datetime.strptime(shift["employee_clock_in_time"], "%B %d, %Y %I:%M %p").date()
                if shift_date == current_day.date() and \
                   shift["first_name"] == employee["first_name"] and \
                   shift["last_name"] == employee["last_name"]:
                    shift_found = shift
                    break

            if not shift_found:
                # Didn't work on the expected day
                if current_day.date() not in employee_reports:
                    employee_reports[current_day.date()] = {}
                employee_reports[current_day.date()][f"{employee['first_name']} {employee['last_name']}"] = f"Didn't work on {day_name}, {current_day.strftime('%B %d, %Y')}."
            else:
                # Shift found but now check clock-in and clock-out individually
                clock_in_time = shift_found.get("employee_clock_in_time")
                clock_out_time = shift_found.get("employee_clock_out_time")

                if not clock_in_time:
                    if current_day.date() not in employee_reports:
                        employee_reports[current_day.date()] = {}
                    employee_reports[current_day.date()][f"{employee['first_name']} {employee['last_name']}"] = f"Didn't clock in on {day_name}, {current_day.strftime('%B %d, %Y')}."

                elif not clock_out_time:
                    if current_day.date() not in employee_reports:
                        employee_reports[current_day.date()] = {}
                    employee_reports[current_day.date()][f"{employee['first_name']} {employee['last_name']}"] = f"Didn't clock-out on {day_name}, {current_day.strftime('%B %d, %Y')}."

                else:
                    # Time mismatch check for clock-in and clock-out times
                    expected_in_time = datetime.strptime(f"{current_day.strftime('%Y-%m-%d')} {expected_in}", "%Y-%m-%d %I:%M %p")
                    expected_out_time = datetime.strptime(f"{current_day.strftime('%Y-%m-%d')} {expected_out}", "%Y-%m-%d %I:%M %p")

                    clock_in_time_obj = datetime.strptime(shift_found["employee_clock_in_time"], "%B %d, %Y %I:%M %p")
                    clock_out_time_obj = datetime.strptime(shift_found["employee_clock_out_time"], "%B %d, %Y %I:%M %p")

                    # Calculate time difference if any
                    if clock_in_time_obj != expected_in_time:
                        if clock_in_time_obj < expected_in_time:
                            time_diff = expected_in_time - clock_in_time_obj
                            hours, minutes, seconds = time_diff.seconds // 3600, (time_diff.seconds % 3600) // 60, (time_diff.seconds % 60)
                            if current_day.date() not in employee_reports:
                                employee_reports[current_day.date()] = {}
                            employee_reports[current_day.date()][f"{employee['first_name']} {employee['last_name']}"] = f"Time mismatch on {day_name} {current_day.strftime('%B %d, %Y')}: Clocked in early by {hours} hrs {minutes} mins {seconds} secs."
                        else:
                            time_diff = clock_in_time_obj - expected_in_time
                            hours, minutes, seconds = time_diff.seconds // 3600, (time_diff.seconds % 3600) // 60, (time_diff.seconds % 60)
                            if current_day.date() not in employee_reports:
                                employee_reports[current_day.date()] = {}
                            employee_reports[current_day.date()][f"{employee['first_name']} {employee['last_name']}"] = f"Time mismatch on {day_name} {current_day.strftime('%B %d, %Y')}: Clocked in late by {hours} hrs {minutes} mins {seconds} secs."

                    if clock_out_time_obj != expected_out_time:
                        if clock_out_time_obj < expected_out_time:
                            time_diff = expected_out_time - clock_out_time_obj
                            hours, minutes, seconds = time_diff.seconds // 3600, (time_diff.seconds % 3600) // 60, (time_diff.seconds % 60)
                            if current_day.date() not in employee_reports:
                                employee_reports[current_day.date()] = {}
                            employee_reports[current_day.date()][f"{employee['first_name']} {employee['last_name']}"] = f"Time mismatch on {day_name} {current_day.strftime('%B %d, %Y')}: Clocked out early by {hours} hrs {minutes} mins {seconds} secs."
                        else:
                            time_diff = clock_out_time_obj - expected_out_time
                            hours, minutes, seconds = time_diff.seconds // 3600, (time_diff.seconds % 3600) // 60, (time_diff.seconds % 60)
                            if current_day.date() not in employee_reports:
                                employee_reports[current_day.date()] = {}
                            employee_reports[current_day.date()][f"{employee['first_name']} {employee['last_name']}"] = f"Time mismatch on {day_name} {current_day.strftime('%B %d, %Y')}: Clocked out late by {hours} hrs {minutes} mins {seconds} secs."

        else:
            # Not scheduled, check if worked
            for shift in shifts:
                shift_date = datetime.strptime(shift["employee_clock_in_time"], "%B %d, %Y %I:%M %p").date()
                if shift_date == current_day.date() and \
                   shift["first_name"] == employee["first_name"] and \
                   shift["last_name"] == employee["last_name"]:
                    clock_in_time = shift.get("employee_clock_in_time")
                    clock_out_time = shift.get("employee_clock_out_time")
                    worked_hours, worked_minutes = map(int, shift['shift_sum'].split(":"))
                    if current_day.date() not in employee_reports:
                        employee_reports[current_day.date()] = {}
                    employee_reports[current_day.date()][f"{employee['first_name']} {employee['last_name']}"] = f"Worked on {day_name}, {current_day.strftime('%B %d, %Y')} when not scheduled. Worked {worked_hours} hrs {worked_minutes} mins."

    current_day += timedelta(days=1)

# Output reports
for date, reports in employee_reports.items():
    for employee, report in reports.items():
        print(report)
print(employee_reports)
# Now, generate the HTML table (unchanged)
# Initialize the HTML table
#start_date = datetime.strptime(start_date, "%Y-%m-%d %H:%M:%S")
#date_tuple = (start_date.year, start_date.month, start_date.day)
#print(date_tuple)
start_date = datetime(start_date.year, start_date.month, start_date.day)
print(start_date)
# Initialize the HTML table
# Initialize the HTML table with embedded CSS styles
start_date_str = start_date.strftime('%B %d, %Y')  # Example: "March 21, 2025"
end_date_str = end_date.strftime('%B %d, %Y')      # Example: "March 25, 2025"
print(start_date_str)
print(type(start_date))
print(end_date_str)
print(type(end_date))
html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Employee Report</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            color: #333;
            padding: 20px;
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }}
        th, td {{
            padding: 12px;
            text-align: center;
            border: 1px solid #ddd;
        }}
        th {{
            background-color: #000000;
            color: white;
        }}
        tr:nth-child(even) {{
            background-color: #f2f2f2;
        }}
        tr:nth-child(odd) {{
            background-color: #fff;
        }}
        td {{
            background-color: #f9f9f9;
        }}
        td.error {{
            background-color: #f44336; /* Red for errors */
            color: white;
        }}
        td.no-mismatch {{
            background-color: #4CAF50; /* Green for no issues */
            color: white;
        }}
        td.not-scheduled {{
            background-color: #333; /* Black for not scheduled */
            color: white;
        }}
        td.mismatch {{
            background-color: #FF9800; /* Orange for mismatch */
            color: white;
        }}
    </style>
</head>
<body>
<h1>Employee Report {start_date_str} - {end_date_str}</h1>

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Monday</th>
            <th>Tuesday</th>
            <th>Wednesday</th>
            <th>Thursday</th>
            <th>Friday</th>
        </tr>
    </thead>
    <tbody>
"""
# Generate the HTML table rows with styles
for employee in EXPECTED_SCHEDULE:
    employee_name = f"{employee['first_name']} {employee['last_name']}"
    
    # Start the row for the employee
    html += f"<tr><td>{employee_name}</td>"
    
    for day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
        # Calculate the date for the current weekday based on start_date
        date_key = start_date
        while date_key.strftime('%A') != day:
            date_key += timedelta(days=1)
        
        date = date_key.date()  # Convert to datetime.date
        
        # Check if the report exists for the employee on that specific day
        if employee_name in employee_reports.get(date, {}):
            report = employee_reports[date][employee_name]
            if "Didn't work" in report:
                html += f"<td class='error'>{report}</td>"
            elif "Worked on" in report:
                html += f"<td class='error'>{report}</td>"
            elif "Clocked in early" in report or "Clocked in late" in report:
                html += f"<td class='mismatch'>{report}</td>"
            elif "Clocked-out early" in report or "Clocked-out late" in report:
                html += f"<td class='mismatch'>{report}</td>"
            else:
                html += f"<td class='error'>{report}</td>"
        else:
            # Default case when there is no report for a scheduled day
            if employee['Schedule'][day] is None:
                # This cell is for a day when the employee is not scheduled, so black background
                html += "<td class='not-scheduled'></td>"
            else:
                # This is a scheduled day with no issues, so green background
                html += "<td class='no-mismatch'>No Mismatch</td>"
    html += "</tr>"

html += "</tbody></table></body></html>"

# Print the HTML table to console
print(html)

# Save the HTML table to a file
with open('employee_report.html', 'w') as file:
    file.write(html)