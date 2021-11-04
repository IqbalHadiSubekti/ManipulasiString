#contoh kalimat yang akan dilakukan manipulasi string
pernyataan = 'saya akan pergi ke pusat perbelanjaan bersama ibu pada pagi hari nanti'
print("Kalimat awal: ",pernyataan)

print()
#melakukan pemisahan per kata untuk menjadi bentuk list menggunakan split
print("Kalimat setelah dilakukan split: ",pernyataan.split())

print()
#melakukan pergantian karakter/kata pada kalimat dari saya ke aku dan ibu ke mama
print("Kalimat setelah dilakukan replace: ",pernyataan.replace('saya','aku'))
print("Kalimat setelah dilakukan replace: ",pernyataan.replace('ibu','mama'))


