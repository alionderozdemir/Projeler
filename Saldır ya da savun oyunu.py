#Ali Önder Özdemir Tarafından Yapılmıştır.
#Projemin amacı strateji oyunlarının hep saldırı olmadığı ya da hep savunma olmadığı, biraz sabrın
# biraz da her iki kısıtın beraber kullanılması gerektiğini belirmektir.

#Projeyi anlatmaya başlarsak:
#Random kütüphanesini import ediyoruz.
import random

# oyuncu adında bir class oluşturuyoruz.
class oyuncu():
    # Class'ımız için bir constructor oluşturuyoruz.
    # Constructor içinde, isim, can, blockDurum ve puan değişkenlerimizi üst block'a tanımlıyoruz.
    def __init__(self, isim, can, blockDurum, puan):
        self.isim = isim
        self.can = can
        self.blockDurum = blockDurum
        self.puan = puan
    # nesnemizin informal string'ini oluşturmak için __str__ fonksiyonumuzu oluşturuyoruz
    def __str__(self):
        str = """
        isim: {0}
        can: {1}
        """.format(self.isim, self.can)
        return str
    #Nesnemiz içindeki can değerimizi yazdırmak için fonksiyonumuzu belirliyoruz.
    def canGoster(self):
        print(self.isim," : ","Can: ", self.can)
    # oyuncularımızın saldırı değerini random bir şekilde hesaplamak için bu fonksiyonu kullanıyoruz.
    def saldiriHesapla(self):
        return random.randint(5,15)
    # Nesnemizin, can değerini değiştirmek için kullandığımız fonksiyon
    def hasarAl(self,hasar):
        if((self.can - hasar) < 0):
            self.can = 0
        else:
            self.can = self.can - hasar
# bir adet oyuncu classımızdan nesne türetiyoruz.
realOyuncu = oyuncu("", 100, False, 0)

print("Oyun başlıyor...")
print("Lütfen karakterinizin ismini giriniz.")
# Kullanıcının girdi değerini yukarı oluşturduğumuz nesnenin isim değeriyle oyuncunun ismini değiştiriyoruz.
realOyuncu.isim = input()
print("Hoşgeldin ", realOyuncu.isim, ".")

while (True):

    # Sonsuz while döngüsünü durdurmak için bir değişken oluşturduk.
    breaker = False
    # NPC ile oyuncumuz arasındaki sırayı belirlemek için kullanıyoruz.
    realOyuncuSirasi = True
    # NPC'miz için oyuncu classımızdan nesne türetiyoruz.
    # Burada can değerini random olarak 20 ile 60 arasında belirliyoruz.
    NPC = oyuncu("NPC", random.randint(20, 60), False, 0)

    print("Yeni savaş başlıyor")
    # informal stringlerimizi çağırıyoruz.
    print(realOyuncu)
    print("------------------")
    print("Düşmanın : ")
    print(NPC)

    # Oynanan tur için bir tane daha while oluşturuyoruz.
    while (True):
        #NPC can değeri 0 veya daha küçük olursa turu kazandırıyoruz.
        if (NPC.can <= 0):
            print("Kazandın !")
            print("Savaş meydanından çekildin ve 30 puan can yeniledin.")
            realOyuncu.can = realOyuncu.can + 30
            realOyuncu.puan = realOyuncu.puan + 10
            print("Puanın : ", realOyuncu.puan)
            break
        #Real oyuncu can değeri 0 veya daha küçük olursa oyunu kaybettiriyoruz.
        elif (realOyuncu.can <= 0):
            print("Kaybettin !!! Savaş meydanından ayrılıyor...")
            print("Puanın : ", realOyuncu.puan)
            breaker = True
            break

        print("------------------")
        realOyuncu.canGoster()
        NPC.canGoster()
        print("------------------")
        # realOyuncuSirasi True ise
        if (realOyuncuSirasi):
            print("Sıra ", realOyuncu.isim, "\'da")
            print("Sonraki hamlen nedir ?")
            print("Saldırı için 1")
            print("Savunma için 2")
            # Kullanıcıdan input bekliyoruz
            hamleDurum = int(input())
            #gelen input 1 ise
            if (hamleDurum == 1):
                # NPC block durum True ise
                if (NPC.blockDurum):
                    print("Karşı taraf block yaptığı için saldırınız 0 hasar vurdu.")
                    # NPC block durumunu False yapıyoruz.
                    #Böylelikle, yaptığı block'u iptal etmiş oluyoruz.
                    NPC.blockDurum = False
                    # Real oyuncu sırasını false yaparak, sıranın npc'ye geçmesini sağlıyoruz.
                    realOyuncuSirasi = False
                else:
                    #Eğer NPC bir önceki tur block yapmadığsa
                    # hasar değerini classımız içinde oluşturduğumuz
                    # fonksiyondan çağırıyoruz
                    hasar = realOyuncu.saldiriHesapla()
                    print("Düşmana ", hasar , "hasar vurdunuz." )
                    # class'ımızdan gelen hasarımızı
                    # NPC objemiz içindeki hasarAl fonksiyonu ile
                    # nesnemizin can değerini değiştiriyoruz.
                    NPC.hasarAl(hasar)
                    # Real oyuncu sırasını false yaparak, sıranın npc'ye geçmesini sağlıyoruz.
                    realOyuncuSirasi = False
            elif(hamleDurum == 2):
                print("Sonraki saldırı için block yapmayı tercih ettiniz.")
                # Bir sonraki turda NPC saldırı yaparsa
                # block yapsın diye block durumunu true yapıyoruz
                realOyuncu.blockDurum = True
                # Real oyuncu sırasını false yaparak, sıranın npc'ye geçmesini sağlıyoruz.
                realOyuncuSirasi = False


        if(not realOyuncuSirasi):
            print("Sıra NPC \'de")
            #hamle durum için 1 veya 2 olacak şekilde random değer atıyoruz.
            hamleDurum = random.randint(1,2)
            if(hamleDurum == 1):
                if(realOyuncu.blockDurum):
                    print("Karşı taraf block yaptığı için saldırınız 0 hasar vurdu.")
                    realOyuncu.blockDurum = False
                    realOyuncuSirasi = True
                else:
                    hasar = NPC.saldiriHesapla()
                    print(realOyuncu.isim," ", hasar , "hasar aldı." )
                    realOyuncu.hasarAl(hasar)
                    realOyuncuSirasi = True

            elif(hamleDurum == 2):
                print("NPC sonraki saldırı için block yapmayı tercih etti.")
                NPC.blockDurum = True
                realOyuncuSirasi = True


    if (breaker):
        break
