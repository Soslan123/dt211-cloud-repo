Total = 0
for i in range(1,1000):
    if (i%3 == 0) or (i%5 == 0): # if the value in i is divisible by 3 or 5 then
        Total +=  i              # all the values that are divisible by 3 or 5                                                                   # will be incremented to Total
print (Total)

