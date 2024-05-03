'''
Input Harga: 370000
Input Diskon: 15
Output: harga yang harus dibayar adalah Rp. 314.500
'''

inputHarga = input("Input Harga : ")
inputDiskon = input("Input Diskon : ")

hargaAwal = int(inputHarga)
diskon = int(inputDiskon)
hargaDiskon = (diskon/100) * hargaAwal
hargaAkhir = hargaAwal - hargaDiskon
print(hargaAkhir)