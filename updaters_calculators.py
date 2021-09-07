from scope import SHEET
from pprint import pprint

from events import subscribe


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
        print(f"| Name: {name} - Stock: {stock} - Sold: {sales} = Remaining stock: {surplus}")
    
    print("\n")
    return stock_surplus


def calculate_stock_data(sales_column):
    """
    Calculate average stock for each item type, adds 10%
    """
    print("Calculating stock data....\n")
    new_stock_data = []
    for column in sales_column:
        int_column = [int(num) for num in column]
        average_sales = sum(int_column) / len(int_column)
        suggested_stock = average_sales * 1.1
        new_stock_data.append(round(suggested_stock))

    return new_stock_data


def show_final_stock_suggestions(sheet):
    """
    Return next day stock suggestions for each sandwich
    """
    print(f"Coalating results for stock suggestions....\n")
    stock = SHEET.worksheet(sheet).get_all_values()
    sandwich_names = stock[0]
    last_stock_row = stock[-1]

    stock_suggestions = {}
    print("Suggest stock numbers below....\n")
    for sandwich_name, stock_num in zip(sandwich_names, last_stock_row):
        print(f"| Name: {sandwich_name} - Suggested amount to stock: {stock_num}")
        stock_suggestions[sandwich_name] = stock_num

    return stock_suggestions

def setup_calc_updater_subscribers():
    subscribe('update_sheet', update_worksheet)
    subscribe('return_surplus', calculate_surplus_data)
    subscribe('calculate_stock', calculate_stock_data)
    subscribe('get_stock_suggestions', show_final_stock_suggestions)
