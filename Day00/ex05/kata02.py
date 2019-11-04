t = (3,30,2019,9,25)

for number in t:
    if (number < 10):
        number = '0' + str(number)
print(str(t[3]) + '/' + str(t[4]) + '/' + str(t[2]) + ' ' + str(t[0]) + ':' + str(t[1]))