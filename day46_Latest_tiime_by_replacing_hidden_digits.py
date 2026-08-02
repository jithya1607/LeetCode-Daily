#46 Latest time by replacing hidden digits
#Replace the hidden digits in a given time string to create the latest possible time.
def maximumTime(time):
    lt={3:'5',4:'9'}
    new_time=''
    for i in range(len(time)):
        if time[i]=='?':
            if i in lt:
                new_time+=lt[i]
            else:
                if i==0:
                    if time[1] in '456789':
                        new_time+='1'
                    else:
                        new_time+='2'
                if i==1:
                    if time[0]=='0' or time[0]=='1':
                        new_time+='9'
                    else:
                        new_time+='3'
        else:
            new_time+=time[i]
    return new_time