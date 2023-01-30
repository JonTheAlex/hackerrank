def timeConversion(s):
    time = s.split(':')
    hour = int(time[0])
    min = time[1]
    sec = time[-1][:2]
    meridien = s.find('PM')
    
    if meridien != -1:
        if hour < 12:
            hour += 12
        else:
            hour = 12

    else: 
        if hour == 12:
            hour = 0            
            
    return f'{str(hour).zfill(2)}:{min}:{sec}'


print(timeConversion('06:40:03AM'))
