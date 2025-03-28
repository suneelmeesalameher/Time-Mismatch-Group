from datetime import datetime, timedelta
from Get_details_from_csv import EXPECTED_SCHEDULE
import os

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
json_body ={
  "response": "success",
  "employee": 0,
  "date_range_start": "2025-03-24 00:00:00",
  "date_range_end": "2025-03-28 22:00:00",
  "report_action": "generate_report",
  "shifts": {
    "response": "success",
    "shift_count": 132,
    "shift_total_time": "522:52",
    "wage_total": "0.00",
    "shift_array": [
      {
        "shift_id": 28341,
        "employee_clock_in_time": "March 25, 2025 12:00 pm",
        "employee_clock_out_time": "March 25, 2025 7:00 pm",
        "first_name": "Jayaprakash",
        "last_name": "Vangala",
        "shift_sum": "7:00"
      },
      {
        "shift_id": 28340,
        "employee_clock_in_time": "March 26, 2025 9:00 am",
        "employee_clock_out_time": "March 26, 2025 4:00 pm",
        "first_name": "Rakshitha Reddy",
        "last_name": "Potu",
        "shift_sum": "7:00"
      },
      {
        "shift_id": 28339,
        "employee_clock_in_time": "March 26, 2025 10:00 am",
        "employee_clock_out_time": "March 26, 2025 5:00 pm",
        "first_name": "Nithish Reddy",
        "last_name": "Mannem",
        "shift_sum": "7:00"
      },
      {
        "shift_id": 28338,
        "employee_clock_in_time": "March 26, 2025 8:00 am",
        "employee_clock_out_time": "March 26, 2025 6:00 pm",
        "first_name": "Aanu",
        "last_name": "Adewusi",
        "shift_sum": "10:00"
      },
      {
        "shift_id": 28337,
        "employee_clock_in_time": "March 25, 2025 8:00 am",
        "employee_clock_out_time": "March 25, 2025 9:30 pm",
        "first_name": "Aanu",
        "last_name": "Adewusi",
        "shift_sum": "13:30"
      },
      {
        "shift_id": 28336,
        "employee_clock_in_time": "March 24, 2025 8:00 am",
        "employee_clock_out_time": "March 24, 2025 9:30 pm",
        "first_name": "Aanu",
        "last_name": "Adewusi",
        "shift_sum": "13:30"
      },
      {
        "shift_id": 28332,
        "employee_clock_in_time": "March 26, 2025 1:00 pm",
        "employee_clock_out_time": "March 26, 2025 6:00 pm",
        "first_name": "Sree Lakshmi",
        "last_name": "Akella",
        "shift_sum": "5:00"
      },
      {
        "shift_id": 28331,
        "employee_clock_in_time": "March 26, 2025 11:00 am",
        "employee_clock_out_time": "March 26, 2025 6:00 pm",
        "first_name": "Kalind",
        "last_name": "Joshi",
        "shift_sum": "7:00"
      },
      {
        "shift_id": 28329,
        "employee_clock_in_time": "March 26, 2025 9:00 am",
        "employee_clock_out_time": "March 26, 2025 4:00 pm",
        "first_name": "MeherSuneel",
        "last_name": "Meesala",
        "shift_sum": "7:00"
      },
      {
        "shift_id": 28328,
        "employee_clock_in_time": "March 28, 2025 11:00 am",
        "employee_clock_out_time": None,
        "first_name": "Jisha",
        "last_name": "Sheelakumar",
        "shift_sum": "00:00"
      },
      {
        "shift_id": 28327,
        "employee_clock_in_time": "March 28, 2025 10:56 am",
        "employee_clock_out_time": None,
        "first_name": "Chandrashakar",
        "last_name": "Gudipally",
        "shift_sum": "00:00"
      },
      {
        "shift_id": 28322,
        "employee_clock_in_time": "March 28, 2025 9:03 am",
        "employee_clock_out_time": None,
        "first_name": "Neelima",
        "last_name": "Palleboina",
        "shift_sum": "00:00"
      },
      {
        "shift_id": 28321,
        "employee_clock_in_time": "March 28, 2025 9:02 am",
        "employee_clock_out_time": None,
        "first_name": "Samyukta",
        "last_name": "Padmanabhuni",
        "shift_sum": "00:00"
      },
      {
        "shift_id": 28320,
        "employee_clock_in_time": "March 28, 2025 9:00 am",
        "employee_clock_out_time": None,
        "first_name": "Shreya",
        "last_name": "Edulakanti",
        "shift_sum": "00:00"
      },
      {
        "shift_id": 28319,
        "employee_clock_in_time": "March 28, 2025 9:00 am",
        "employee_clock_out_time": None,
        "first_name": "MeherSuneel",
        "last_name": "Meesala",
        "shift_sum": "00:00"
      },
      {
        "shift_id": 28311,
        "employee_clock_in_time": "March 27, 2025 3:22 pm",
        "employee_clock_out_time": None,
        "first_name": "Sanath",
        "last_name": "Desai",
        "shift_sum": "00:00"
      },
      {
        "shift_id": 28310,
        "employee_clock_in_time": "March 27, 2025 3:01 pm",
        "employee_clock_out_time": None,
        "first_name": "Adarsh",
        "last_name": "Devineni",
        "shift_sum": "00:00"
      },
      {
        "shift_id": 28308,
        "employee_clock_in_time": "March 27, 2025 12:59 pm",
        "employee_clock_out_time": "March 27, 2025 6:04 pm",
        "first_name": "Sagar Naidu",
        "last_name": "Potana",
        "shift_sum": "5:05"
      },
      {
        "shift_id": 28301,
        "employee_clock_in_time": "March 27, 2025 12:03 pm",
        "employee_clock_out_time": "March 27, 2025 5:03 pm",
        "first_name": "Nigama",
        "last_name": "Dendukuri",
        "shift_sum": "5:00"
      },
      {
        "shift_id": 28300,
        "employee_clock_in_time": "March 27, 2025 11:57 am",
        "employee_clock_out_time": "March 27, 2025 4:52 pm",
        "first_name": "Sai Venkata",
        "last_name": "Dhanush Amirinenii",
        "shift_sum": "4:54"
      },
      {
        "shift_id": 28299,
        "employee_clock_in_time": "March 27, 2025 11:43 am",
        "employee_clock_out_time": "March 27, 2025 7:47 pm",
        "first_name": "Ayush",
        "last_name": "Kattupalli",
        "shift_sum": "8:04"
      },
      {
        "shift_id": 28297,
        "employee_clock_in_time": "March 27, 2025 10:01 am",
        "employee_clock_out_time": "March 27, 2025 3:15 pm",
        "first_name": "Sanath",
        "last_name": "Desai",
        "shift_sum": "5:13"
      },
      {
        "shift_id": 28296,
        "employee_clock_in_time": "March 27, 2025 10:00 am",
        "employee_clock_out_time": None,
        "first_name": "Sai",
        "last_name": "Shivani",
        "shift_sum": "00:00"
      },
      {
        "shift_id": 28295,
        "employee_clock_in_time": "March 27, 2025 10:00 am",
        "employee_clock_out_time": "March 27, 2025 5:03 pm",
        "first_name": "Nithish Reddy",
        "last_name": "Mannem",
        "shift_sum": "7:03"
      },
      {
        "shift_id": 28294,
        "employee_clock_in_time": "March 27, 2025 9:48 am",
        "employee_clock_out_time": "March 27, 2025 2:13 pm",
        "first_name": "Ru",
        "last_name": "Chen",
        "shift_sum": "4:25"
      },
      {
        "shift_id": 28293,
        "employee_clock_in_time": "March 27, 2025 9:04 am",
        "employee_clock_out_time": "March 27, 2025 4:10 pm",
        "first_name": "Neelima",
        "last_name": "Palleboina",
        "shift_sum": "7:05"
      },
      {
        "shift_id": 28292,
        "employee_clock_in_time": "March 27, 2025 9:04 am",
        "employee_clock_out_time": "March 27, 2025 5:03 pm",
        "first_name": "Samyukta",
        "last_name": "Padmanabhuni",
        "shift_sum": "7:59"
      },
      {
        "shift_id": 28291,
        "employee_clock_in_time": "March 27, 2025 8:59 am",
        "employee_clock_out_time": "March 27, 2025 1:00 pm",
        "first_name": "Shreya",
        "last_name": "Edulakanti",
        "shift_sum": "4:01"
      },
      {
        "shift_id": 28290,
        "employee_clock_in_time": "March 27, 2025 8:59 am",
        "employee_clock_out_time": "March 27, 2025 1:59 pm",
        "first_name": "Haren",
        "last_name": "Akula",
        "shift_sum": "5:00"
      },
      {
        "shift_id": 28289,
        "employee_clock_in_time": "March 27, 2025 8:58 am",
        "employee_clock_out_time": "March 27, 2025 2:03 pm",
        "first_name": "Celeste",
        "last_name": "Nascimento",
        "shift_sum": "5:04"
      },
      {
        "shift_id": 28288,
        "employee_clock_in_time": "March 27, 2025 8:57 am",
        "employee_clock_out_time": None,
        "first_name": "Aanu",
        "last_name": "Adewusi",
        "shift_sum": "00:00"
      },
      {
        "shift_id": 28287,
        "employee_clock_in_time": "March 27, 2025 8:30 am",
        "employee_clock_out_time": "March 27, 2025 2:35 pm",
        "first_name": "Prateeksha",
        "last_name": "Gawande",
        "shift_sum": "6:04"
      },
      {
        "shift_id": 28286,
        "employee_clock_in_time": "March 27, 2025 8:00 am",
        "employee_clock_out_time": "March 27, 2025 1:00 pm",
        "first_name": "Sree Lakshmi",
        "last_name": "Akella",
        "shift_sum": "4:59"
      },
      {
        "shift_id": 28283,
        "employee_clock_in_time": "March 25, 2025 9:00 am",
        "employee_clock_out_time": "March 25, 2025 2:00 pm",
        "first_name": "Ru",
        "last_name": "Chen",
        "shift_sum": "5:00"
      },
      {
        "shift_id": 28282,
        "employee_clock_in_time": "March 24, 2025 9:00 am",
        "employee_clock_out_time": "March 24, 2025 2:00 pm",
        "first_name": "Ru",
        "last_name": "Chen",
        "shift_sum": "5:00"
      },
      {
        "shift_id": 28281,
        "employee_clock_in_time": "March 26, 2025 4:05 pm",
        "employee_clock_out_time": "March 26, 2025 4:05 pm",
        "first_name": "Rakshitha Reddy",
        "last_name": "Potu",
        "shift_sum": "0:00"
      },
      {
        "shift_id": 28280,
        "employee_clock_in_time": "March 26, 2025 4:03 pm",
        "employee_clock_out_time": "March 26, 2025 4:04 pm",
        "first_name": "Savana",
        "last_name": "Patel",
        "shift_sum": "0:00"
      },
      {
        "shift_id": 28279,
        "employee_clock_in_time": "March 26, 2025 3:21 pm",
        "employee_clock_out_time": "March 26, 2025 4:57 pm",
        "first_name": "Jessica",
        "last_name": "Vigil",
        "shift_sum": "1:35"
      },
      {
        "shift_id": 28277,
        "employee_clock_in_time": "March 26, 2025 2:44 pm",
        "employee_clock_out_time": "March 26, 2025 6:02 pm",
        "first_name": "Aanu",
        "last_name": "Adewusi",
        "shift_sum": "3:17"
      },
      {
        "shift_id": 28276,
        "employee_clock_in_time": "March 26, 2025 2:24 pm",
        "employee_clock_out_time": "March 26, 2025 4:56 pm",
        "first_name": "Sarah",
        "last_name": "Patil",
        "shift_sum": "2:31"
      },
      {
        "shift_id": 28274,
        "employee_clock_in_time": "March 25, 2025 9:14 am",
        "employee_clock_out_time": "March 25, 2025 3:10 pm",
        "first_name": "Sarah",
        "last_name": "Patil",
        "shift_sum": "5:56"
      },
      {
        "shift_id": 28273,
        "employee_clock_in_time": "March 25, 2025 9:00 am",
        "employee_clock_out_time": "March 25, 2025 5:00 pm",
        "first_name": "Shreya",
        "last_name": "Edulakanti",
        "shift_sum": "8:00"
      },
      {
        "shift_id": 28272,
        "employee_clock_in_time": "March 25, 2025 10:00 am",
        "employee_clock_out_time": "March 25, 2025 3:00 pm",
        "first_name": "Almatou",
        "last_name": "SARE",
        "shift_sum": "5:00"
      },
      {
        "shift_id": 28271,
        "employee_clock_in_time": "March 26, 2025 1:12 pm",
        "employee_clock_out_time": "March 26, 2025 6:29 pm",
        "first_name": "Sree Lakshmi",
        "last_name": "Akella",
        "shift_sum": "5:17"
      },
      {
        "shift_id": 28270,
        "employee_clock_in_time": "March 26, 2025 1:00 pm",
        "employee_clock_out_time": "March 26, 2025 6:04 pm",
        "first_name": "Sagar Naidu",
        "last_name": "Potana",
        "shift_sum": "5:03"
      },
      {
        "shift_id": 28269,
        "employee_clock_in_time": "March 26, 2025 12:27 pm",
        "employee_clock_out_time": "March 26, 2025 1:57 pm",
        "first_name": "Jessica",
        "last_name": "Vigil",
        "shift_sum": "1:29"
      },
      {
        "shift_id": 28268,
        "employee_clock_in_time": "March 26, 2025 12:14 pm",
        "employee_clock_out_time": "March 26, 2025 5:00 pm",
        "first_name": "Sai Swethan",
        "last_name": "Durganala",
        "shift_sum": "4:45"
      },
      {
        "shift_id": 28267,
        "employee_clock_in_time": "March 26, 2025 12:11 pm",
        "employee_clock_out_time": "March 26, 2025 5:18 pm",
        "first_name": "Nigama",
        "last_name": "Dendukuri",
        "shift_sum": "5:06"
      },
      {
        "shift_id": 28266,
        "employee_clock_in_time": "March 26, 2025 11:59 am",
        "employee_clock_out_time": "March 26, 2025 5:38 pm",
        "first_name": "Smita",
        "last_name": "Aghav",
        "shift_sum": "5:38"
      },
      {
        "shift_id": 28265,
        "employee_clock_in_time": "March 26, 2025 11:56 am",
        "employee_clock_out_time": "March 26, 2025 6:59 pm",
        "first_name": "Shubhika",
        "last_name": "Gupta",
        "shift_sum": "7:03"
      },
      {
        "shift_id": 28264,
        "employee_clock_in_time": "March 26, 2025 11:41 am",
        "employee_clock_out_time": None,
        "first_name": "Savana",
        "last_name": "Patel",
        "shift_sum": "00:00"
      },
      {
        "shift_id": 28263,
        "employee_clock_in_time": "March 26, 2025 11:35 am",
        "employee_clock_out_time": "March 26, 2025 1:01 pm",
        "first_name": "valerie",
        "last_name": "Osaweedoh",
        "shift_sum": "1:26"
      },
      {
        "shift_id": 28262,
        "employee_clock_in_time": "March 26, 2025 11:02 am",
        "employee_clock_out_time": None,
        "first_name": "Kalind",
        "last_name": "Joshi",
        "shift_sum": "00:00"
      },
      {
        "shift_id": 28261,
        "employee_clock_in_time": "March 26, 2025 11:01 am",
        "employee_clock_out_time": "March 26, 2025 6:02 pm",
        "first_name": "Jisha",
        "last_name": "Sheelakumar",
        "shift_sum": "7:00"
      },
      {
        "shift_id": 28260,
        "employee_clock_in_time": "March 26, 2025 10:13 am",
        "employee_clock_out_time": "March 26, 2025 3:34 pm",
        "first_name": "Sai Venkata",
        "last_name": "Dhanush Amirinenii",
        "shift_sum": "5:20"
      },
      {
        "shift_id": 28259,
        "employee_clock_in_time": "March 26, 2025 10:04 am",
        "employee_clock_out_time": "March 26, 2025 3:04 pm",
        "first_name": "Sanath",
        "last_name": "Desai",
        "shift_sum": "5:00"
      },
      {
        "shift_id": 28258,
        "employee_clock_in_time": "March 26, 2025 10:03 am",
        "employee_clock_out_time": None,
        "first_name": "Adarsh",
        "last_name": "Devineni",
        "shift_sum": "00:00"
      },
      {
        "shift_id": 28257,
        "employee_clock_in_time": "March 26, 2025 10:00 am",
        "employee_clock_out_time": "March 26, 2025 2:01 pm",
        "first_name": "Shreya",
        "last_name": "Edulakanti",
        "shift_sum": "4:00"
      },
      {
        "shift_id": 28256,
        "employee_clock_in_time": "March 26, 2025 10:00 am",
        "employee_clock_out_time": None,
        "first_name": "Nithish Reddy",
        "last_name": "Mannem",
        "shift_sum": "00:00"
      },
      {
        "shift_id": 28255,
        "employee_clock_in_time": "March 26, 2025 9:13 am",
        "employee_clock_out_time": "March 26, 2025 2:29 pm",
        "first_name": "Ru",
        "last_name": "Chen",
        "shift_sum": "5:16"
      },
      {
        "shift_id": 28254,
        "employee_clock_in_time": "March 26, 2025 9:05 am",
        "employee_clock_out_time": None,
        "first_name": "Sarah",
        "last_name": "Patil",
        "shift_sum": "00:00"
      },
      {
        "shift_id": 28253,
        "employee_clock_in_time": "March 26, 2025 9:02 am",
        "employee_clock_out_time": "March 26, 2025 4:03 pm",
        "first_name": "Hepsiba Grace",
        "last_name": "Boddu",
        "shift_sum": "7:01"
      },
      {
        "shift_id": 28252,
        "employee_clock_in_time": "March 26, 2025 9:01 am",
        "employee_clock_out_time": None,
        "first_name": "Rakshitha Reddy",
        "last_name": "Potu",
        "shift_sum": "00:00"
      },
      {
        "shift_id": 28251,
        "employee_clock_in_time": "March 26, 2025 9:00 am",
        "employee_clock_out_time": "March 26, 2025 5:01 pm",
        "first_name": "Samyukta",
        "last_name": "Padmanabhuni",
        "shift_sum": "8:01"
      },
      {
        "shift_id": 28250,
        "employee_clock_in_time": "March 26, 2025 8:58 am",
        "employee_clock_out_time": "March 26, 2025 1:59 pm",
        "first_name": "Haren",
        "last_name": "Akula",
        "shift_sum": "5:00"
      },
      {
        "shift_id": 28249,
        "employee_clock_in_time": "March 26, 2025 8:56 am",
        "employee_clock_out_time": "March 26, 2025 2:59 pm",
        "first_name": "Arpita",
        "last_name": "Arpita LNU",
        "shift_sum": "6:02"
      },
      {
        "shift_id": 28248,
        "employee_clock_in_time": "March 26, 2025 8:30 am",
        "employee_clock_out_time": "March 26, 2025 3:33 pm",
        "first_name": "Prateeksha",
        "last_name": "Gawande",
        "shift_sum": "7:02"
      },
      {
        "shift_id": 28247,
        "employee_clock_in_time": "March 25, 2025 7:27 pm",
        "employee_clock_out_time": "March 25, 2025 7:27 pm",
        "first_name": "Jonathan.",
        "last_name": "Almeida",
        "shift_sum": "0:00"
      },
      {
        "shift_id": 28236,
        "employee_clock_in_time": "March 25, 2025 3:10 pm",
        "employee_clock_out_time": "March 25, 2025 3:10 pm",
        "first_name": "Sarah",
        "last_name": "Patil",
        "shift_sum": "0:00"
      },
      {
        "shift_id": 28235,
        "employee_clock_in_time": "March 25, 2025 2:07 pm",
        "employee_clock_out_time": "March 25, 2025 5:08 pm",
        "first_name": "Jessica",
        "last_name": "Vigil",
        "shift_sum": "3:00"
      },
      {
        "shift_id": 28226,
        "employee_clock_in_time": "March 25, 2025 1:00 pm",
        "employee_clock_out_time": "March 25, 2025 6:03 pm",
        "first_name": "Sagar Naidu",
        "last_name": "Potana",
        "shift_sum": "5:02"
      },
      {
        "shift_id": 28224,
        "employee_clock_in_time": "March 24, 2025 9:05 am",
        "employee_clock_out_time": "March 24, 2025 3:05 pm",
        "first_name": "sarah",
        "last_name": "janeway",
        "shift_sum": "6:00"
      },
      {
        "shift_id": 28223,
        "employee_clock_in_time": "March 25, 2025 12:01 pm",
        "employee_clock_out_time": "March 25, 2025 5:01 pm",
        "first_name": "Nigama",
        "last_name": "Dendukuri",
        "shift_sum": "4:59"
      },
      {
        "shift_id": 28222,
        "employee_clock_in_time": "March 25, 2025 11:59 am",
        "employee_clock_out_time": "March 25, 2025 5:18 pm",
        "first_name": "Ayush",
        "last_name": "Kattupalli",
        "shift_sum": "5:19"
      },
      {
        "shift_id": 28221,
        "employee_clock_in_time": "March 25, 2025 11:51 am",
        "employee_clock_out_time": "March 25, 2025 6:56 pm",
        "first_name": "",
        "last_name": "",
        "shift_sum": "7:05"
      },
      {
        "shift_id": 28218,
        "employee_clock_in_time": "March 25, 2025 11:19 am",
        "employee_clock_out_time": "March 25, 2025 6:19 pm",
        "first_name": "Kalind",
        "last_name": "Joshi",
        "shift_sum": "6:59"
      },
      {
        "shift_id": 28216,
        "employee_clock_in_time": "March 25, 2025 11:15 am",
        "employee_clock_out_time": None,
        "first_name": "Aanu",
        "last_name": "Adewusi",
        "shift_sum": "00:00"
      },
      {
        "shift_id": 28215,
        "employee_clock_in_time": "March 25, 2025 10:55 am",
        "employee_clock_out_time": "March 25, 2025 6:14 pm",
        "first_name": "Nitant",
        "last_name": "Jatale",
        "shift_sum": "7:18"
      },
      {
        "shift_id": 28212,
        "employee_clock_in_time": "March 25, 2025 10:34 am",
        "employee_clock_out_time": None,
        "first_name": "Sai Venkata",
        "last_name": "Dhanush Amirinenii",
        "shift_sum": "00:00"
      },
      {
        "shift_id": 28211,
        "employee_clock_in_time": "March 25, 2025 10:05 am",
        "employee_clock_out_time": "March 25, 2025 2:02 pm",
        "first_name": "Ibiye",
        "last_name": "Bright",
        "shift_sum": "3:56"
      },
      {
        "shift_id": 28210,
        "employee_clock_in_time": "March 25, 2025 10:02 am",
        "employee_clock_out_time": "March 25, 2025 3:02 pm",
        "first_name": "Sanath",
        "last_name": "Desai",
        "shift_sum": "5:00"
      },
      {
        "shift_id": 28209,
        "employee_clock_in_time": "March 25, 2025 10:00 am",
        "employee_clock_out_time": None,
        "first_name": "Sai",
        "last_name": "Shivani",
        "shift_sum": "00:00"
      },
      {
        "shift_id": 28208,
        "employee_clock_in_time": "March 25, 2025 10:00 am",
        "employee_clock_out_time": "March 25, 2025 5:00 pm",
        "first_name": "Nithish Reddy",
        "last_name": "Mannem",
        "shift_sum": "6:59"
      },
      {
        "shift_id": 28207,
        "employee_clock_in_time": "March 25, 2025 10:00 am",
        "employee_clock_out_time": "March 25, 2025 1:52 pm",
        "first_name": "valerie",
        "last_name": "Osaweedoh",
        "shift_sum": "3:52"
      },
      {
        "shift_id": 28206,
        "employee_clock_in_time": "March 25, 2025 9:59 am",
        "employee_clock_out_time": "March 25, 2025 3:01 pm",
        "first_name": "McKenzie",
        "last_name": "Lynn Kovach",
        "shift_sum": "5:01"
      },
      {
        "shift_id": 28205,
        "employee_clock_in_time": "March 25, 2025 9:55 am",
        "employee_clock_out_time": "March 25, 2025 4:55 pm",
        "first_name": "Sai Swethan",
        "last_name": "Durganala",
        "shift_sum": "7:00"
      },
      {
        "shift_id": 28204,
        "employee_clock_in_time": "March 25, 2025 9:51 am",
        "employee_clock_out_time": None,
        "first_name": "Almatou",
        "last_name": "SARE",
        "shift_sum": "00:00"
      },
      {
        "shift_id": 28202,
        "employee_clock_in_time": "March 24, 2025 11:00 am",
        "employee_clock_out_time": "March 24, 2025 6:00 pm",
        "first_name": "Chandrashakar",
        "last_name": "Gudipally",
        "shift_sum": "7:00"
      },
      {
        "shift_id": 28194,
        "employee_clock_in_time": "March 25, 2025 9:15 am",
        "employee_clock_out_time": "March 25, 2025 4:16 pm",
        "first_name": "Hepsiba Grace",
        "last_name": "Boddu",
        "shift_sum": "7:01"
      },
      {
        "shift_id": 28193,
        "employee_clock_in_time": "March 25, 2025 9:14 am",
        "employee_clock_out_time": None,
        "first_name": "Sarah",
        "last_name": "Patil",
        "shift_sum": "00:00"
      },
      {
        "shift_id": 28192,
        "employee_clock_in_time": "March 25, 2025 9:00 am",
        "employee_clock_out_time": "March 25, 2025 4:00 pm",
        "first_name": "Neelima",
        "last_name": "Palleboina",
        "shift_sum": "7:00"
      },
      {
        "shift_id": 28191,
        "employee_clock_in_time": "March 25, 2025 9:05 am",
        "employee_clock_out_time": "March 25, 2025 12:07 pm",
        "first_name": "FNU",
        "last_name": "Jannat",
        "shift_sum": "3:02"
      },
      {
        "shift_id": 28190,
        "employee_clock_in_time": "March 25, 2025 9:01 am",
        "employee_clock_out_time": "March 25, 2025 4:03 pm",
        "first_name": "Rakshitha Reddy",
        "last_name": "Potu",
        "shift_sum": "7:01"
      },
      {
        "shift_id": 28189,
        "employee_clock_in_time": "March 25, 2025 9:01 am",
        "employee_clock_out_time": "March 25, 2025 2:04 pm",
        "first_name": "Celeste",
        "last_name": "Nascimento",
        "shift_sum": "5:02"
      },
      {
        "shift_id": 28188,
        "employee_clock_in_time": "March 25, 2025 9:00 am",
        "employee_clock_out_time": "March 25, 2025 2:00 pm",
        "first_name": "Haren",
        "last_name": "Akula",
        "shift_sum": "4:59"
      },
      {
        "shift_id": 28187,
        "employee_clock_in_time": "March 25, 2025 8:59 am",
        "employee_clock_out_time": None,
        "first_name": "Shreya",
        "last_name": "Edulakanti",
        "shift_sum": "00:00"
      },
      {
        "shift_id": 28186,
        "employee_clock_in_time": "March 25, 2025 8:57 am",
        "employee_clock_out_time": "March 25, 2025 2:57 pm",
        "first_name": "Arpita",
        "last_name": "Arpita LNU",
        "shift_sum": "6:00"
      },
      {
        "shift_id": 28185,
        "employee_clock_in_time": "March 25, 2025 8:55 am",
        "employee_clock_out_time": None,
        "first_name": "Jonathan.",
        "last_name": "Almeida",
        "shift_sum": "00:00"
      },
      {
        "shift_id": 28184,
        "employee_clock_in_time": "March 25, 2025 8:34 am",
        "employee_clock_out_time": "March 25, 2025 3:36 pm",
        "first_name": "Prateeksha",
        "last_name": "Gawande",
        "shift_sum": "7:02"
      },
      {
        "shift_id": 28183,
        "employee_clock_in_time": "March 25, 2025 7:59 am",
        "employee_clock_out_time": "March 25, 2025 1:00 pm",
        "first_name": "Sree Lakshmi",
        "last_name": "Akella",
        "shift_sum": "5:01"
      },
      {
        "shift_id": 28182,
        "employee_clock_in_time": "March 24, 2025 7:48 pm",
        "employee_clock_out_time": "March 24, 2025 7:49 pm",
        "first_name": "Jonathan.",
        "last_name": "Almeida",
        "shift_sum": "0:00"
      },
      {
        "shift_id": 28178,
        "employee_clock_in_time": "March 24, 2025 5:01 pm",
        "employee_clock_out_time": "March 24, 2025 5:01 pm",
        "first_name": "Nitant",
        "last_name": "Jatale",
        "shift_sum": "0:00"
      },
      {
        "shift_id": 28177,
        "employee_clock_in_time": "March 24, 2025 5:00 pm",
        "employee_clock_out_time": None,
        "first_name": "Aanu",
        "last_name": "Adewusi",
        "shift_sum": "00:00"
      },
      {
        "shift_id": 28176,
        "employee_clock_in_time": "March 24, 2025 4:17 pm",
        "employee_clock_out_time": "March 24, 2025 4:17 pm",
        "first_name": "Savana",
        "last_name": "Patel",
        "shift_sum": "0:00"
      },
      {
        "shift_id": 28175,
        "employee_clock_in_time": "March 24, 2025 3:59 pm",
        "employee_clock_out_time": "March 24, 2025 7:01 pm",
        "first_name": "Jessica",
        "last_name": "Vigil",
        "shift_sum": "3:02"
      },
      {
        "shift_id": 28174,
        "employee_clock_in_time": "March 24, 2025 3:05 pm",
        "employee_clock_out_time": "March 24, 2025 3:05 pm",
        "first_name": "Sarah",
        "last_name": "Patil",
        "shift_sum": "0:00"
      },
      {
        "shift_id": 28145,
        "employee_clock_in_time": "March 24, 2025 1:00 pm",
        "employee_clock_out_time": "March 24, 2025 5:59 pm",
        "first_name": "Sree Lakshmi",
        "last_name": "Akella",
        "shift_sum": "4:58"
      },
      {
        "shift_id": 28144,
        "employee_clock_in_time": "March 24, 2025 12:59 pm",
        "employee_clock_out_time": "March 24, 2025 2:01 pm",
        "first_name": "valerie",
        "last_name": "Osaweedoh",
        "shift_sum": "1:01"
      },
      {
        "shift_id": 28143,
        "employee_clock_in_time": "March 24, 2025 12:58 pm",
        "employee_clock_out_time": "March 24, 2025 6:00 pm",
        "first_name": "Sagar Naidu",
        "last_name": "Potana",
        "shift_sum": "5:02"
      },
      {
        "shift_id": 28141,
        "employee_clock_in_time": "March 24, 2025 12:12 pm",
        "employee_clock_out_time": "March 24, 2025 5:25 pm",
        "first_name": "Ayush",
        "last_name": "Kattupalli",
        "shift_sum": "5:13"
      },
      {
        "shift_id": 28140,
        "employee_clock_in_time": "March 24, 2025 12:01 pm",
        "employee_clock_out_time": "March 24, 2025 6:02 pm",
        "first_name": "Jisha",
        "last_name": "Sheelakumar",
        "shift_sum": "6:00"
      },
      {
        "shift_id": 28139,
        "employee_clock_in_time": "March 24, 2025 11:59 am",
        "employee_clock_out_time": "March 24, 2025 7:00 pm",
        "first_name": "Smita",
        "last_name": "Aghav",
        "shift_sum": "7:01"
      },
      {
        "shift_id": 28138,
        "employee_clock_in_time": "March 24, 2025 11:09 am",
        "employee_clock_out_time": None,
        "first_name": "Nitant",
        "last_name": "Jatale",
        "shift_sum": "00:00"
      },
      {
        "shift_id": 28137,
        "employee_clock_in_time": "March 24, 2025 11:00 am",
        "employee_clock_out_time": "March 24, 2025 6:00 pm",
        "first_name": "Kalind",
        "last_name": "Joshi",
        "shift_sum": "7:00"
      },
      {
        "shift_id": 28136,
        "employee_clock_in_time": "March 24, 2025 11:00 am",
        "employee_clock_out_time": "March 24, 2025 1:56 pm",
        "first_name": "FNU",
        "last_name": "Jannat",
        "shift_sum": "2:55"
      },
      {
        "shift_id": 28135,
        "employee_clock_in_time": "March 24, 2025 10:55 am",
        "employee_clock_out_time": None,
        "first_name": "Savana",
        "last_name": "Patel",
        "shift_sum": "00:00"
      },
      {
        "shift_id": 28133,
        "employee_clock_in_time": "March 24, 2025 10:27 am",
        "employee_clock_out_time": "March 24, 2025 3:35 pm",
        "first_name": "Sai Venkata",
        "last_name": "Dhanush Amirinenii",
        "shift_sum": "5:08"
      },
      {
        "shift_id": 28132,
        "employee_clock_in_time": "March 24, 2025 10:02 am",
        "employee_clock_out_time": None,
        "first_name": "Ibiye",
        "last_name": "Bright",
        "shift_sum": "00:00"
      },
      {
        "shift_id": 28131,
        "employee_clock_in_time": "March 24, 2025 10:00 am",
        "employee_clock_out_time": "March 24, 2025 3:01 pm",
        "first_name": "McKenzie",
        "last_name": "Lynn Kovach",
        "shift_sum": "5:00"
      },
      {
        "shift_id": 28130,
        "employee_clock_in_time": "March 24, 2025 10:00 am",
        "employee_clock_out_time": "March 24, 2025 5:00 pm",
        "first_name": "Nithish Reddy",
        "last_name": "Mannem",
        "shift_sum": "6:59"
      },
      {
        "shift_id": 28128,
        "employee_clock_in_time": "March 24, 2025 10:00 am",
        "employee_clock_out_time": None,
        "first_name": "Sanath",
        "last_name": "Desai",
        "shift_sum": "00:00"
      },
      {
        "shift_id": 28129,
        "employee_clock_in_time": "March 24, 2025 10:00 am",
        "employee_clock_out_time": "March 24, 2025 3:00 pm",
        "first_name": "Sanath",
        "last_name": "Desai",
        "shift_sum": "5:00"
      },
      {
        "shift_id": 28127,
        "employee_clock_in_time": "March 24, 2025 10:00 am",
        "employee_clock_out_time": None,
        "first_name": "valerie",
        "last_name": "Osaweedoh",
        "shift_sum": "00:00"
      },
      {
        "shift_id": 28126,
        "employee_clock_in_time": "March 24, 2025 9:56 am",
        "employee_clock_out_time": "March 24, 2025 4:59 pm",
        "first_name": "Sai Swethan",
        "last_name": "Durganala",
        "shift_sum": "7:02"
      },
      {
        "shift_id": 28125,
        "employee_clock_in_time": "March 24, 2025 9:05 am",
        "employee_clock_out_time": None,
        "first_name": "Sarah",
        "last_name": "Patil",
        "shift_sum": "00:00"
      },
      {
        "shift_id": 28124,
        "employee_clock_in_time": "March 24, 2025 9:03 am",
        "employee_clock_out_time": "March 24, 2025 4:05 pm",
        "first_name": "Hepsiba Grace",
        "last_name": "Boddu",
        "shift_sum": "7:01"
      },
      {
        "shift_id": 28123,
        "employee_clock_in_time": "March 24, 2025 9:00 am",
        "employee_clock_out_time": "March 24, 2025 4:08 pm",
        "first_name": "Rakshitha Reddy",
        "last_name": "Potu",
        "shift_sum": "7:08"
      },
      {
        "shift_id": 28122,
        "employee_clock_in_time": "March 24, 2025 9:00 am",
        "employee_clock_out_time": "March 24, 2025 4:00 pm",
        "first_name": "MeherSuneel",
        "last_name": "Meesala",
        "shift_sum": "7:00"
      },
      {
        "shift_id": 28121,
        "employee_clock_in_time": "March 24, 2025 8:59 am",
        "employee_clock_out_time": None,
        "first_name": "Jonathan.",
        "last_name": "Almeida",
        "shift_sum": "00:00"
      },
      {
        "shift_id": 28120,
        "employee_clock_in_time": "March 24, 2025 8:59 am",
        "employee_clock_out_time": None,
        "first_name": "Jonathan.",
        "last_name": "Almeida",
        "shift_sum": "00:00"
      },
      {
        "shift_id": 28119,
        "employee_clock_in_time": "March 24, 2025 8:59 am",
        "employee_clock_out_time": "March 24, 2025 1:59 pm",
        "first_name": "Haren",
        "last_name": "Akula",
        "shift_sum": "5:00"
      },
      {
        "shift_id": 28118,
        "employee_clock_in_time": "March 24, 2025 8:58 am",
        "employee_clock_out_time": None,
        "first_name": "Arpita",
        "last_name": "Arpita LNU",
        "shift_sum": "00:00"
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
            background-color: #f44336; /* Black for not scheduled */
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