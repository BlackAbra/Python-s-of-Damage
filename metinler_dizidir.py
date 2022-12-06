sesli_harfler = 'aeiou'
flag = 0 
kelime = input('kelime girin  >>>')
for harf in kelime:
    if harf in sesli_harfler:
        flag +=1
text ='{} kelimesinde {} sesli harf var >>> '
print(text.format(kelime,flag))