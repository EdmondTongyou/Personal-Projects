def cassini(number):
    if number <= 1:
        return 1
    return ((pow(number, -1) + cassini(number - 1) * cassini(number - 1))/cassini(number - 2))

print("The Fibbonacci Sequence using the Cassini identity for 1-10 is:")
for index in range(0, 10):
    print(int(cassini(index)))
