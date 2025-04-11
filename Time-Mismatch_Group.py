from datetime import datetime, timedelta
from collections import defaultdict
from Get_details_from_csv import EXPECTED_SCHEDULE
import os
import json
#from dotenv import load_dotenv

#load_dotenv()
# Get JSON string from .env
#json_body_str = os.getenv("JSON_BODY")

# Convert string to Python dictionary
#json_body = json.loads(json_body_str)
json_body = {
  "response": "success",
  "employee": 0,
  "date_range_start": "2025-03-31 00:00:00",
  "date_range_end": "2025-04-04 22:00:00",
  "report_action": "generate_report",
  "shifts": {
    "response": "success",
    "shift_count": 122,
    "shift_total_time": "517:38",
    "wage_total": "0.00",
    "shift_array": [
      {
        "shift_id": 28656,
        "employee_clock_in_time": "April 4, 2025 9:00 am",
        "employee_clock_out_time": "April 4, 2025 4:00 pm",
        "first_name": "Neelima",
        "last_name": "Palleboina",
        "shift_sum": "7:00"
      },
      {
        "shift_id": 28526,
        "employee_clock_in_time": "April 4, 2025 5:55 pm",
        "employee_clock_out_time": "April 4, 2025 5:55 pm",
        "first_name": "Nitant",
        "last_name": "Jatale",
        "shift_sum": "0:00"
      },
      {
        "shift_id": 28525,
        "employee_clock_in_time": "April 4, 2025 5:11 pm",
        "employee_clock_out_time": "April 4, 2025 5:11 pm",
        "first_name": "Sarah",
        "last_name": "Patil",
        "shift_sum": "0:00"
      },
      {
        "shift_id": 28524,
        "employee_clock_in_time": "April 4, 2025 1:41 pm",
        "employee_clock_out_time": "April 4, 2025 5:56 pm",
        "first_name": "Sai",
        "last_name": "Shivani",
        "shift_sum": "4:15"
      },
      {
        "shift_id": 28523,
        "employee_clock_in_time": "April 4, 2025 12:06 pm",
        "employee_clock_out_time": "April 4, 2025 4:20 pm",
        "first_name": "Poliana",
        "last_name": "Santana",
        "shift_sum": "4:13"
      },
      {
        "shift_id": 28522,
        "employee_clock_in_time": "April 4, 2025 12:01 pm",
        "employee_clock_out_time": "April 4, 2025 5:01 pm",
        "first_name": "Nigama",
        "last_name": "Dendukuri",
        "shift_sum": "5:00"
      },
      {
        "shift_id": 28521,
        "employee_clock_in_time": "April 4, 2025 12:00 pm",
        "employee_clock_out_time": "April 4, 2025 4:33 pm",
        "first_name": "Almatou",
        "last_name": "SARE",
        "shift_sum": "4:33"
      },
      {
        "shift_id": 28520,
        "employee_clock_in_time": "April 4, 2025 11:59 am",
        "employee_clock_out_time": "April 4, 2025 7:02 pm",
        "first_name": "Smita",
        "last_name": "Aghav",
        "shift_sum": "7:02"
      },
      {
        "shift_id": 28519,
        "employee_clock_in_time": "April 4, 2025 11:54 am",
        "employee_clock_out_time": None,
        "first_name": "Shubhika",
        "last_name": "Gupta",
        "shift_sum": "00:00"
      },
      {
        "shift_id": 28518,
        "employee_clock_in_time": "April 4, 2025 11:05 am",
        "employee_clock_out_time": "April 4, 2025 4:49 pm",
        "first_name": "Savana",
        "last_name": "Patel",
        "shift_sum": "5:43"
      },
      {
        "shift_id": 28517,
        "employee_clock_in_time": "April 4, 2025 10:58 am",
        "employee_clock_out_time": "April 4, 2025 6:46 pm",
        "first_name": "Jisha",
        "last_name": "Sheelakumar",
        "shift_sum": "7:47"
      },
      {
        "shift_id": 28516,
        "employee_clock_in_time": "April 4, 2025 10:58 am",
        "employee_clock_out_time": "April 4, 2025 5:00 pm",
        "first_name": "Chandrashakar",
        "last_name": "Gudipally",
        "shift_sum": "6:02"
      },
      {
        "shift_id": 28515,
        "employee_clock_in_time": "April 4, 2025 10:22 am",
        "employee_clock_out_time": None,
        "first_name": "Nitant",
        "last_name": "Jatale",
        "shift_sum": "00:00"
      },
      {
        "shift_id": 28514,
        "employee_clock_in_time": "April 4, 2025 9:59 am",
        "employee_clock_out_time": "April 4, 2025 4:16 pm",
        "first_name": "Imani",
        "last_name": "Thomas",
        "shift_sum": "6:16"
      },
      {
        "shift_id": 28513,
        "employee_clock_in_time": "April 4, 2025 9:13 am",
        "employee_clock_out_time": None,
        "first_name": "Sarah",
        "last_name": "Patil",
        "shift_sum": "00:00"
      },
      {
        "shift_id": 28512,
        "employee_clock_in_time": "April 4, 2025 9:00 am",
        "employee_clock_out_time": "April 4, 2025 4:00 pm",
        "first_name": "MeherSuneel",
        "last_name": "Meesala",
        "shift_sum": "7:00"
      },
      {
        "shift_id": 28511,
        "employee_clock_in_time": "April 4, 2025 9:00 am",
        "employee_clock_out_time": "April 4, 2025 1:02 pm",
        "first_name": "Samyukta",
        "last_name": "Padmanabhuni",
        "shift_sum": "4:02"
      },
      {
        "shift_id": 28510,
        "employee_clock_in_time": "April 4, 2025 8:00 am",
        "employee_clock_out_time": "April 4, 2025 1:00 pm",
        "first_name": "Sree Lakshmi",
        "last_name": "Akella",
        "shift_sum": "5:00"
      },
      {
        "shift_id": 28504,
        "employee_clock_in_time": "April 3, 2025 3:03 pm",
        "employee_clock_out_time": "April 3, 2025 3:03 pm",
        "first_name": "McKenzie",
        "last_name": "Lynn Kovach",
        "shift_sum": "0:00"
      },
      {
        "shift_id": 28497,
        "employee_clock_in_time": "April 3, 2025 12:18 pm",
        "employee_clock_out_time": None,
        "first_name": "Ayush",
        "last_name": "Kattupalli",
        "shift_sum": "00:00"
      },
      {
        "shift_id": 28496,
        "employee_clock_in_time": "April 3, 2025 12:17 pm",
        "employee_clock_out_time": "April 3, 2025 5:19 pm",
        "first_name": "Sai Venkata",
        "last_name": "Dhanush Amirinenii",
        "shift_sum": "5:02"
      },
      {
        "shift_id": 28494,
        "employee_clock_in_time": "April 3, 2025 12:00 pm",
        "employee_clock_out_time": "April 3, 2025 4:00 pm",
        "first_name": "Poliana",
        "last_name": "Santana",
        "shift_sum": "3:59"
      },
      {
        "shift_id": 28492,
        "employee_clock_in_time": "April 3, 2025 10:03 am",
        "employee_clock_out_time": "April 3, 2025 2:03 pm",
        "first_name": "Imani",
        "last_name": "Thomas",
        "shift_sum": "3:59"
      },
      {
        "shift_id": 28491,
        "employee_clock_in_time": "April 3, 2025 10:00 am",
        "employee_clock_out_time": "April 3, 2025 3:01 pm",
        "first_name": "Sanath",
        "last_name": "Desai",
        "shift_sum": "5:00"
      },
      {
        "shift_id": 28490,
        "employee_clock_in_time": "April 3, 2025 10:00 am",
        "employee_clock_out_time": "April 3, 2025 5:03 pm",
        "first_name": "Nithish Reddy",
        "last_name": "Mannem",
        "shift_sum": "7:02"
      },
      {
        "shift_id": 28489,
        "employee_clock_in_time": "April 3, 2025 9:54 am",
        "employee_clock_out_time": "April 3, 2025 6:01 pm",
        "first_name": "Sai",
        "last_name": "Shivani",
        "shift_sum": "8:06"
      },
      {
        "shift_id": 28488,
        "employee_clock_in_time": "April 3, 2025 9:08 am",
        "employee_clock_out_time": "April 3, 2025 4:14 pm",
        "first_name": "Hepsiba Grace",
        "last_name": "Boddu",
        "shift_sum": "7:05"
      },
      {
        "shift_id": 28487,
        "employee_clock_in_time": "April 3, 2025 9:05 am",
        "employee_clock_out_time": "April 3, 2025 5:07 pm",
        "first_name": "Samyukta",
        "last_name": "Padmanabhuni",
        "shift_sum": "8:01"
      },
      {
        "shift_id": 28486,
        "employee_clock_in_time": "April 3, 2025 9:00 am",
        "employee_clock_out_time": "April 3, 2025 4:00 pm",
        "first_name": "Neelima",
        "last_name": "Palleboina",
        "shift_sum": "7:00"
      },
      {
        "shift_id": 28485,
        "employee_clock_in_time": "April 3, 2025 9:01 am",
        "employee_clock_out_time": "April 3, 2025 2:01 pm",
        "first_name": "Haren",
        "last_name": "Akula",
        "shift_sum": "5:00"
      },
      {
        "shift_id": 28484,
        "employee_clock_in_time": "April 3, 2025 8:56 am",
        "employee_clock_out_time": "April 3, 2025 2:06 pm",
        "first_name": "",
        "last_name": "",
        "shift_sum": "5:10"
      },
      {
        "shift_id": 28483,
        "employee_clock_in_time": "April 3, 2025 8:55 am",
        "employee_clock_out_time": None,
        "first_name": "Aanu",
        "last_name": "Adewusi",
        "shift_sum": "00:00"
      },
      {
        "shift_id": 28482,
        "employee_clock_in_time": "April 3, 2025 8:46 am",
        "employee_clock_out_time": "April 3, 2025 2:47 pm",
        "first_name": "Prateeksha",
        "last_name": "Gawande",
        "shift_sum": "6:00"
      },
      {
        "shift_id": 28481,
        "employee_clock_in_time": "April 3, 2025 8:00 am",
        "employee_clock_out_time": "April 3, 2025 1:02 pm",
        "first_name": "Sree Lakshmi",
        "last_name": "Akella",
        "shift_sum": "5:02"
      },
      {
        "shift_id": 28480,
        "employee_clock_in_time": "April 2, 2025 5:16 pm",
        "employee_clock_out_time": "April 2, 2025 5:16 pm",
        "first_name": "Nitant",
        "last_name": "Jatale",
        "shift_sum": "0:00"
      },
      {
        "shift_id": 28479,
        "employee_clock_in_time": "April 2, 2025 4:01 pm",
        "employee_clock_out_time": "April 2, 2025 7:02 pm",
        "first_name": "Jessica",
        "last_name": "Vigil",
        "shift_sum": "3:01"
      },
      {
        "shift_id": 28476,
        "employee_clock_in_time": "April 1, 2025 9:00 am",
        "employee_clock_out_time": "April 1, 2025 4:00 pm",
        "first_name": "Rakshitha Reddy",
        "last_name": "Potu",
        "shift_sum": "7:00"
      },
      {
        "shift_id": 28475,
        "employee_clock_in_time": "March 31, 2025 7:00 am",
        "employee_clock_out_time": "March 31, 2025 9:00 pm",
        "first_name": "Aanu",
        "last_name": "Adewusi",
        "shift_sum": "14:00"
      },
      {
        "shift_id": 28474,
        "employee_clock_in_time": "April 1, 2025 8:36 am",
        "employee_clock_out_time": "April 1, 2025 3:36 pm",
        "first_name": "Prateeksha",
        "last_name": "Gawande",
        "shift_sum": "7:00"
      },
      {
        "shift_id": 28473,
        "employee_clock_in_time": "April 1, 2025 9:00 am",
        "employee_clock_out_time": "April 1, 2025 2:00 pm",
        "first_name": "Haren",
        "last_name": "Akula",
        "shift_sum": "5:00"
      },
      {
        "shift_id": 28472,
        "employee_clock_in_time": "March 31, 2025 12:00 pm",
        "employee_clock_out_time": "March 31, 2025 5:00 pm",
        "first_name": "Ayush",
        "last_name": "Kattupalli",
        "shift_sum": "5:00"
      },
      {
        "shift_id": 28471,
        "employee_clock_in_time": "March 31, 2025 11:00 am",
        "employee_clock_out_time": "March 31, 2025 6:00 pm",
        "first_name": "Kalind",
        "last_name": "Joshi",
        "shift_sum": "7:00"
      },
      {
        "shift_id": 28468,
        "employee_clock_in_time": "April 2, 2025 3:00 pm",
        "employee_clock_out_time": None,
        "first_name": "Shreya",
        "last_name": "Edulakanti",
        "shift_sum": "00:00"
      },
      {
        "shift_id": 28466,
        "employee_clock_in_time": "April 2, 2025 2:02 pm",
        "employee_clock_out_time": None,
        "first_name": "",
        "last_name": "",
        "shift_sum": "00:00"
      },
      {
        "shift_id": 28465,
        "employee_clock_in_time": "April 2, 2025 1:02 pm",
        "employee_clock_out_time": "April 2, 2025 6:00 pm",
        "first_name": "Sree Lakshmi",
        "last_name": "Akella",
        "shift_sum": "4:58"
      },
      {
        "shift_id": 28464,
        "employee_clock_in_time": "April 2, 2025 12:05 pm",
        "employee_clock_out_time": "April 2, 2025 5:36 pm",
        "first_name": "Ayush",
        "last_name": "Kattupalli",
        "shift_sum": "5:31"
      },
      {
        "shift_id": 28463,
        "employee_clock_in_time": "April 2, 2025 12:04 pm",
        "employee_clock_out_time": "April 2, 2025 4:04 pm",
        "first_name": "Poliana",
        "last_name": "Santana",
        "shift_sum": "3:59"
      },
      {
        "shift_id": 28462,
        "employee_clock_in_time": "April 2, 2025 12:00 pm",
        "employee_clock_out_time": "April 2, 2025 7:44 pm",
        "first_name": "Nigama",
        "last_name": "Dendukuri",
        "shift_sum": "7:43"
      },
      {
        "shift_id": 28461,
        "employee_clock_in_time": "April 2, 2025 11:59 am",
        "employee_clock_out_time": "April 2, 2025 7:00 pm",
        "first_name": "Smita",
        "last_name": "Aghav",
        "shift_sum": "7:00"
      },
      {
        "shift_id": 28460,
        "employee_clock_in_time": "April 2, 2025 11:06 am",
        "employee_clock_out_time": None,
        "first_name": "Kalind",
        "last_name": "Joshi",
        "shift_sum": "00:00"
      },
      {
        "shift_id": 28459,
        "employee_clock_in_time": "April 2, 2025 11:05 am",
        "employee_clock_out_time": None,
        "first_name": "Adarsh",
        "last_name": "Devineni",
        "shift_sum": "00:00"
      },
      {
        "shift_id": 28458,
        "employee_clock_in_time": "April 2, 2025 11:05 am",
        "employee_clock_out_time": "April 2, 2025 5:20 pm",
        "first_name": "Savana",
        "last_name": "Patel",
        "shift_sum": "6:15"
      },
      {
        "shift_id": 28457,
        "employee_clock_in_time": "April 2, 2025 11:00 am",
        "employee_clock_out_time": "April 2, 2025 6:06 pm",
        "first_name": "Jisha",
        "last_name": "Sheelakumar",
        "shift_sum": "7:06"
      },
      {
        "shift_id": 28456,
        "employee_clock_in_time": "April 2, 2025 10:55 am",
        "employee_clock_out_time": "April 2, 2025 3:53 pm",
        "first_name": "Sai Venkata",
        "last_name": "Dhanush Amirinenii",
        "shift_sum": "4:57"
      },
      {
        "shift_id": 28455,
        "employee_clock_in_time": "April 2, 2025 10:44 am",
        "employee_clock_out_time": None,
        "first_name": "Nitant",
        "last_name": "Jatale",
        "shift_sum": "00:00"
      },
      {
        "shift_id": 28454,
        "employee_clock_in_time": "April 2, 2025 10:26 am",
        "employee_clock_out_time": None,
        "first_name": "Sai Swethan",
        "last_name": "Durganala",
        "shift_sum": "00:00"
      },
      {
        "shift_id": 28453,
        "employee_clock_in_time": "April 2, 2025 10:00 am",
        "employee_clock_out_time": "April 2, 2025 3:05 pm",
        "first_name": "Sanath",
        "last_name": "Desai",
        "shift_sum": "5:04"
      },
      {
        "shift_id": 28452,
        "employee_clock_in_time": "April 2, 2025 10:00 am",
        "employee_clock_out_time": None,
        "first_name": "Nithish Reddy",
        "last_name": "Mannem",
        "shift_sum": "00:00"
      },
      {
        "shift_id": 28451,
        "employee_clock_in_time": "April 2, 2025 9:57 am",
        "employee_clock_out_time": "April 2, 2025 1:00 pm",
        "first_name": "valerie",
        "last_name": "Osaweedoh",
        "shift_sum": "3:02"
      },
      {
        "shift_id": 28450,
        "employee_clock_in_time": "April 2, 2025 9:30 am",
        "employee_clock_out_time": "April 2, 2025 2:17 pm",
        "first_name": "Ru",
        "last_name": "Chen",
        "shift_sum": "4:47"
      },
      {
        "shift_id": 28449,
        "employee_clock_in_time": "April 2, 2025 9:09 am",
        "employee_clock_out_time": "April 2, 2025 4:11 pm",
        "first_name": "Hepsiba Grace",
        "last_name": "Boddu",
        "shift_sum": "7:02"
      },
      {
        "shift_id": 28448,
        "employee_clock_in_time": "April 2, 2025 9:03 am",
        "employee_clock_out_time": "April 2, 2025 5:07 pm",
        "first_name": "Samyukta",
        "last_name": "Padmanabhuni",
        "shift_sum": "8:03"
      },
      {
        "shift_id": 28447,
        "employee_clock_in_time": "April 2, 2025 9:00 am",
        "employee_clock_out_time": "April 2, 2025 4:01 pm",
        "first_name": "MeherSuneel",
        "last_name": "Meesala",
        "shift_sum": "7:01"
      },
      {
        "shift_id": 28446,
        "employee_clock_in_time": "April 2, 2025 8:59 am",
        "employee_clock_out_time": "April 2, 2025 4:05 pm",
        "first_name": "Rakshitha Reddy",
        "last_name": "Potu",
        "shift_sum": "7:06"
      },
      {
        "shift_id": 28445,
        "employee_clock_in_time": "April 2, 2025 8:59 am",
        "employee_clock_out_time": "April 2, 2025 1:59 pm",
        "first_name": "Haren",
        "last_name": "Akula",
        "shift_sum": "5:00"
      },
      {
        "shift_id": 28444,
        "employee_clock_in_time": "April 2, 2025 8:45 am",
        "employee_clock_out_time": None,
        "first_name": "Aanu",
        "last_name": "Adewusi",
        "shift_sum": "00:00"
      },
      {
        "shift_id": 28443,
        "employee_clock_in_time": "April 2, 2025 8:34 am",
        "employee_clock_out_time": "April 2, 2025 3:39 pm",
        "first_name": "Prateeksha",
        "last_name": "Gawande",
        "shift_sum": "7:04"
      },
      {
        "shift_id": 28442,
        "employee_clock_in_time": "April 1, 2025 7:08 pm",
        "employee_clock_out_time": "April 1, 2025 7:08 pm",
        "first_name": "Jonathan.",
        "last_name": "Almeida",
        "shift_sum": "0:00"
      },
      {
        "shift_id": 28441,
        "employee_clock_in_time": "April 1, 2025 3:34 pm",
        "employee_clock_out_time": "April 1, 2025 5:22 pm",
        "first_name": "Nigama",
        "last_name": "Dendukuri",
        "shift_sum": "1:47"
      },
      {
        "shift_id": 28440,
        "employee_clock_in_time": "April 1, 2025 3:06 pm",
        "employee_clock_out_time": None,
        "first_name": "Sanath",
        "last_name": "Desai",
        "shift_sum": "00:00"
      },
      {
        "shift_id": 28439,
        "employee_clock_in_time": "April 1, 2025 3:00 pm",
        "employee_clock_out_time": "April 1, 2025 3:01 pm",
        "first_name": "Sarah",
        "last_name": "Patil",
        "shift_sum": "0:00"
      },
      {
        "shift_id": 28438,
        "employee_clock_in_time": "April 1, 2025 2:05 pm",
        "employee_clock_out_time": None,
        "first_name": "Imani",
        "last_name": "Thomas",
        "shift_sum": "00:00"
      },
      {
        "shift_id": 28436,
        "employee_clock_in_time": "April 1, 2025 12:33 pm",
        "employee_clock_out_time": "April 1, 2025 5:19 pm",
        "first_name": "Ayush",
        "last_name": "Kattupalli",
        "shift_sum": "4:46"
      },
      {
        "shift_id": 28432,
        "employee_clock_in_time": "April 1, 2025 11:55 am",
        "employee_clock_out_time": "April 1, 2025 7:15 pm",
        "first_name": "",
        "last_name": "",
        "shift_sum": "7:20"
      },
      {
        "shift_id": 28431,
        "employee_clock_in_time": "April 1, 2025 11:35 am",
        "employee_clock_out_time": "April 1, 2025 4:56 pm",
        "first_name": "Sai Venkata",
        "last_name": "Dhanush Amirinenii",
        "shift_sum": "5:21"
      },
      {
        "shift_id": 28424,
        "employee_clock_in_time": "April 1, 2025 11:06 am",
        "employee_clock_out_time": "April 1, 2025 6:28 pm",
        "first_name": "Kalind",
        "last_name": "Joshi",
        "shift_sum": "7:22"
      },
      {
        "shift_id": 28417,
        "employee_clock_in_time": "April 1, 2025 10:05 am",
        "employee_clock_out_time": "April 1, 2025 3:27 pm",
        "first_name": "Ibiye",
        "last_name": "Bright",
        "shift_sum": "5:22"
      },
      {
        "shift_id": 28416,
        "employee_clock_in_time": "April 1, 2025 10:03 am",
        "employee_clock_out_time": "April 1, 2025 3:39 pm",
        "first_name": "Arpita",
        "last_name": "Arpita LNU",
        "shift_sum": "5:35"
      },
      {
        "shift_id": 28415,
        "employee_clock_in_time": "April 1, 2025 10:00 am",
        "employee_clock_out_time": "April 1, 2025 3:03 pm",
        "first_name": "Sanath",
        "last_name": "Desai",
        "shift_sum": "5:02"
      },
      {
        "shift_id": 28413,
        "employee_clock_in_time": "April 1, 2025 10:00 am",
        "employee_clock_out_time": "April 1, 2025 1:32 pm",
        "first_name": "valerie",
        "last_name": "Osaweedoh",
        "shift_sum": "3:32"
      },
      {
        "shift_id": 28412,
        "employee_clock_in_time": "April 1, 2025 9:55 am",
        "employee_clock_out_time": None,
        "first_name": "Sai Swethan",
        "last_name": "Durganala",
        "shift_sum": "00:00"
      },
      {
        "shift_id": 28411,
        "employee_clock_in_time": "April 1, 2025 9:04 am",
        "employee_clock_out_time": None,
        "first_name": "Sarah",
        "last_name": "Patil",
        "shift_sum": "00:00"
      },
      {
        "shift_id": 28410,
        "employee_clock_in_time": "April 1, 2025 9:03 am",
        "employee_clock_out_time": "April 1, 2025 4:03 pm",
        "first_name": "Hepsiba Grace",
        "last_name": "Boddu",
        "shift_sum": "6:59"
      },
      {
        "shift_id": 28409,
        "employee_clock_in_time": "April 1, 2025 9:02 am",
        "employee_clock_out_time": None,
        "first_name": "Rakshitha Reddy",
        "last_name": "Potu",
        "shift_sum": "00:00"
      },
      {
        "shift_id": 28408,
        "employee_clock_in_time": "April 1, 2025 9:00 am",
        "employee_clock_out_time": "April 1, 2025 4:00 pm",
        "first_name": "Neelima",
        "last_name": "Palleboina",
        "shift_sum": "7:00"
      },
      {
        "shift_id": 28407,
        "employee_clock_in_time": "April 1, 2025 9:01 am",
        "employee_clock_out_time": "April 1, 2025 1:09 pm",
        "first_name": "Haren",
        "last_name": "Akula",
        "shift_sum": "4:08"
      },
      {
        "shift_id": 28406,
        "employee_clock_in_time": "April 1, 2025 8:59 am",
        "employee_clock_out_time": "April 1, 2025 5:00 pm",
        "first_name": "Shreya",
        "last_name": "Edulakanti",
        "shift_sum": "8:01"
      },
      {
        "shift_id": 28405,
        "employee_clock_in_time": "April 1, 2025 8:58 am",
        "employee_clock_out_time": "April 1, 2025 2:05 pm",
        "first_name": "Celeste",
        "last_name": "Nascimento",
        "shift_sum": "5:06"
      },
      {
        "shift_id": 28404,
        "employee_clock_in_time": "April 1, 2025 8:55 am",
        "employee_clock_out_time": None,
        "first_name": "Jonathan.",
        "last_name": "Almeida",
        "shift_sum": "00:00"
      },
      {
        "shift_id": 28403,
        "employee_clock_in_time": "April 1, 2025 8:36 am",
        "employee_clock_out_time": None,
        "first_name": "Prateeksha",
        "last_name": "Gawande",
        "shift_sum": "00:00"
      },
      {
        "shift_id": 28402,
        "employee_clock_in_time": "April 1, 2025 8:30 am",
        "employee_clock_out_time": None,
        "first_name": "Aanu",
        "last_name": "Adewusi",
        "shift_sum": "00:00"
      },
      {
        "shift_id": 28401,
        "employee_clock_in_time": "April 1, 2025 8:12 am",
        "employee_clock_out_time": "April 1, 2025 4:12 pm",
        "first_name": "Ru",
        "last_name": "Chen",
        "shift_sum": "7:59"
      },
      {
        "shift_id": 28399,
        "employee_clock_in_time": "March 31, 2025 10:15 am",
        "employee_clock_out_time": "March 31, 2025 5:15 pm",
        "first_name": "Nitant",
        "last_name": "Jatale",
        "shift_sum": "7:00"
      },
      {
        "shift_id": 28398,
        "employee_clock_in_time": "March 31, 2025 1:00 am",
        "employee_clock_out_time": "March 31, 2025 6:00 pm",
        "first_name": "Sree Lakshmi",
        "last_name": "Akella",
        "shift_sum": "17:00"
      },
      {
        "shift_id": 28397,
        "employee_clock_in_time": "March 31, 2025 9:00 am",
        "employee_clock_out_time": "March 31, 2025 4:00 pm",
        "first_name": "MeherSuneel",
        "last_name": "Meesala",
        "shift_sum": "7:00"
      },
      {
        "shift_id": 28393,
        "employee_clock_in_time": "March 31, 2025 7:32 pm",
        "employee_clock_out_time": "March 31, 2025 7:32 pm",
        "first_name": "Jonathan.",
        "last_name": "Almeida",
        "shift_sum": "0:00"
      },
      {
        "shift_id": 28392,
        "employee_clock_in_time": "March 31, 2025 5:15 pm",
        "employee_clock_out_time": "March 31, 2025 5:15 pm",
        "first_name": "Nitant",
        "last_name": "Jatale",
        "shift_sum": "0:00"
      },
      {
        "shift_id": 28391,
        "employee_clock_in_time": "March 31, 2025 4:10 pm",
        "employee_clock_out_time": "March 31, 2025 4:10 pm",
        "first_name": "Ru",
        "last_name": "Chen",
        "shift_sum": "0:00"
      },
      {
        "shift_id": 28390,
        "employee_clock_in_time": "March 31, 2025 3:59 pm",
        "employee_clock_out_time": "March 31, 2025 7:00 pm",
        "first_name": "Jessica",
        "last_name": "Vigil",
        "shift_sum": "3:00"
      },
      {
        "shift_id": 28377,
        "employee_clock_in_time": "March 31, 2025 1:00 pm",
        "employee_clock_out_time": "March 31, 2025 5:24 pm",
        "first_name": "Ayush",
        "last_name": "Kattupalli",
        "shift_sum": "4:23"
      },
      {
        "shift_id": 28376,
        "employee_clock_in_time": "March 31, 2025 1:00 pm",
        "employee_clock_out_time": "March 31, 2025 9:06 pm",
        "first_name": "Sree Lakshmi",
        "last_name": "Akella",
        "shift_sum": "8:06"
      },
      {
        "shift_id": 28374,
        "employee_clock_in_time": "March 31, 2025 12:16 pm",
        "employee_clock_out_time": "March 31, 2025 6:48 pm",
        "first_name": "Adarsh",
        "last_name": "Devineni",
        "shift_sum": "6:32"
      },
      {
        "shift_id": 28372,
        "employee_clock_in_time": "March 31, 2025 11:59 am",
        "employee_clock_out_time": "March 31, 2025 6:00 pm",
        "first_name": "Jisha",
        "last_name": "Sheelakumar",
        "shift_sum": "6:01"
      },
      {
        "shift_id": 28371,
        "employee_clock_in_time": "March 31, 2025 11:58 am",
        "employee_clock_out_time": "March 31, 2025 7:01 pm",
        "first_name": "Smita",
        "last_name": "Aghav",
        "shift_sum": "7:02"
      },
      {
        "shift_id": 28370,
        "employee_clock_in_time": "March 31, 2025 11:15 am",
        "employee_clock_out_time": "March 31, 2025 9:03 pm",
        "first_name": "Aanu",
        "last_name": "Adewusi",
        "shift_sum": "9:48"
      },
      {
        "shift_id": 28369,
        "employee_clock_in_time": "March 31, 2025 11:01 am",
        "employee_clock_out_time": "March 31, 2025 4:05 pm",
        "first_name": "Sai Venkata",
        "last_name": "Dhanush Amirinenii",
        "shift_sum": "5:04"
      },
      {
        "shift_id": 28368,
        "employee_clock_in_time": "March 31, 2025 11:01 am",
        "employee_clock_out_time": "March 31, 2025 5:03 pm",
        "first_name": "Chandrashakar",
        "last_name": "Gudipally",
        "shift_sum": "6:02"
      },
      {
        "shift_id": 28367,
        "employee_clock_in_time": "March 31, 2025 10:59 am",
        "employee_clock_out_time": "March 31, 2025 4:15 pm",
        "first_name": "Savana",
        "last_name": "Patel",
        "shift_sum": "5:16"
      },
      {
        "shift_id": 28365,
        "employee_clock_in_time": "March 31, 2025 10:27 am",
        "employee_clock_out_time": None,
        "first_name": "Nitant",
        "last_name": "Jatale",
        "shift_sum": "00:00"
      },
      {
        "shift_id": 28364,
        "employee_clock_in_time": "March 31, 2025 10:22 am",
        "employee_clock_out_time": None,
        "first_name": "FNU",
        "last_name": "Jannat",
        "shift_sum": "00:00"
      },
      {
        "shift_id": 28363,
        "employee_clock_in_time": "March 31, 2025 10:04 am",
        "employee_clock_out_time": "March 31, 2025 3:00 pm",
        "first_name": "McKenzie",
        "last_name": "Lynn Kovach",
        "shift_sum": "4:55"
      },
      {
        "shift_id": 28362,
        "employee_clock_in_time": "March 31, 2025 10:04 am",
        "employee_clock_out_time": None,
        "first_name": "Ibiye",
        "last_name": "Bright",
        "shift_sum": "00:00"
      },
      {
        "shift_id": 28360,
        "employee_clock_in_time": "March 31, 2025 10:00 am",
        "employee_clock_out_time": None,
        "first_name": "Sanath",
        "last_name": "Desai",
        "shift_sum": "00:00"
      },
      {
        "shift_id": 28361,
        "employee_clock_in_time": "March 31, 2025 10:00 am",
        "employee_clock_out_time": "March 31, 2025 3:00 pm",
        "first_name": "Sanath",
        "last_name": "Desai",
        "shift_sum": "5:00"
      },
      {
        "shift_id": 28359,
        "employee_clock_in_time": "March 31, 2025 10:00 am",
        "employee_clock_out_time": None,
        "first_name": "Nithish Reddy",
        "last_name": "Mannem",
        "shift_sum": "00:00"
      },
      {
        "shift_id": 28358,
        "employee_clock_in_time": "March 31, 2025 9:49 am",
        "employee_clock_out_time": "March 31, 2025 2:00 pm",
        "first_name": "valerie",
        "last_name": "Osaweedoh",
        "shift_sum": "4:11"
      },
      {
        "shift_id": 28357,
        "employee_clock_in_time": "March 31, 2025 9:26 am",
        "employee_clock_out_time": None,
        "first_name": "Jonathan.",
        "last_name": "Almeida",
        "shift_sum": "00:00"
      },
      {
        "shift_id": 28356,
        "employee_clock_in_time": "March 31, 2025 9:05 am",
        "employee_clock_out_time": "March 31, 2025 3:01 pm",
        "first_name": "Sarah",
        "last_name": "Patil",
        "shift_sum": "5:55"
      },
      {
        "shift_id": 28355,
        "employee_clock_in_time": "March 31, 2025 9:01 am",
        "employee_clock_out_time": "March 31, 2025 4:06 pm",
        "first_name": "Rakshitha Reddy",
        "last_name": "Potu",
        "shift_sum": "7:04"
      },
      {
        "shift_id": 28354,
        "employee_clock_in_time": "March 31, 2025 8:59 am",
        "employee_clock_out_time": "March 31, 2025 2:00 pm",
        "first_name": "Haren",
        "last_name": "Akula",
        "shift_sum": "5:00"
      },
      {
        "shift_id": 28353,
        "employee_clock_in_time": "March 31, 2025 8:59 am",
        "employee_clock_out_time": "March 31, 2025 5:00 pm",
        "first_name": "Shreya",
        "last_name": "Edulakanti",
        "shift_sum": "8:01"
      },
      {
        "shift_id": 28352,
        "employee_clock_in_time": "March 31, 2025 8:41 am",
        "employee_clock_out_time": None,
        "first_name": "Ru",
        "last_name": "Chen",
        "shift_sum": "00:00"
      }
    ]
  }
}
#EXPECTED_SCHEDULE = [
#    {
#        "first_name": "Alma",
#        "last_name": "Landaverde",
#        "Schedule": {
#            "Monday": ("9:00 AM", "1:00 PM"),
#            "Tuesday": (None, None),
#            "Wednesday": ("9:00 AM", "1:00 PM"),
#            "Thursday": ("9:00 AM", "1:00 PM"),
#            "Friday": (None, None)
#        }
#    },
#    {
#        "first_name": "MeherSuneel",
#        "last_name": "Meesala",
#        "Schedule": {
#            "Monday": ("9:00 AM", "4:00 PM"),
#            "Tuesday": (None, None),
#            "Wednesday": ("9:00 AM", "4:00 PM"),
#            "Thursday": (None, None),
#            "Friday": ("9:00 AM", "4:00 PM")
#        }
#    }
#]


