def gen_primes():
  D = {}
  q = 2  # first integer to test for primality.

  while True:
    if q not in D:
      # not marked composite, must be prime  
      yield q 

      #first multiple of q not already marked
      D[q * q] = [q] 
    else:
      for p in D[q]:
        D.setdefault(p + q, []).append(p)
      # no longer need D[q], free memory
      del D[q]

    q += 1

primes = gen_primes()
a = 10
for p in primes:
    print(p)
    a += 1
    if a == 10:
        break
