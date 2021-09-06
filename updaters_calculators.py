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


def setup_subscribers():
    subscribe('update_sheet', update_worksheet)
    subscribe('return_surplus', calculate_surplus_data)
