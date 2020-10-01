print("Muhammad Dicky Febriansyah")

#1 Mencari nilai rata rata 
A=10
B=15
C=7
D=4
E=12

rata=(A+B+C+D+E)/5
print("rata-rata jumlah 5 nilai")
print("A:",A,"B:",B,"c:",C,"D:",D,"E:",E)
print("rata-rata nilai=", rata)
print('')



#2 Menghitung Keliling dan Luas PP
print ("\n")
def persegipanjang (): 
   print("-- Keliling dan Luas Persegi Panjang --")
   p= int(input("Masukkan Panjang Persegi Panjang  :"))
   l= int(input("Masukkan Lebar : "))
   Luas = p * l
   Keliling = (2 * p) + (2 * l)
   print("Luas =", Luas)
   print("Keliling =", Keliling)
persegipanjang ()

#3 Menghitung kategori kelompok BIM 
print ("\n")
print("Body Mass Index")
berat= float(input("Masukkan berat badan anda (KG) "))
tinggi= float(input("Maasukkan tinggi badan anda (CM) "))
meter=(tinggi/100)
bmi=(berat/(meter*meter))
print("hasil=",bmi)
      
if bmi <18.5 : 
   print("Berat badan kamu kurang")
elif bmi >=18.5 and bmi <23 :
   print("Berat badan normal")
elif bmi >=23 and bmi < 30:
   print("Berat badan anda berlebihan")
elif bmi >=30:
   print("anda obesitas")



#4 Melakukan inputan nilai terbesar dan terkecil
print ("\n")
print("Nilai terbesar dan Terkecil")
angka = int(input("masukkan berapa kali angka yang anda mau ? : "))
bil = []
for n in range(angka):
   masukan= int(input("masukan nomor : "))
   bil.append(masukan)

print("nilai",bil)
print("nilai yang terbesar", max(bil))
print("nilai yang terkecil", min(bil))


#5 Melakukan validasi ussername dan password
print ("\n")
print("cek username dan password")
uss= 'febri'
paw='febri'
coba=0


while coba <3:
   us= input("masukkan ussername : ")
   pww= input("masukkan password : ")
   if us == uss and pww == paw: 
      print("Berhasil masuk")
      break

   else:
      print("maaf ussername dan password salah")
      coba+=1
   
