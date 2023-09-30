sides = [3, 2, 4, 7, 5, 12, 11, 13, 15, 16, 14, 14]
sides = sorted(sides, reverse = True)
l = len(sides)

sm = 0
for i in range(l):
    for j in range(i + 1, l):
        for k in range(j + 1, l):
            a = sides[i]
            b = sides[j]
            c = sides[k]
            if a + b > c and a + c > b and c + b > a:
                p = (a + b + c)/2
                Ger = (p*(p - a)*(p - b)*(p - c))**0.5
                if Ger > sm:
                    sm = Ger
print(sm)