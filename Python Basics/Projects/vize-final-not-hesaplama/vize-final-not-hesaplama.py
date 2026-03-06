# SINIFI GEÇME DURUMU PROJESİ

class Exams(object):
        
        global büt 
  
        v1 = float(input("Vizeniz: "))
        f1 = float(input("Final notunuz: "))
        
        if f1 > -1 and f1 < 50:
            print("Final notun 50'den küçük olamaz!! Geçme notu 50 çünkü!!")
            vf_ortalama = v1 * 0.4 + f1 * 0.6
            print("vf ortalaman: {}".format(vf_ortalama))
            print("Harf notun FF. Büte girmen gerekiyor!!")
            büt = float(input("Büt notunuzu giriniz: "))
            vb_ortalama = v1 * 0.4 + büt * 0.6
            
            if vb_ortalama > -1 and vb_ortalama < 50:
                print("Senin not orta: {}".format(vb_ortalama))
                print("Dersten kaldınız!!! Notunuz FF.")
            elif vb_ortalama > 49 and vb_ortalama < 60:
                print("Senin not ortal: {}".format(vb_ortalama))
                print("Dersi CB ile geçtiniz! ")
            elif vb_ortalama > 59 and vb_ortalama < 80:
                print("Senin not ortala: {}".format(vb_ortalama))
                print("Dersi BB ile geçtiniz!")
            elif vb_ortalama > 79 and vb_ortalama < 90:
                print("Senin not ortalam: {}".format(vb_ortalama))
                print("Dersi BA ile geçtiniz!") 
            elif vb_ortalama > 89 and vb_ortalama < 101:
                print("Senin not ortalaman: {}".format(vb_ortalama))
                print("Dersi AA ile geçtiniz. TEBRİKLER!!!")
        
        elif f1 >= 50 and f1 <= 100:
        
            vf_ortalama = v1 * 0.4 + f1 * 0.6
            
            
            if vf_ortalama > -1 and vf_ortalama < 50:
                print("---Senin not ort: {}".format(vf_ortalama))
                print("---Harf notun FF. Büte girmen gerekiyor!!")
                büt = float(input("----Büt notunuzu giriniz: "))
                vb_ortalama = v1 * 0.4 + büt * 0.6
                
                    
                if vb_ortalama > -1 and vb_ortalama < 50:
                    print("---Senin not orta: {}".format(vb_ortalama))
                    print("Dersten kaldınız!!! Notunuz FF.")
                elif vb_ortalama > 49 and vb_ortalama < 60:
                    print("---Senin not ortal: {}".format(vb_ortalama))
                    print("Dersi CB ile geçtiniz! ")
                elif vb_ortalama > 59 and vb_ortalama < 80:
                    print("---Senin not ortala: {}".format(vb_ortalama))
                    print("---Dersi BB ile geçtiniz!")
                elif vb_ortalama > 79 and vb_ortalama < 90:
                    print("---Senin not ortalam: {}".format(vb_ortalama))
                    print("Dersi BA ile geçtiniz!") 
                elif vb_ortalama > 89 and vb_ortalama < 101:
                    print("---Senin not ortalaman: {}".format(vb_ortalama))
                    print("Dersi AA ile geçtiniz. TEBRİKLER!!!")
        else:
            print("geçerli bir değer giriniz")
        
n1 = Exams()

    