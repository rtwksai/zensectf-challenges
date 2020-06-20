import random
def turner(s):
    res = ""
    res += s[int(len(s)/2):]
    res += s[:int(len(s)/2)]
    return res

def modifier(s):
    res = ""
    for i in s:
        res += chr(ord(i)-1**ord(i))
    return res

def xor(sd,s):
    random.seed(sd)
    l = list(s)
    m = map(lambda x : chr(ord(x)^random.randint(0,10)),l)
    l = list(m)
    res = ""
    for i in l:
        res += i
    return res


def container():
    print("Enter the key :")
    input_string = input()
    if(input_string.startswith("zenseCTF{") and input_string[len(input_string)-1] == '}'):
        r = xor(1427,input_string[9:-1])
        r = modifier(r)
        r = turner(r)
        r = xor(1065,r)
        if(r == "N*W]h0m8{R'tPl6V=^fWo<RskdD2Y3q?TaYoT1lHP"):
            print("There you go you have your string!\n")
        else:
            print("Nope that wasn't the key!\n")
    else:
        print("Tags aren't right!\n")

container() 
