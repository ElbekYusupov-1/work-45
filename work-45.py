# Array51
# a va b massiv qiymatlarini almashtirish

n = int(input("n = "))
a = []
b = []

print("a massiv elementlari:")
for i in range(n):
    a.append(int(input()))

print("b massiv elementlari:")
for i in range(n):
    b.append(int(input()))

for i in range(n):
    a[i], b[i] = b[i], a[i]

print("Yangi a massivi:", a)
print("Yangi b massivi:", b)


# Array52
# Agar a[i] < 5 bo'lsa b[i] = 2*a[i], aks holda b[i] = a[i]/2

n = int(input("\nn = "))
a = []
b = []

print("a massiv elementlari:")
for i in range(n):
    a.append(int(input()))

for i in range(n):
    if a[i] < 5:
        b.append(2 * a[i])
    else:
        b.append(a[i] / 2)

print("b massivi:", b)


# Array53
# c[i] = max(a[i], b[i])

n = int(input("\nn = "))
a = []
b = []
c = []

print("a massiv elementlari:")
for i in range(n):
    a.append(int(input()))

print("b massiv elementlari:")
for i in range(n):
    b.append(int(input()))

for i in range(n):
    c.append(max(a[i], b[i]))

print("c massivi:", c)


# Array54
# a massivning juft elementlaridan b massivi hosil qilish

n = int(input("\nn = "))
a = []
b = []

print("a massiv elementlari:")
for i in range(n):
    a.append(int(input()))

for i in range(n):
    if a[i] % 2 == 0:
        b.append(a[i])

print("b massivi:", b)
print("Elementlar soni:", len(b))


# Array55
# a massivning toq indeksdagi elementlaridan b massivi hosil qilish

n = int(input("\nn = "))
a = []
b = []

print("a massiv elementlari:")
for i in range(n):
    a.append(int(input()))

i = 1
while i < n:
    b.append(a[i])
    i += 2

print("b massivi:", b)
print("Elementlar soni:", len(b))