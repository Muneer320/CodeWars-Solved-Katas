tap_code_translation1=lambda s:' '.join(-~z*'.'for c in s for z in divmod(ord(c*(c!='k')or'c')-97-(c>'k'),5))


print(tap_code_translation1('muneer alam'))