A = int(input("Enter your first no. A: "))
B = int(input("Enter your second no. B: "))

result = 1
for i in range(B):
    result *= A

print("A^B =", result)
