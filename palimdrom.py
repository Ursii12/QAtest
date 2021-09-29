x = input("Elementul : ")
if len(x)>2 :
        y = ''
        for i in x:
            y = i + y
        if x == y:
                 print("Elementul este palindrom")
        else:
                  print("Elementul nu este palindrom")
else :
    print("Nu se poate aflaa")