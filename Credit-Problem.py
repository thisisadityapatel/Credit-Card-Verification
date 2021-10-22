'''
|--------------------------|
| Credit-Card-Verification |
|--------------------------|

Program Function: 
----------------
This program simply takes any credit card number as input and checks if the card entered is valid or not,
if valid it shows the users what company the card belongs to, i.e. American Express, Mastercard or Visa.

Principle used:
---------------
-> Hans Peter Luhn of IBM made an algorithm that could be used for the verification of the credi card numbers.
   The principle used was:
    1. Multiplying every other digit with 2, starting with the second last digit and then adding them all together.
    2. Adding the rest of the digits to the sum. (these are the digits that werent multiplied with two.)
    3. If the sum of all the digits in the numbers, is divisible by 10 with 0 remainder, than the card number entered is valid.

-> To determine what company the card belongs to, there are various standards set by the companies as follows:
    1. American Express : 15 digits, starts with 34 or 37
    2. MasterCard : 16 digits, starts with 51, 52, 53, 54, or 55
    3. Visa : 13 or 16 digits , starts with 4.

Example Inputs:
---------------
378282246310005 as American Express
371449635398431 as American Express
5555555555554444 as MasterCard
5105105105105100 as MasterCard
4111111111111111 as Visa
4012888888881881 as Visa
1234567890 as INVALID
369421438430814 as INVALID
4062901840 as INVALID
5673598276138003 as INVALID
4111111111111113 as INVALID
4222222222223 as INVALID

'''

# Defining the main function
def main():
    # Prompt the user for input
    n = int(input("Enter the credi card number : "))
    number = n

    # Converting the number into a list
    lst = []
    temp = []
    while number > 0:
        r = number % 10
        lst.append(r)
        temp.append(r)
        number = number // 10

    # Checkting the validity of the card number entered.
    validity = check_valid(lst)
    
    # Condition if the card numbers is invalid
    if validity == False:
        print("Invalid Card Number !!")
    
    size = len(temp)
    flag = 0

    # Conditions is the card number entered is valid
    if validity == True:
        
        # Condition is card number is not of the correct size
        if size != 15 and size != 16 and size != 13:
            print("Invalid Card Number !!")
            flag = 1
        
        # Condition to check if the card is American Express
        elif size == 15:
            if temp[size-1] == 3:
                if temp[size-2] == 4 or temp[size-2] == 7 :
                    print("American Express")
                    flag = 1
        
        # Condition to check if the card is Mastercard or Visa
        elif size == 16:
            if temp[size-1] == 5:
                if temp[size-2] == 1 or temp[size-2] == 2 or temp[size-2] == 3 or temp[size-2] == 4 or temp[size-2] == 5:
                    print("MasterCard")
                    flag = 1
            elif temp[size-1] == 4:
                print("Visa")
                flag = 1

        # Checking if the card is Visa 
        elif size == 13:
            print("Visa")
            flag = 1
        
        # Other card numbers
        if flag == 0:
            print("Invalid Card Number !!")


# Function to check the validity of the card entered
# Hans Peter Luhn of IBM made an algorithm that could be used for the verification of the credi card numbers
def check_valid(list):
    size = len(list)

    for i in range(1, size, 2):
        list[i] = list[i] * 2

    sum = 0
    for j in list:
        while j > 0:
            remainder = j % 10
            sum = sum + remainder
            j = j // 10
    
    # If the sum is divisible by 10
    if sum % 10 == 0:
        return True
    else:
        return False

if __name__ == "__main__":
    main()

