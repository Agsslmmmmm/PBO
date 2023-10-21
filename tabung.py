import math

print("Menghitung luas tabung")

pi = math.pi


r = 12 
T = 23

# Luas selimut
luas_selimut = 2 * pi * r * T

# Luas permukaan

luas_permukaan = 2 * pi * r * T + 2 * pi * r**2


# volume

volume = pi * r**2 * T

# output

print("Luas selimut adalah: ", luas_selimut)
print("Luas permukaan adalah: ", luas_permukaan)
print("Volumenya adalah: ", volume)