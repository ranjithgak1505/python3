def generator_function(token_count):
    for i in range(token_count):
        yield i
variable= generator_function(10)
for i in range(10):
    print(next(variable))

print()
         
