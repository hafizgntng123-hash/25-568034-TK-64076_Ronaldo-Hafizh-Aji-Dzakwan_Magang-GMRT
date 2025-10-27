import math

# femur
L1 = 34 
# tibia
L2 = 76
# sudut servo 1 dan 2
theta1 = 40
theta2 = 30

t1 = math.radians(theta1)
t2 = math.radians(theta2)

x = L1 * math.cos(t1) + L2 * math.cos(t1+t2)
y = L1 * math.sin(t1) + L2 * math.sin(t1+t2)

print("Ujung Lengan Robot")
print(f"y: {x:.2f} cm")
print(f"y: {y:.2f} cm")

# hasilnya sesuai dengan menggunakan rumus tulis maupun program