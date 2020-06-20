def representation(n):
    l_map = {1000:"M",500:"D",100:"C",50:"L",10:"X",5:"V",1:"I"}
    if(n >= 4000):
        return "Bad input"
    l = []
    for val in l_map:
        fr = int(n/val)
        n = n - (fr*val)
        while(fr != 0):
            l.append(l_map[val])
            fr = fr - 1
    f_l = []
    for val in l_map:
        if(l.count(l_map[val]) > 3):
            if(l.count(l_map[val*5]) == 0):
                f_l.append(l_map[val])
                f_l.append(l_map[val*5])
            else:
                f_l.pop()
                f_l.append(l_map[val])
                f_l.append(l_map[val*10])
        else:
            for i in range(l.count(l_map[val])):
                f_l.append(l_map[val])

    r = ""
    for i in f_l:
        r = r + i
    return r

def container():
    print("Input key:")
    ans = input()
    rstr = ""
    for i in range(0,len(ans),2):
        if(i != len(ans)-1):
            ad = representation(ord(ans[i])+ord(ans[i+1]))
            sb = representation(abs(ord(ans[i])-ord(ans[i+1])))
            if(ord(ans[i]) > ord(ans[i+1])):
                rstr = rstr + ad + "s" + sb + "s"
            else:
                rstr = rstr + sb + "s" + ad + "s"
        else:
            rstr = rstr + representation(ord(ans[i]))
    if(rstr == "CCXXIIIsXXIsVsCCXXVsCLXVIIIsXXXIVsCLIVsXIVsCCXXXVIIsIXsLXVIIsCLXIXsLXIIIsCLXVsLXIsCLIXsCXCVIIIsVIIIsCLsLIVsCCIXsXIXsCLXIIsLXVIsCLXIsLVIIsCCVsXVsXXXIXsCXCVsCLXsLVIIIsCLXVIsLXIIsCLXIsLVsXCIIsCLVIIIs"):
        print("Yup that's the key!, Great Job")
    else:
        print("Try again!")

container()