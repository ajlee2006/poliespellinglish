#import eng_to_ipa as ipa
import requests, re

# ENGLISH TO POLIESPELLINGLISH
# Usage: poliespellinglishstring = eng2pol("Put an English sentence here")
# It will use an API that uses tophonetics.com to convert English text to IPA.
# Alternatively, you can use a separate tool to get the IPA and use the functions below.
def eng2pol(s):

    s = s.strip()

    # Uses the Python eng_to_ipa module to convert English text to IPA.
    #pron = ipa.convert(s)

    # Uses an API that uses tophonetics.com to convert English text to IPA.
    pron = requests.get("https://tophonetics-api.ajlee.repl.co/api", data={"text": s}).text

    fs = ipa2pol(pron)
    return transfercase(s,fs)

# IPA TO POLIESPELLINGLISH (doesn't have all IPA characters, only those in English)
# You can use this function and transfercase if you have a custom IPA string.
# Usage: poliespellinglishstring = transfercase("Put an English sentence here",ipa2pol("pʊt ən ˈɪŋglɪʃ ˈsɛntəns hɪə"))
def ipa2pol(pron):
    ipalist = ['m', 'n', 'ŋ', 'p', 'b', 't', 'd', 'k', 'ɡ', 'f', 'v', 'θ', 'ð', 's', 'z', 'ʃ', 'ʒ', 'x', 'h', 'l', 'r', 'j', 'w', 'a', 'æ', 'ɑ', 'ɒ', 'ɔ', 'i', 'ɪ', 'e', 'ɛ', 'ɜ', 'ə', 'o', 'u', 'ʌ', 'ʊ', 'ʤ', 'ʧ', 'ˌ', 'ˈ', '*', 'ʔ']
    pollist = ['m', 'n', 'ng', 'p', 'b', 't', 'd', 'k', 'ɡ', 'f', 'v', 't̂', 'ψ', 's', 'z', 'ŝ', 'ĵ', 'ĥ', 'h', 'l', 'r', 'j', 'ŭ', 'a', 'ⱥ', 'a', 'w', 'w', 'i', 'ĭ', 'e', 'ⱥ', 'q', 'x', 'o', 'u', 'q', 'u', 'ĝ', 'ĉ', '', '', '', '']
    fs = ''
    for i in pron:
        if i in ipalist:
            fs += pollist[ipalist.index(i)]
        else:
            fs += i
    fs = fs.replace('kts','ẑ')
    fs = fs.replace('gdz','z̆')
    fs = fs.replace('ts','c')
    fs = re.sub('h([mnbk])', r'\1̆', fs)
    fs = fs.replace('pŭ','φ')
    fs = re.sub('([aeiouⱥĭwqxː])[iĭ]', r'\1j', fs)
    fs = re.sub('([aeioⱥĭwqxː])uŭ', r'\1ŭ', fs)
    fs = re.sub('([aeioⱥĭwqxː])u', r'\1ŭ', fs)
    fs = re.sub('ŭj([mnpbtdkgfvt̂ψszŝĵĥhlrjcφ])', r'ŭi\1', fs)
    fs = fs.replace('ː',':')
    return fs

# Stuff to make the IPA capitalised
def transfercase(s,f):
    s = s.replace('\u0007','').replace('\n','\u0007 ')
    f = f.replace('\u0007','').replace('\n','\u0007 ')
    fl = f.split(' ')
    sl = s.split(' ')
    for i in range(len(sl)):
        try:
            if sl[i].upper() == sl[i].lower():
                pass
            elif sl[i].islower():
                fl[i] = fl[i].lower()
            elif sl[i] == sl[i].capitalize():
                fl[i] = fl[i].capitalize()
            elif sl[i].isupper():
                fl[i] = fl[i].upper()
        except:
            pass
    return ' '.join(fl).replace('\u0007 ','\n')

#print(eng2pol('As the school flag flies up high\nRising up towards the sky\nAll our hearts rejoice singing in one voice\nFor our spirit never dies\n\nBurning passion deep inside\nWith faith hope and foresight\nScaling greater heights\nWith one big stride\nFor NUS High we fight\n\nArise young minds, together\nThe seeds have just been planted\nIn our souls the flames ignite\nAs we show our might'))

# Prompts you for English text, prints Poliespellinglish, then prompts you again.
#'''
while True:
    print(eng2pol(input('English: > ')))
    #print(ipa2pol(input('IPA: > ')))
#'''

# Prompts you for English text, then IPA, then prints Poliespellinglish.
#print(transfercase(input('English: > '),ipa2pol(input('IPA: > '))))
