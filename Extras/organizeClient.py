def organize(client):
    result = {"Name": "", "Age": '',"Hobbies": '', "Occupation": ''}

    for var in client:
        if type(var) == type(""): 
            result.update(Name = var)

        elif type(var) == type(1): 
            result.update(Age = var)

        elif type(var) == type(()): 
            result.update(Hobbies = var)

        elif type(var) == type(True):
            result.update(Occupation = var)
    
    result_ = {}

    for key, value in result.items():
        if value != '':
            result_[key] = value
    
    return result_
    


print(organize([23, True, 'John']))