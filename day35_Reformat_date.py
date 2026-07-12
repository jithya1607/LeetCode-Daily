#35 Reformat date
# Given a date string in the format "Day Month Year", reformat the date string to the format "YYYY-MM-DD".
def reformatDate(date):
    a=date.split()
    m={"Jan":'01', "Feb":'02', "Mar":'03', "Apr":'04', "May":'05', "Jun":'06', "Jul":'07', "Aug":'08', "Sep":'09', "Oct":'10', "Nov":'11', "Dec":'12'}
    if len(a[0][:-2])==2:
        return f'{a[2]}-{m[a[1]]}-{a[0][:-2]}'
    else:
        return f'{a[2]}-{m[a[1]]}-0{a[0][:-2]}'