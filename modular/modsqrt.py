def findQS(q):
    s = 0
    while (q % 2 == 0):
        q = q // 2
        s += 1

    return q, s

a = 8479994658316772151941616510097127087554541274812435112009425778595495359700244470400642403747058566807127814165396640215844192327900454116257979487432016769329970767046735091249898678088061634796559556704959846424131820416048436501387617211770124292793308079214153179977624440438616958575058361193975686620046439877308339989295604537867493683872778843921771307305602776398786978353866231661453376056771972069776398999013769588936194859344941268223184197231368887060609212875507518936172060702209557124430477137421847130682601666968691651447236917018634902407704797328509461854842432015009878011354022108661461024768
p = 30531851861994333252675935111487950694414332763909083514133769861350960895076504687261369815735742549428789138300843082086550059082835141454526618160634109969195486322015775943030060449557090064811940139431735209185996454739163555910726493597222646855506445602953689527405362207926990442391705014604777038685880527537489845359101552442292804398472642356609304810680731556542002301547846635101455995732584071355903010856718680732337369128498655255277003643669031694516851390505923416710601212618443109844041514942401969629158975457079026906304328749039997262960301209158175920051890620947063936347307238412281568760161

#print(pow(a, (p - 1) // 2, p))

q, s = findQS(p - 1)

z = 2
while (True):
    if pow(z, (p - 1) // 2, p) == p - 1:
        break

    z += 1

m = s
c = pow(z, q, p)
t = pow(a, q, p)
R = pow(a, (q + 1) // 2, p)

count = 0
while t != 1:
    i = 1
    while True:
        if pow(t, pow(2, i), p) == 1:
            break
        i += 1

    b = pow(c, pow(2, m - i - 1), p)
    m = i
    c = pow(b, 2, p)
    t = (t * pow(b, 2)) % p
    R = (R * b) % p

    count += 1

print(R)
