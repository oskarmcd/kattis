import sys
n = 3
for line in sys.stdin:
    ready = [line[i:i + n] for i in range(0, len(line), n)]
#print(ready)
greshka = False
for item in ready:
    if ready.count(item) > 1:
        print("GRESKA")
        greshka = True
        break
if not greshka:
    crap = []
    for x in range(1,14):
        if x < 10:
            crap.append("P0" + str(x))
            crap.append("K0" + str(x))
            crap.append("H0" + str(x))
            crap.append("T0" + str(x))
        else:
            crap.append("P" + str(x))
            crap.append("K" + str(x))
            crap.append("H" + str(x))
            crap.append("T" + str(x))
    for item in ready:
        if item in crap:
            crap.remove(item)
    p_counter = 0
    k_counter = 0
    h_counter = 0
    t_counter = 0

    for item in crap:
        if "P" in item:
            p_counter += 1
        elif "K" in item:
            k_counter += 1
        elif "H" in item:
            h_counter += 1
        elif "T" in item:
            t_counter += 1
    print(p_counter, k_counter, h_counter, t_counter)