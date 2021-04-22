class RN:
  def to_roman(self, n):
    st='M'*(n//1000)+'C'*(n//100%10)+'X'*(n//10%10)+'I'*(n%10)
    for x, y, z in ['CDM', 'XLC', 'IVX']:
      st=st.replace(x*9,x+z).replace(x*5, y).replace(x*4, x+y)
    return st
    
  def from_roman(self, st):
    for x, y, z in ['CDM', 'XLC', 'IVX']:
      st=st.replace(x+y,x*4).replace(y, x*5).replace(x+z, x*9)
    return sum(st.count(x)*10**a for a, x in enumerate('IXCM'))
RomanNumerals = RN()


print(RomanNumerals.to_roman(1990))