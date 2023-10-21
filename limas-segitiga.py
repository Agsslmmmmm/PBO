print("Menghitung Luas dan Volume limas segitiga")

sisi = [12, 13, 22, 23]
luas_alas = 23
tinggi = 22


# luas
luas = sisi[0] + sisi[1] + sisi[2] + sisi[3]

# volume

volume = 1/3 * luas_alas * tinggi


# output 
print("Luas limas segitiga adalah: ", luas)
print("Volume limas segitiga adalah: ", volume)