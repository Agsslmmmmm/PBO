import math

print("Menghitung luas dan volume kerucut")

pi = math.pi

r = 29
s = 22
T = 23

# Luas selimut
luas_selimut = pi * r * s

# Luas permukaan
luas_permukaan = pi * r * s + pi * r**2

# Volume
volume = 1/3 * r**2 * T


# output
print("Luas selimut adalah: ", luas_selimut)
print("Luas permukaan adalah: ", luas_permukaan)
print("Volumenya adalah: ", volume)