num = int(input("Enter a number: "))
di = dict()

for x in range(1, num + 1):
    di.update({x : x**2})

print(di)
