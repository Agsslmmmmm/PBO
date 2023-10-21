print("Menghitung Luas dan Volume Prisma Segitiga")

sisi = [12, 22, 13]
tinggi = 22
luas_alas = 23


# Luas
LS = (sisi[0] + sisi[1] + sisi[2]) * tinggi

LP = (sisi[0] + sisi[1] + sisi[2]) * tinggi * luas_alas

# Volume

volume = 1/3 * luas_alas * tinggi

# output
print("Luas segitiga adalah: ", LS)
print("Luas prisma adalah: ", LP)
print("Volume Prisma segitiga adalah: ", volume)