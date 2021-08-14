number_of_streams = 0
stream_specification = ""
streams = []
number_of_streams = int(input())

for i in range(0, number_of_streams):
    streams.append(int(input()))
    
while stream_specification != 77:
    stream_specification = int(input())
    if stream_specification == 77:
        break
    if stream_specification == 99:
        stream_number = int(input())
        stream_percentage = int(input())
        stream_left = (streams[stream_number-1]*stream_percentage)/100.00
        stream_right = streams[stream_number-1]-stream_left
        if len(streams) == 1:
            streams = [stream_left, stream_right]
        elif stream_number == 1:
            streams = [stream_left, stream_right] + streams[1:]
        elif stream_number == len(streams):
            streams = streams[0:-1] + [stream_left, stream_right]
        else:
            streams = streams[0:stream_number-1] + [stream_left, stream_right] + streams[stream_number:]
    if stream_specification == 88:
        stream_number = int(input())
        if len(streams) == 1:
            streams = streams        
        elif len(streams) == 2:
            streams = [streams[0] + streams[1]]
        elif stream_number == 1:
            streams = [streams[0] + streams[1]] + streams[2:]
        elif stream_number == len(streams):
            streams = streams[0:-2] + [streams[-2] + streams[-1]]
        else:
            streams = streams[0:stream_number-1] + [streams[stream_number-1] + streams[stream_number]] + streams[stream_number+1:]
            
answer=[]
for i in range(0, len(streams)):
    answer.append(str(round(streams[i])))    
print(' '.join(answer))
    