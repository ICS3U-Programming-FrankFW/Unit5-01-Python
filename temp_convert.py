# !/user/bin/env.python3
# Created By:Frankie fox
# Date: Nov. 25, 2022
# This program Makes the entered temperature
# in Celsius to Fahrenheit.


def calculate_fahrenheit():

    # this changes temperature into celsius from the user
    temp_c_string = input("Enter the temperature (°C): ")
    print("")

    try:
        # Turns user input to a float
        # It does this so can accepts decimal
        temp_c_float = float(temp_c_string)

        # calculates the fahrenheit of user input
        temp_f = (9 / 5) * temp_c_float + 32
        print("{:,.2f}°C is equal to {:,.2f}°F".format(temp_c_float, temp_f))

    # makes sure if the number is a string and says it is not a number
    except Exception:
        print("{} is not a number.".format(temp_c_string))


def main():
    calculate_fahrenheit()


if __name__ == "__main__":
    main()
