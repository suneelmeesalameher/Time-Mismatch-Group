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
