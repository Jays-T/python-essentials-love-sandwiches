from events import subscribe
from scope import SHEET
from pprint import pprint
from validators import validate_length, convert_to_int

def get_sales_data(user):
    """
    Get sales figures from user input
    Data must be six values
    Values must be convertible to Int
    """
    while True:
        print(f"{user}, your data must be six numbers separated by commas.")
        print("Example: 10,20,30,40,50,60\n")

        data_as_str = input("Enter your data here: \n")
        data_split = data_as_str.split(',')
        """
        Should be six values,
        Should be able to convert str to int
        """
        if validate_length(data_split):
            data_as_int = convert_to_int(data_split)
            if data_as_int:
                break

    return data_as_int


def get_last_5_entries(sheet):
    """
    Collect columns of data from sales worksheet
    Get last 5 entries for each sandwich and return data
    as list of lists

    Six columns to loop over
    Range is (1,7) as col_values indexes from 1, not 0
    """
    sales = SHEET.worksheet(sheet)

    columns = []
    print("Collecting sales numbers from last 5 days....\n")
    for col in range(1,7):
        column = sales.col_values(col)
        sandwich_name = column[0]
        sandwiches_sold = column[-5:]
        
        columns.append(sandwiches_sold)

        print(f"| Name: {sandwich_name} - Last 5 day sales: {sandwiches_sold}")
    print("\nLast 5 day sales shown above....\n")
    return columns


def setup_getter_subscribers():
    subscribe('get_sales', get_sales_data)
    subscribe('get_last_5_day_sales', get_last_5_entries)
