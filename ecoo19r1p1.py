for n in range(0, 10):
    stats = input()
    events = input()
    dirty_shirts = 0
    laundry_count = 0
    number_of_shirts = int(stats.split()[0])
    days_with_event = events.split()
    clean_shirts = int(stats.split()[0])
    number_of_events = int(stats.split()[1])
    number_of_days = int(stats.split()[2])
    days_with_event.sort()
    for d in range(1, number_of_days+1):
        if clean_shirts == 0:
            clean_shirts += number_of_shirts
            laundry_count += 1
        clean_shirts -= 1
        clean_shirts += days_with_event.count(str(d))
        number_of_shirts += days_with_event.count(str(d))
    print(laundry_count)
        
      