a = "ababaa"
sufi = ''
cont = len(a)

for i in range(len(a) - 1):
    sufi2 = a[i+1:]
    sufi += a[i]
    print(sufi)
    if len(sufi2) >= 1:
        for j in range(len(sufi)):
            if sufi[j] != sufi2[j]:
                break
            elif sufi[j] == sufi2[j]:               
                
    
print(cont)


Given an integer n, use Javascript generators to generate all prime numbers less than n.   Function Description Complete the getPrimes function in the editor below.   getPrimes has the following parameter(s): n:  an integer that represents the upper limit of prime numbers to be generated.   Constraints 2 ≤ n ≤ 104
