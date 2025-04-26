""" 
Summary:
--------
Program to convert between base 10 and binary. 

Pseudo Code:
------------
START
    PRINT "This application will convert numbers from base 10 to binary and from binary to base 10"
    
    PRINT "The first input is asking for you to enter the starting base, you should enter either '10' or '2'"
    
    TRY:
        PROMPT user to input the base (should be '10' or '2')
        CONVERT input to an integer
        IF conversion fails, PRINT error and EXIT
    
        PROMPT user to input the number to convert
        CONVERT input based on the base:
            IF base is 10:
                CONVERT number from decimal (base 10) to binary
                PRINT binary result
            ELSE IF base is 2:
                CHECK if input is a valid binary number
                CONVERT from binary (base 2) to decimal
                PRINT decimal result
            ELSE:
                RAISE error for unsupported base
    EXCEPT:
        PRINT "Invalid input. Please enter valid numbers."

    PRINT "Conversion complete."
END
"""
print("This application will convert numbers from base 10 to binary and from binary to base 10")
print("The first input is asking for you to enter the starting base, you should enter either '10' or '2'")
base = int(input("Please enter the starting base, enter '10' or '2': "))
number = int(input("Please enter the number you would like to convert: "))


def base_conversion(base, number):
    
    try:
        if base == 10:
            result = []

            original_number = number
            while number > 0:
                remainder = number % 2
                result.append(remainder)
                number = number // 2
            result.reverse()  # Reverse list after loop finishes
            result_string = "".join(map(str, result))  # Convert list to string

            print(f'The base 10 number {original_number} as a binary number is: {result_string}')
            return result_string  # Return correct binary representation

        elif base == 2:
            # Convert binary (string) to decimal
            try:
                decimal_number = int(str(number), 2)  # Convert binary string to decimal
                print(f'The binary number {number} as a base 10 number is: {decimal_number}')
                return decimal_number
            except ValueError:
                print("Error: Invalid binary number.")
                return None
        else:
            raise ValueError("Unsupported base. Only base 10 and base 2 are allowed.")
    except ValueError as e:
        print(f"Error: {e}")  # Or handle it another way


base_conversion(base, number)
