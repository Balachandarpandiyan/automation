

# Q2 write a python code using lambda function to check every elements of a list an integer or string?

sample = [1, 'hello', 3.14, 'world', 42]

check_type = lambda x: 'integer' if isinstance(x, int) else 'string' if isinstance(x, str) else 'other'
result = list(map(check_type, sample))
print(result)
