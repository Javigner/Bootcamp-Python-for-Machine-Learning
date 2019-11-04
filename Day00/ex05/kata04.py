t = ( 0, 4, 132.42222, 10000, 12345.67)

day = ''
exo = ''
note1 = ''
note2 = ''
note3 = ''
if (t[0] < 10 and t[0] >= 0):
    day = 'day_0' + str(t[0]) + ', '
elif t[0] >= 10:
    day = 'day_' + str(t[0]) + ', '
if (t[1] < 10 and t[1] >= 1):
    exo = 'ex_0' + str(t[1]) + ' : '
elif t[1] >= 10:
    exo = 'ex_' + str(t[1]) + ' : '
note1 = "%.2f" % t[2]
note2 = "%0.2e" % t[3]
note3 = "%0.2e" % t[4]
print(day + exo + str(note1) + ', ' + str(note2) + ', ' + str(note3))
    