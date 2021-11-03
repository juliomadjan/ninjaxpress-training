# nama_buah=["apel","jeruk","mangga","lemon","salak"]
# print(nama_buah[0])
# print(nama_buah[1])
# print(nama_buah[2])
# print(nama_buah[3])
# print(nama_buah[4])

# # For Loop Iterasi Elemen dalam Suatu Array
# for buah in nama_buah:
#     print(buah)
#     print("---")

# # Di luar indent dari fungsi for sehingga tidak diprint berulang
# print("done")

# # Fungsi range(start,stop,increment) -> default range(0,wajib diisi,1)
# x = range(6)
# for n in x:
#     print(n)

# print("---")

# y = range(3,6)
# for n in y:
#     print(n)
# print("---")

# z = range(11,20,2)
# for n in z:
#     print(n)
# print("---")

# for n in range(2):
#     for m in range(3):
#         print(m)

# # FOR LOOP
# nama = []
# umur = []

# kuota = int(input("Jumlah orang: "))

# for n in range(kuota):
#     print("Data ke-{}".format(n+1))
#     nama_pelanggan = input("Enter Name: ")
#     umur_pelanggan = input("Age: ")


#     nama.append (nama_pelanggan)
#     umur.append (umur_pelanggan)
    
# for n in range(len(nama)):
#     print("Pelanggan {} berusia {}".format(nama[n],umur[n]))


# # WHILE LOOP
# i=1
# while i<6:
#     print(i)
#     i+=1

# print("done")


# # CONTINUE
# for i in range(5):
#     if i == 2:
#         continue
#     print(i)
# # Print Bilangan Genap
# for j in range(10):
#     if j % 2 == 1:
#         continue
#     print(j)


# # BREAK
# for k in range(10):
#     if k == 2:
#         break
#     print(k)


# # NESTED LOOP
# for l in range(3):
#     for m in range(3):
#         print("{}.{}".format(l+1, m+1), end=" ")
#     print()

x = [1,2,3,4,5]
y = [2,3,4,5,6]
z = 0
for i in x:
    for j in y:
        z = z + 1
print(z)
