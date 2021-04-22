def validBraces1(string):
    parenthesis = []
    pardict = {"{":"}", "[":"]", "(":")", "}":"{", "]":"[", ")":"("}
    for i in range(len(string)):
        if string[i] == "(" or string[i] == "[" or string[i] == "{":
            parenthesis.append(string[i])
        else:
            if len(parenthesis) == 0:
                return False
            elif pardict[string[i]] == parenthesis[len(parenthesis)-1]:
                del parenthesis[len(parenthesis)-1]
            else:
                return False
    if len(parenthesis) != 0:
        return False
    return True

def validBraces2(s):
  while '{}' in s or '()' in s or '[]' in s:
      s=s.replace('{}','')
      s=s.replace('[]','')
      s=s.replace('()','')
  return s==''

if validBraces1('[{()()}]'):
    print("it's true")
else:
    print('False')

print("\n\n\t\t\t**********Alternate Way**********\n\n")

if validBraces2('[{()()}]'):
    print("it's true")
else:
    print('False')