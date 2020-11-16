# Function tells number of digits at ten's place and at one's place.
def NumberOfDigits(integer):
    ones=0
    ten=0
    if integer >9 and integer <100:
        while integer > 9:
            ones+= integer%10
            integer=integer//10
            ten+=integer
    else:
        ones= integer
    return "Ten's: {}\nOne's: {}".format(ten,ones)
print(NumberOfDigits(10))

# Function to form integer from number of digits.
def Integer_from_number_of_digits(tens, ones):
    integer = (tens*10)+ones
    return integer
print(Integer_from_number_of_digits(2,2))
