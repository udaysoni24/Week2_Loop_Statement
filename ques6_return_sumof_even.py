
a = int(input("Enter your number :"))
sum = 0
for i in range(2, a + 1, 2):
	sum += i
print("Sum of even numbers from 1 to", a, "is:",sum)
