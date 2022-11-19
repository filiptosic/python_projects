x = int(input("enter number of rows: "))
star = str(input("enter a symbol: "))
pattern = star
for i in range(x):
    print(pattern)
    pattern += star
while True:
    try:
        y = int(input("Please enter a number of rows: "))
    except ValueError:
        print("Number of rows must be entered as integer.")
        continue
    else:
        break
pattern2 = str(input("Enter a symbol to be repeated: "))
i = 0
symbol = pattern2
while i <= y:
    print(symbol)
    symbol += pattern2
    i += 1
