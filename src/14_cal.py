"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py month [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
"""

import sys
import calendar
from datetime import datetime


def user_calendar():

	print('enter month and year: ')
	user_input_value = input()

	if user_input_value == '':
		current_month = calendar.month(2019, 8, w=0, l=0)
		print(current_month)

	user_input_list = user_input_value.split(' ')
	
	if len(user_input_value) == 1 and int(user_input_list[0])<=12:
		current_month = calendar.month(2019, (int(user_input_list[0])), w=0, l=0)
		print(current_month)

	if len(user_input_list) == 2 and (int(user_input_list[0])) <=12:
		current_month = calendar.month((int(user_input_list[1])), (int(user_input_list[0])), w=0, l=0)
		print(current_month)

	if len(user_input_list) == 2 and (int(user_input_list[1])) <=12:
		current_month = calendar.month((int(user_input_list[0])), (int(user_input_list[1])), w=0, l=0)
		print(current_month)

	else:
		return print('The expected format is : MM, YYYY')


user_calendar()