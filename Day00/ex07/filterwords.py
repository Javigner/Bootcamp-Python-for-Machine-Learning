import sys

if (len(sys.argv) != 3 or sys.argv[1].isnumeric() == True or sys.argv[2].isnumeric() == False):
    print('ERROR')
    sys.exit()
String = " ".join(sys.argv[1].split())
l = String.split(' ')
result = []
for element in l:
    if (len(element) == int(sys.argv[2])):
        result.append(element)
print(result)
    