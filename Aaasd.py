for x in range(1, 100):
    if x % 15 == 0:
        print("fizzbuzz")
    else:
        if x % 5 == 0:
            print("buzz")
        else:
            continue

        if x % 3 == 0:
            print("fizz")
    print(x)
