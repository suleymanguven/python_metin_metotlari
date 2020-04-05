"""""
adsoyad=str(input("Adınızı Soyadınızı Giriniz: "))
adsoyad=adsoyad.upper()
print("Adınız Soyadınız: ",adsoyad)


adsoyad=str(input("Adınızı Soyadınızı Giriniz: "))
adsoyad=adsoyad.lower()
print("Adınız Soyadınız: ",adsoyad)



adsoyad=str(input("Adınızı Soyadınızı Giriniz: "))
adsoyad=adsoyad.replace("I","ı")
adsoyad=adsoyad.lower()
print("Adınız Soyadınız: ",adsoyad)


adsoyad=str(input("Adınızı Soyadınızı Giriniz: "))
adsoyad=adsoyad.replace("i","İ")
adsoyad=adsoyad.upper()
print("Adınız Soyadınız: ",adsoyad)



tckimlik=input("T.C. Kimlik Numaranızı Giriniz: ")
print(tckimlik[0]+tckimlik[1]+"***"+tckimlik[9]+tckimlik[10])

#12345678910

"""
ad=input("adınızı giriniz: ")
adUzunluk=len(ad)
print(adUzunluk)
print(ad[adUzunluk-adUzunluk]+ad[adUzunluk-(adUzunluk-1)]+"***"+ad[adUzunluk-2]+ad[adUzunluk-1])
