import gspread
from google.oauth2.service_account import Credentials


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('love_sandwiches')

"""
Main functions
1) Collect sales data from User / Check that input is valid
2) Add sales data into worksheet
3) Calculate surplus numbers
4) Add surplus data to worksheet
5) Calculate the average sales for the last 5 market days
6) Add calculated stock numbers into stock worksheet
7) Print stock recommendations to terminal
"""

"""
Workflow
start program:

1) Request sales data from user
Is data valid?
No = Print error message, return to step 1
Yes = go to step 2
2) Parse sales data, use correct format for worksheet
3) Update worksheet
4) Calculate surplus values Sales - Stock
5) Update surplus worksheet
6) Calculate stock data based on averages over last 5 market days
7) Update stock worksheet with calculated values
8) Pair stock calculations with original sandwich types
9) Print data to terminal

end program
"""


def get_sales_data():
    """
    Get sales figures from user input
    """
    print("Welcome to love sandwiches.")
    print("Data should be six numbers separated by commas.\n")
    print("Example: 10,20,30,40,50,60\n")

    sales_data_str = input("Enter your data here: \n")
    print(f"The data provided is: {sales_data_str}")

get_sales_data()