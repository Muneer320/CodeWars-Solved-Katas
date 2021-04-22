def rgb1(r, g, b):
    round = lambda x: min(255, max(x, 0))
    return ("{:02X}" * 3).format(round(r), round(g), round(b))

def rgb2(r, g, b):
    #your code here :)
    
    def OctToHex(num):
      if num <= 0:
        return "00"
      elif num >= 255:
        return "FF"
      mapping = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
      tmp = ""
      while num > 0:
        num, mod = divmod(num, 16)
       #print num, mod
        tmp += mapping[mod]
        
      return tmp[::-1] if len(tmp) == 2 else "0" + tmp
    
    return OctToHex(r) + OctToHex(g) + OctToHex(b)

print(rgb1(111,111,111))

print("\n\n\t\t\t**********Alternate Way**********\n\n")

print(rgb2(111,111,111))