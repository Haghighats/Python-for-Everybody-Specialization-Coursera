import re
with open('regex_sum_1820622.txt' , 'r') as f:
    numbers = f.read()
    for line in numbers:
        y = re.findall('[0-9]+' , str(numbers))
        adad= [int(x) for x in y]
    print (sum (adad))

