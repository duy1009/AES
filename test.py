def _pad(s):
    bs = 16
    print(chr(bs - len(s) % bs))
    return s + (bs - len(s) % bs) * chr(bs - len(s) % bs)

def _unpad(s):
    return s[:-ord(s[len(s)-1:])]


print(len(_pad("abac")))