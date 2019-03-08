numsEven = []
numsOdd = []
def checkIfEven(n):
    if (n % 2 == 0):
        # print ("Number is even")
        numsEven.append(n)
        return n
    else:
        # print("number is odd")
        numsOdd.append(n)


# fibonacci Sequence
def recur_fib(n):
    # recursive function to print fibonacci sequence
    if n <= 1:
        return n
    else:
        return(recur_fib(n-1) + recur_fib(n-2))


nterms = 89
sum = 0
limit = 4000000

# Calculate the fib sequence, check if it is under 4,000,000
# add sum of even integers

if nterms <= 0:
    print("Please enter a positive integer")
else:
    print("Fibonacci sequence:")
    for i in range(nterms):
        if recur_fib(i) >= limit:
            for i in range(len(numsEven)):
                sum += numsEven[i]    
            print("The sum of even numbers up to 4,000,000 is: " + str(sum)) 
            exit()
        else:
            checkIfEven(recur_fib(i))
            print(recur_fib(i))


            
# def gen_fib():
#     count = int(input("How many fibonacci numbers would you like to generate? "))
#     i = 1
    
#     if count == 0:
#         fib = []
#     elif count == 1:
#         fib = [1]
#     elif count == 2:
#         fib = [1,1]
#     elif count > 2:
#         fib = [1, 1]
#         while i < (count - 1):
#             fib.append(fib[i] + fib[i-1])
#             i += 1   
#         return print(fib)
