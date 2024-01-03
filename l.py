import time
start = time.time()

#Iterative sum
total = 0
# iterative through 5 million numbers
for item in range (0, 10000000):
    total=total+item

print ('sum is : '+ str(total))
end = time.time()
print (end-start)
