def findMultiples(n):
    sum = 0
    count = 0
    for i in range (1, 1000):
        if (i % 3 == 0 or i % 5 == 0):
            sum += i
            count = count + 1
    print(sum)
    print(count)
    return sum

findMultiples(1000)


