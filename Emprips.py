import  math as m
def find_emirp(n):
    fir_primes = []
    primes_set = {}
    nex_emrips=[]
    final_emprips = []

    def check_prime(i):
        cntr = 0
        if len(str(i))>1:
            if i in primes_set.values():
                return True
            elif i % 2 == 0:
                return False
            elif i%m.sqrt(i) == 0:
                return False
            else:
                breaker = m.ceil(m.sqrt(i))
                for ii in range(3,int(breaker),2):
                    if i%ii == 0:
                        return False
                cntr += 1
                primes_set[cntr]=i
                return True
    def is_palindrome(pn):
        strpn = str(pn)
        if len(strpn)%2 ==0:
            mid = len(strpn)//2
            x = mid +1
            final_len  = len(strpn)
            first_half = strpn[0:mid]
            secnd_half = strpn[mid: final_len]
            if first_half == secnd_half:
                return True
            else:
                return False
        elif len(strpn) >2 and len(strpn)%2 != 0:
            #print("Number is ",pn)
            mid = len(strpn) // 2
            x = mid
            y = mid + 1
            final_len = len(strpn)
            first_half = strpn[0:x]
            secnd_half = strpn[y: final_len]
            #print("First half ->", first_half, " ,Second half->  ", secnd_half)
            if first_half == secnd_half[::-1]:
                #print("First half ->", first_half, " ,Second half->  ", secnd_half)
                return True
            else:
                #print("First half ->", first_half, " ,Second half->  ", secnd_half)
                return False
        else:
            return False
    for ii in range(n):
        if check_prime(ii) == True:
            rev = int(str(ii)[::-1])
            if rev not in primes_set.values():
                if check_prime(rev) == True:
                    if is_palindrome(ii) == False:
                        if ii < n:
                            nex_emrips.append(ii)
    if len(nex_emrips)>1:
        nex_emrips.reverse()
        final_emprips.append(len(nex_emrips))
        final_emprips.append(nex_emrips[0])
        final_emprips.append(sum(nex_emrips))
        return final_emprips
    else:
        final_emprips.append(0)
        final_emprips.append(0)
        final_emprips.append(0)
        return final_emprips
