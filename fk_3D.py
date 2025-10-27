import math

# kita kasih perintah input untuk L1, L2, L3, 01, 02 dan 03
# karena desimal kita pakai float
# disini saya menambahkan 1 DOF lagi, perintahnya kurang lebih sama 
# jika ingin membuat versi 3D maka kita menambahkan tinggi (z)
L1 = float(input("Masukkan panjang lengan (L1) dalam cm: "))
L2 = float(input("Masukkan panjang lengan (L2) dalam cm: "))
L3 = float(input("Masukkan panjang lengan (L3) dalam cm: "))
theta1 = float(input("Masukkan sudut servo 1 (01) dalam derajat: "))
theta2 = float(input("Masukkan sudut servo 2 (02) dalam derajat:"))
theta3 = float(input("Masukkan sudut servo 3 (03) dalam derajat:"))
                     
# ubah derajat ke radian
t1 = math.radians(theta1)
t2 = math.radians(theta2)
t3 = math.radians(theta3)

# cari ujung lengan robot dengan rumus Foward Kinematics (FK)
r = L1 * math.cos(t2) + L2 * math.cos(t2+t3) + L3 * math.cos(t2+t3) 
x = r * math.cos(t1)
y = r * math.sin(t1)
z = L1 * math.sin(t2) + L2 * math.sin(t2+t3) + L3 * math.sin(t2+t3)

# berikan perintah untuk menampilkan hasil
print("\nHasil ujung lengan robot dengan 3 DOF (3D)")  #agar mendapat 2 angka dibelakang koma saja
print("x = ", round(x,2), "cm")
print("y = ", round(y,2), "cm")
print("z = ", round(z,2), "cm")