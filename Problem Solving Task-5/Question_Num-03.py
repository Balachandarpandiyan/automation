 # Q3 Using a python Lambda function create a fibonacci series from 1 to 50 elements?


def fibonacci(count):
    fibonacci_list = [0, 1]

    any(map(lambda _: fibonacci_list.append(sum(fibonacci_list[-2:])), range(2, count)))

    return fibonacci_list[:count]

print(fibonacci(50))
