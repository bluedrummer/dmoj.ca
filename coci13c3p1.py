
nb_of_times_butt_is_pressed = int(input()) + 1
fib_array = [0]*nb_of_times_butt_is_pressed
fib_array[0] = 0
fib_array[1] = 1
def fibonacci(n):
    if n > 1:
        for i in range(2, n):
            fib_array[i] = fib_array[i-1] + fib_array[i-2]
fibonacci(nb_of_times_butt_is_pressed)
count_of_a = fib_array[-2]
count_of_b = fib_array[-1] 

print(str(count_of_a) + " " + str(count_of_b))