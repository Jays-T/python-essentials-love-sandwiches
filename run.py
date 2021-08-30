import gspread
from google.oauth2.service_account import Credentials
from validators import validate_length, convert_to_int


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

def start_program():
    """
    Get sales data
    """
    sales_data = get_sales_data()

    """
    Should be six values
    """
    is_six = validate_length(sales_data)
    if not is_six:
        start_program()
        return
    
    """
    Should be able to convert str to int
    """
    sales_data_as_int = convert_to_int(sales_data)
    if not sales_data_as_int:
        start_program()
        return
    
    print(f"Your sales data is: {sales_data_as_int}")


def get_sales_data():
    """
    Get sales figures from user input
    Data must be six values
    Values must be convertible to Int
    """
    print("Welcome to love sandwiches. Data should be six numbers separated by commas.\n")
    print("Example: 10,20,30,40,50,60\n")

    data_str = input("Enter your data here: \n")
    data_split = data_str.split(',')
    return data_split




start_program()