times_measured = int(input())
times_measured = int(input())
water_readings = input().split()
diffrence = 0
previous_value = 0
check_flag = "false"

if times_measured > 3:
    water_readings = list(map(int, water_readings))
    diffrence = max(water_readings) - min(water_readings)

    for n in range(0, times_measured):
        if water_readings[n] == min(water_readings):
            check_flag = "true"
        elif check_flag == "true":
            if previous_value >= water_readings[n]:
                print("unknown")
                break
            elif water_readings[n] == max(water_readings):
                print(diffrence)
                break
        previous_value = water_readings[n]

elif times_measured <= 3:
        print("unknown")
