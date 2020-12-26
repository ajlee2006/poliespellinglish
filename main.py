import eng_to_ipa as ipa

# ENGLISH TO POLIESPELLINGLISH
# Usage: poliespellinglishstring = eng2pol("Put an English sentence here")
def eng2pol(s):
    pron = ipa.convert(s)
    fs = ipa2pol(pron)
    return transfercase(s,fs)

# IPA TO POLIESPELLINGLISH (doesn't have all IPA characters, only those in English)
def ipa2pol(pron):
    ipalist = ['m', 'n', 'ŋ', 'p', 'b', 't', 'd', 'k', 'ɡ', 'f', 'v', 'θ', 'ð', 's', 'z', 'ʃ', 'ʒ', 'x', 'h', 'l', 'r', 'j', 'w', 'a', 'æ', 'ɑ', 'ɒ', 'ɔ', 'i', 'ɪ', 'e', 'ɛ', 'ɜ', 'ə', 'o', 'u', 'ʌ', 'ʊ', 'ʤ', 'ʧ', 'ˌ', 'ˈ', '*', 'ː']
    pollist = ['m', 'n', 'ng', 'p', 'b', 't', 'd', 'k', 'ɡ', 'f', 'v', 't̂', 'ψ', 's', 'z', 'ŝ', 'ĵ', 'ĥ', 'h', 'l', 'r', 'j', 'ŭ', 'a', 'ⱥ', 'a', 'w', 'w', 'i', 'ĭ', 'e', 'ⱥ', 'q', 'x', 'o', 'u', 'q', 'u', 'ĝ', 'ĉ', '', '', '', ':']
    fs = ''
    for i in pron:
        if i in ipalist:
            fs += pollist[ipalist.index(i)]
        else:
            fs += i
    fs = fs.replace('ts','c')
    fs = fs.replace('hm','m̆')
    fs = fs.replace('hn','n̆')
    fs = fs.replace('hb','b̆')
    fs = fs.replace('hk','k̆')
    fs = fs.replace('ai','aj')
    fs = fs.replace('ei','ej')
    fs = fs.replace('oi','oj')
    fs = fs.replace('ui','uj')
    fs = fs.replace('ⱥi','ⱥj')
    fs = fs.replace('wi','wj')
    fs = fs.replace('qi','qj')
    fs = fs.replace('xi','xj')
    fs = fs.replace('aĭ','aj')
    fs = fs.replace('eĭ','ej')
    fs = fs.replace('oĭ','oj')
    fs = fs.replace('uĭ','uj')
    fs = fs.replace('ⱥĭ','ⱥj')
    fs = fs.replace('wĭ','wj')
    fs = fs.replace('qĭ','qj')
    fs = fs.replace('xĭ','xj')
    fs = fs.replace('au','aŭ')
    fs = fs.replace('eu','eŭ')
    fs = fs.replace('iu','iŭ')
    fs = fs.replace('ou','oŭ')
    fs = fs.replace('ⱥu','ⱥŭ')
    fs = fs.replace('ĭu','ĭŭ')
    fs = fs.replace('wu','wŭ')
    fs = fs.replace('qu','qŭ')
    fs = fs.replace('xu','xŭ')
    fs = fs.replace('pŭ','φ')
    return fs

# stuff to make the IPA capitalised
def transfercase(s,f):
    fl = f.split(' ')
    sl = s.split(' ')
    for i in range(len(sl)):
        try:
            if sl[i] == sl[i].capitalize():
                fl[i] = fl[i].capitalize()
            elif sl[i].isupper():
                fl[i] = fl[i].upper()
            elif sl[i].islower():
                fl[i] = fl[i].lower()
        except:
            pass
    return ' '.join(fl)
