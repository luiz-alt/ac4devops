def fibonacci():
    i = 1
    a, b = 1 , 1
    val = [1,1]

    while i != 50:
        c = a+b
        a, b = b, c
        val.append(c)        
        i += 1

    print (val)
