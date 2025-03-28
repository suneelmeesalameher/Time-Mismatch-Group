# Time-Mismatch-Group
# Employee Schedule Processing Script

## Overview

This Python script processes an employee schedule CSV file, extracts shift details, formats time values, and converts the data into a structured JSON format. The script handles scheduling for **one week at a time** and replaces any `null` values with `None` in the final JSON output. The script is designed to be easily extensible and modifiable based on your specific needs.

## Features

- **CSV Parsing**: Reads employee schedule data from a CSV file.
- **Time Formatting**: Converts times from the format `HH:MM:SS AM/PM` to `HH:MM AM/PM` and removes seconds.
- **Null Handling**: Replaces any `null` values with `None` in the output JSON.
- **Weekly Schedule**: The script processes shift data for one week (Monday to Friday) per employee.

## Dependencies

The script requires the following Python libraries:

- `pandas`: For reading and manipulating the CSV data.
- `datetime`: For time formatting and manipulation.

### Installation

To install the required dependencies, you can use the following command:

    ```bash
    pip install pandas
    ```





## Script Overview

### 1. `format_time(time_str)`

This function takes a time string in the format `HH:MM:SS AM/PM`, parses it into a `datetime` object, and returns the formatted time as `HH:MM AM/PM`. If the time is missing or in an unexpected format, it returns `None`.

**Example Input/Output:**

- **Input**: `"9:00:00 AM"`
- **Output**: `"9:00 AM"`

### 2. Reading Employee Data

The script reads a CSV file named **"Employee Schedule (Responses) - Form Responses 1.csv"**. This CSV is expected to contain columns for:
- **First Name**
- **Last Name**
- **Monday to Friday Shift Start and End Times**

### 3. Processing and Formatting the Schedule

The script iterates through each row (employee). 

- For each employee, it formats the start and end times for each day from Monday to Friday.
- The formatted times are stored in a structured dictionary, which is appended to the `EXPECTED_SCHEDULE` list.
### 4. `calculate_time_diff(start_time, end_time)`

This function calculates the time difference between the start and end times. It returns the difference in hours, minutes, and seconds.

**Example Input/Output:**

- **Input**: `start_time = 9:00:00 AM`, `end_time = 5:00:00 PM`
- **Output**: `8 hours 0 minutes 0 seconds`

### 5. Reading Shift Data

The script reads the employee shift data from a JSON structure. It extracts:
- **Shifts Array**: A list of shifts containing details like employee clock-in and clock-out times.
- **Date Range**: The start and end dates of the period for which reports need to be generated.

### 6. Checking Employee Attendance and Reporting

For each day in the date range, the script:
- Compares the expected shift times with the clock-in and clock-out times for each employee.
- If an employee was scheduled but didn’t work or didn’t clock in/out, it flags that in the report.
- If there was a time mismatch (e.g., clocking in early/late or clocking out early/late), the script calculates the time difference and adds that to the report.

The output includes a report of any issues, such as:
- **Unscheduled Work**: Employees worked on days they weren’t scheduled.
- **Missed Shifts**: Employees didn’t work when scheduled.
- **Missing Clock-In/Clock-Out**: Employees didn’t clock in or clock out.
- **Time Mismatches**: Employees clocked in or out at unexpected times.

### 7. Generating HTML Report

After processing the data, the script generates an HTML table displaying the following:
- **Employee Name**
- **Attendance and Time Mismatches for each Day (Monday - Friday)**

Each cell in the table is color-coded based on the report:
- **Red**: Errors (e.g., missed clock-ins, clock-outs, etc.)
- **Orange**: Time mismatches
- **Green**: No issues (employees worked as scheduled)
- **Black**: Not scheduled to work on a particular day
