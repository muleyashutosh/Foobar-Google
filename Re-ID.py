primes = '23'
def prime_generate():
    global primes
    primelist = [2,3]
    no = 5
    while True:
        #print('XXXXX')
        is_prime = True
        for x in primelist:
            if no % x == 0:
                is_prime = False
        if is_prime:
            primelist.append(no)
            primes += str(no)
        no += 2
        if len(primes) >= 10006:
            break
        

def solution(i):
    global primes
    print(primes[i:i+5])

prime_generate()
#print(len(primes))
solution(3)
