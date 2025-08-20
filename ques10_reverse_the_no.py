# getting input from user
num = int(input("Enter a number to check if it's a palindrome: "))

# save a original number value
original_number = num

reversed_number = 0
# reverse the number
while num > 0:
    digit = num % 10
    reversed_number = (reversed_number * 10) + digit
    num = num // 10

# cheaking
if original_number == reversed_number:
    print(original_number, "is a palindrome.")
else:
    print(original_number, "is not a palindrome.")