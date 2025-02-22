def function(a, b):
    if b == 0:
        return "Division by zero!"  #Handle the error
    else:
        return a / b

result = function(10, 0)
print(result) # Output: Division by zero!