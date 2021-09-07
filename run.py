from updaters_calculators import setup_calc_updater_subscribers
from getters import setup_getter_subscribers
from events import post_event, return_data_event, show_data_event


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

"""
If adding functionality to start_program
First setup subscribers:
Parameters: subscribe(event_type: str, fn)

Use post_event to call updaters:
e.g: Update worksheets

Event types: update_sheet

Use return_data_event to call calculators:
    * pass data
    * run calculations
    * return calculated data
e.g: calculate sales, calculate surplus, calculate stock

Event types: return_surplus, calculate_stock, get_last_5_day_sales

Parameters:  ....event(event_type: str, worksheet: str, data)

"""


def start_program():
    """
    Get sales data
    """
    current_user = {}
    user = input("Please input your name\n")
    current_user["Name:"] = user
    user = current_user["Name:"]

    print(f"Welcome {user}!\n")
    while True:
        sales_data = return_data_event("get_sales", user)

        print(f"{user} your sales data is: {sales_data}")
        print("Is this correct? ")

        check_input = input("Write 'yes' and hit enter to update sales data...\nWrite 'no', 'cancel' or leave blank and hit enter to input data again...\nWrite 'exit' and hit enter to exit the program...\n")
        if check_input == "yes":
            break
        if check_input == "exit":
            print("Exiting.....\nThank you for using Love Sandwiches data automation.")
            return

    post_event("update_sheet", "sales", sales_data)

    surplus_data = return_data_event("return_surplus", sales_data)

    post_event("update_sheet", "surplus", surplus_data)

    last_5_day_sales = return_data_event("get_last_5_day_sales", "sales")

    calculated_stock = return_data_event("calculate_stock", last_5_day_sales)
    
    post_event("update_sheet", "stock", calculated_stock)

    print(f"{user} we'll recommend your stock numbers...\n")

    show_data_event("get_stock_suggestions", "stock")

    print(f"\nAll done {user}! Thank you for using Love Sandwiches data automation!\n")


def main():
    """
    Welcome message
    """
    setup_calc_updater_subscribers()
    setup_getter_subscribers()

    print("Welcome to love sandwiches data automation\n")
    print("Update your daily sales totals,\ncalculate surplus numbers.")
    print("Calculate the daily average sales over the last 5 market days,")
    print("and get stock recommendations\n")
    begin_program = input("Write 'start' and then hit enter to begin.... or hit enter to close the program\n")

    if begin_program == "start":
        start_program()
    else:
        print("Alright, we'll calculate the stock some other time.")
        return


main()
