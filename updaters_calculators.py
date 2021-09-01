import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint

from events import subscribe


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('love_sandwiches')


def update_worksheet(sheet, data):
    """
    Add new row to worksheet
    Update with list data provided
    """
    print(f"Updating {sheet} worksheet....\n")
    worksheet_to_update = SHEET.worksheet(sheet)
    worksheet_to_update.append_row(data)
    print(f"{sheet} worksheet successfully updated!\n")


def calculate_surplus_data(sales_row):
    """
    Compare sales with stock and calculate the surplus for each item type.
    The surplus is defined as the sales figure subtracted from the stock:
    - Positive surplus indicates waste
    - Negative surplus indicates extra made when stock was sold out.
    """
    print("Calculating surplus data....\n")
    in_stock = SHEET.worksheet("stock").get_all_values()
    sandwich_names = in_stock[0]
    last_stock_row = in_stock[-1]

    stock_surplus = []
    for name, sales, stock in zip(sandwich_names, sales_row, last_stock_row):
        surplus = int(stock) - sales
        stock_surplus.append(surplus)
        print(f"| Name: {name} - Sold: {sales} - Stock: {stock}")

    # print(f"Stock row: {last_stock_row}.")
    # print(f"sales_row: {sales_row}")
    return stock_surplus



def setup_subscribers():
    subscribe('update_sales', update_worksheet)
    subscribe('update_surplus', update_worksheet)