# Your existing JSON body
#



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


# Initialize a dictionary to accumulate total work time for each employee
employee_work_time = defaultdict(lambda: [0, 0])  # [total_hours, total_minutes]

# Iterate through the shifts and calculate total hours and minutes worked
for shift in shifts:  # Now we iterate directly over the list
    full_name = f"{shift['first_name']} {shift['last_name']}"
    
    # Parse shift_sum like "7:51"
    shift_sum = shift.get("shift_sum", "0:00")
    hrs, mins = map(int, shift_sum.split(":"))
    
    # Add the hours and minutes to the total for this employee
    employee_work_time[full_name][0] += hrs
    employee_work_time[full_name][1] += mins

# Now generate the JSON body with the total hours worked for each employee
result = []

for full_name, time in employee_work_time.items():
    # Ensure there is at least a first name and last name
    name_parts = full_name.split()
    if len(name_parts) < 2:
        print(f"Warning: Invalid name format for employee '{full_name}', skipping...")
        continue

    first_name, last_name = name_parts[0], name_parts[1]
    
    # Calculate total hours and minutes
    total_hours = time[0] + (time[1] // 60)  # Convert minutes to hours
    total_minutes = time[1] % 60            # Remainder of minutes after converting to hours
    
    # Add the employee data to the result list
    result.append({
        "first_name": first_name,
        "last_name": last_name,
        "total_hours": f"{total_hours}:{total_minutes:02d}"
    })

print(result)

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
            background-color:rgb(244, 244, 54); /* Black for not scheduled */
            color: white;
        }}
        td.mismatch {{
            background-color: #f44336; /* Orange for mismatch */
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
            <th>Total Hours Worked</th>
        </tr>
    </thead>
    <tbody>
"""
# Generate the HTML table rows with styles
for employee in EXPECTED_SCHEDULE:
    employee_name = f"{employee['first_name']} {employee['last_name']}"
    total_hours_worked = "Not Available"  # Default value in case the employee is not found
    for result_employee in result:
        if result_employee['first_name'] == employee['first_name'] and result_employee['last_name'] == employee['last_name']:
            total_hours_worked = result_employee['total_hours']
            break
    
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
    html += f"<td>{total_hours_worked}</td></tr>"

html += "</tbody></table></body></html>"

# Print the HTML table to console
print(html)

# Save the HTML table to a file
with open('employee_report.html', 'w') as file:
    file.write(html)
