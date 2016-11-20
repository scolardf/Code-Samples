# takes a list of ints, returns the largest possible number made from the digits
def largestN(l):
    if l != []:
        x = 0
        for n in l:
            if n >= 10:
                t = int(str(n)[:1])
                if t > x:
                    x = n
            else:
                if n > x:
                    x = n
        l.remove(x)
        return str(x)+largestN(l)
    else:
        return ""

tList = [1,4,7,2,50]
result = largestN(tList)
print (result)
