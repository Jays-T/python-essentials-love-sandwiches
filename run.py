from updaters_calculators import calculate_surplus_data, setup_subscribers
from validators import validate_length, convert_to_int
from events import post_event



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
Use post_event to update worksheets
Parameters:  post_event(event_type: str, worksheet: str, data)
"""


def start_program():
    """
    Get sales data
    """
    while True:
        sales_data = get_sales_data()

        print(f"Your sales data is: {sales_data}")
        print("Is this correct? ")

        check_input = input("Write 'yes' and hit enter to update sales data,\n Write 'no', 'cancel' or leave blank and hit enter to start again...\n")
        if check_input == "yes":
            post_event("update_sales", "sales", sales_data)
            break

    surplus_data = calculate_surplus_data(sales_data)

    post_event("update_surplus", "surplus", surplus_data)


def get_sales_data():
    """
    Get sales figures from user input
    Data must be six values
    Values must be convertible to Int
    """
    while True:
        print("Data must be six numbers separated by commas.")
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


def main():
    """
    Welcome message
    """
    setup_subscribers()

    print("Welcome to love sandwiches\n")
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
