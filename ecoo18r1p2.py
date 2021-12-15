for n in range(0, 10):
    number_of_routes = int(input())
    routes = {}
    min_number = 100000
    output_string = ""
    output_ans = ""
    for i in range(0, number_of_routes):
        tmp_line = list(map(int,input().split()))
        routes[tmp_line[0]] = tmp_line[2:]
        routes[tmp_line[0]].sort()
    for k,v in routes.items():
        if min_number > min(v):
            min_number = min(v)
    for k,v in routes.items():
        if min_number == min(v):
            output_string = output_string + str(k) + " "
    output_string = list(map(int,output_string.split()))
    output_string.sort()
    output_string = list(map(str,output_string))
    output_string = ','.join(list(map(str,output_string)))
    output_ans = str(min_number) + " {" + str(output_string)
    output_ans = output_ans.rstrip()
    output_ans = output_ans.rstrip(",")
    output_ans = output_ans + "}"
    print(output_ans)
