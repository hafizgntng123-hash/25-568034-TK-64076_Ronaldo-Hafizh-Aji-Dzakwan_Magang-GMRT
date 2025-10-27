import math

# kita kasih perintah input untuk L1, L2, q1, dan q2
# karena desimal kita pakai float
L1 = float(input("Masukkan panjang femur (L1) dalam cm: "))
L2 = float(input("Masukkan panjang tibia (L2) dalam cm: "))
theta1 = float(input("Masukkan sudut servo 1 (01) dalam derajat: "))
theta2 = float(input("Masukkan sudut servo 2 (02) dalam derajat:"))
                     
# ubah derajat ke radian
t1 = math.radians(theta1)
t2 = math.radians(theta2)

# cari ujung lengan robot dengan rumus Foward Kinematics (FK)
x = L1 * math.cos(t1) + L2 * math.cos(t1+t2)
y = L1 * math.sin(t1) + L2 * math.sin(t1+t2)

# berikan perintah untuk menampilkan hasil
print("\nHasil ujung lengan robot")  #agar mendapat 2 angka dibelakang koma saja
print("x = ", round(x,2), "cm")
print("y = ", round(y,2), "cm")

# Hasilnya sesuai 