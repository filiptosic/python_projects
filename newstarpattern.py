x = int(input("enter number of rows: "))
star = str(input("enter a symbol: "))
pattern = star
for i in range(x):
    print(pattern)
    pattern += star

y = int(input("enter number of rows: "))
pattern2 = str(input("Enter a symbol to be repeated: "))
i = 0
symbol = pattern2
while i <= y:
    print(symbol)
    symbol += pattern2
    i += 1


