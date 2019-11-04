phrase = "The right format"

count = 42 - len(phrase)
String = ''
while(count > 0):
    String = String + '-'
    count = count -1
print(String + phrase)