
num = int(input("Enter a number: "))

# Check if the input is 0
if num == 0:
    print("It is 0")
else:
    # Check if the input is negative
    if num < 0:
        print("It is negative")
    else:
        # Convert the integer to a binary string
        bnString = ""
        while num > 0:
            remainder = num % 2
            bnString = str(remainder) + bnString
            num = num // 2

        # Convert the binary string back to an integer
        decimal_value = 0
        for i in range(len(bnString)):
            if bnString[i] == '1':
                decimal_value += 2 ** (len(bnString) - 1 - i)

        print(f"Binary: {bnString}")
        print(f"Decimal: {str(decimal_value)}")
