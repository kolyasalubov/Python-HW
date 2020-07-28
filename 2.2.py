num=str(input("Enter number: "))   
result=int(num[0])*int(num[1])*int(num[2])*int(num[3])
print("Result: ", result)
print("Reversed number: ", list(reversed(num)))
print("Sorted: ", sorted(num))

в першій стрічці str не потрібно, input завжди повертає стрінгу
