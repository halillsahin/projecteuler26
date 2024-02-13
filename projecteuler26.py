devreden=0
bölen=2
while bölen<1000:
    kalanlar=[]
    bölünen=1
    while True:
        kalan=bölünen%bölen
        if kalan in kalanlar:
            ilk_index=kalanlar.index(kalan)
            son_index=len(kalanlar)
            if son_index - ilk_index >devreden:
                devreden=son_index -ilk_index
                sayı=bölen
            break    
        bölünen=10*kalan
        kalanlar.append(kalan)
    bölen+=1
print(sayı)    