# FILE NAME - convert_C_to_F_02.py

# NAME: Caleb Rodas
# DATE: 10/02/2025
# BRIEF DESCRIPTION: This program converts temperatures between Celsius and Fahrenheit.The user chooses the direction of conversion, enters a temperature,and the equivalent value is displayed.



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience



########## ENTER YER CODE BELOW THIS LINE ##########

def main():
    print("===== Temperature Converter =====\n")
    print("  1. Convert from Celsius to Fahrenheit")
    print("  2. Convert from Fahrenheit to Celsius\n")

    choice = input("Please choose from the above menu: ")

    temperature = float(input("Enter a temperature to convert: "))

    if choice == "1":
        # Celsius to Fahrenheit
        fahrenheit = temperature * 9/5 + 32
        print(f"\n{temperature:.1f} degrees Celsius is {fahrenheit:.1f} degrees Fahrenheit.\n")
    elif choice == "2":
        # Fahrenheit to Celsius
        celsius = (temperature - 32) * 5/9
        print(f"\n{temperature:.1f} degrees Fahrenheit is {celsius:.1f} degrees Celsius.\n")
    else:
        print("\nInvalid choice.\n")

main()


########### END YER CODE ABOVE THIS LINE ###########

    



########################################
#          SAMPLE OUTPUT
########################################

'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 1
Enter a temperature to convert: 100

100.0 degrees Celsius is 212.0 degrees Fahrenheit.
'''


'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 2
Enter a temperature to convert: 32

32.0 degrees Fahrenheit is 0.0 degrees Celsius.
'''


'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 1
Enter a temperature to convert: -40

-40.0 degrees Celsius is -40.0 degrees Fahrenheit.
'''


'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 2
Enter a temperature to convert: -40

-40.0 degrees Fahrenheit is -40.0 degrees Celsius.
'''

########################################
#          REFLECTION QUESTIONS
########################################

'''

1. What is one lesson you learned in this lab?



how to use a user input to affect a different input



'''
