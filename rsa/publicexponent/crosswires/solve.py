from math import sqrt, gcd


def isPrime(n):
    prime_flag = 0 
    if(n > 1):
        for i in range(2, int(sqrt(n)) + 1):
            if (n % i == 0):
                prime_flag = 1
                break
        if (prime_flag == 0):
            return True
        else:
            return False
    else:
        return False


def factorN(n, e, d, primes):
    k = (d * e) - 1
    for prime in primes:
        g = prime
        t = k
        while t % 2 == 0:
            t = t >> 1
            x = pow(g, t, n)
            if x > 1:
                y = gcd(x - 1, n)
                if y > 1:
                    return y, n // y

    return None


def main():
    e = 0x10001
    n, d = (21711308225346315542706844618441565741046498277716979943478360598053144971379956916575370343448988601905854572029635846626259487297950305231661109855854947494209135205589258643517961521594924368498672064293208230802441077390193682958095111922082677813175804775628884377724377647428385841831277059274172982280545237765559969228707506857561215268491024097063920337721783673060530181637161577401589126558556182546896783307370517275046522704047385786111489447064794210010802761708615907245523492585896286374996088089317826162798278528296206977900274431829829206103227171839270887476436899494428371323874689055690729986771, 2734411677251148030723138005716109733838866545375527602018255159319631026653190783670493107936401603981429171880504360560494771017246468702902647370954220312452541342858747590576273775107870450853533717116684326976263006435733382045807971890762018747729574021057430331778033982359184838159747331236538501849965329264774927607570410347019418407451937875684373454982306923178403161216817237890962651214718831954215200637651103907209347900857824722653217179548148145687181377220544864521808230122730967452981435355334932104265488075777638608041325256776275200067541533022527964743478554948792578057708522350812154888097)
    friends = [106979, 108533, 69557, 97117, 103231]
    flag = 20304610279578186738172766224224793119885071262464464448863461184092225736054747976985179673905441502689126216282897704508745403799054734121583968853999791604281615154100736259131453424385364324630229671185343778172807262640709301838274824603101692485662726226902121105591137437331463201881264245562214012160875177167442010952439360623396658974413900469093836794752270399520074596329058725874834082188697377597949405779039139194196065364426213208345461407030771089787529200057105746584493554722790592530472869581310117300343461207750821737840042745530876391793484035024644475535353227851321505537398888106855012746117

    primes = []
    for i in range(2, 0x100):
        x = isPrime(i)
        if x:
            primes.append(i)

    p, q = factorN(n, e, d, primes)
    assert p * q == n

    phi = (p - 1) * (q - 1)

    friends_d = []
    for i in friends:
        fd = pow(i, -1, phi)
        flag = pow(flag, fd, n)

    print(bytes.fromhex(hex(flag)[2:]))


def smartass():
    e = 0x10001
    n, d = (21711308225346315542706844618441565741046498277716979943478360598053144971379956916575370343448988601905854572029635846626259487297950305231661109855854947494209135205589258643517961521594924368498672064293208230802441077390193682958095111922082677813175804775628884377724377647428385841831277059274172982280545237765559969228707506857561215268491024097063920337721783673060530181637161577401589126558556182546896783307370517275046522704047385786111489447064794210010802761708615907245523492585896286374996088089317826162798278528296206977900274431829829206103227171839270887476436899494428371323874689055690729986771, 2734411677251148030723138005716109733838866545375527602018255159319631026653190783670493107936401603981429171880504360560494771017246468702902647370954220312452541342858747590576273775107870450853533717116684326976263006435733382045807971890762018747729574021057430331778033982359184838159747331236538501849965329264774927607570410347019418407451937875684373454982306923178403161216817237890962651214718831954215200637651103907209347900857824722653217179548148145687181377220544864521808230122730967452981435355334932104265488075777638608041325256776275200067541533022527964743478554948792578057708522350812154888097)
    friends = [106979, 108533, 69557, 97117, 103231]
    flag = 20304610279578186738172766224224793119885071262464464448863461184092225736054747976985179673905441502689126216282897704508745403799054734121583968853999791604281615154100736259131453424385364324630229671185343778172807262640709301838274824603101692485662726226902121105591137437331463201881264245562214012160875177167442010952439360623396658974413900469093836794752270399520074596329058725874834082188697377597949405779039139194196065364426213208345461407030771089787529200057105746584493554722790592530472869581310117300343461207750821737840042745530876391793484035024644475535353227851321505537398888106855012746117

    prod = 1
    for k in friends:
        prod *= k

    dd = pow(prod, -1, (e * d) - 1)

    print(bytes.fromhex(hex(pow(flag, dd, n))[2:]))


if __name__ == "__main__":
    #smartass()
    main()
