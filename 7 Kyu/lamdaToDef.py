from re import sub
def convert_lambda_to_def(string):
    return sub(r'(\w+) = lambda ([^:]+): (.*)$', r'def \1(\2):\n    return \3', string)


print(convert_lambda_to_def("func = lambda a, b: a * b"))