#Mengimpor module turtle dan fungsi randint dari module random
import turtle
from random import randint

#Memasang layar sekaligus memberi judul dan ukuran
jendela = turtle.Screen()
jendela.title("Rotating Colorful Squares and Disks")
jendela.setup(1100,600)

#Meminta user memasukkan panjang sisi mula-mula dari persegi
panjang_sisi_awal = jendela.numinput("Rotating Colorful Squares and Disks", "Please enter the side length of the first squares [20-60]",40, 20, 60)

#Menamai dan menyembunyikan turtle serta mengubah kecepatannya menjadi maksimum
kura = turtle.Turtle()
kura.hideturtle()
kura.speed(0)

#Mengatur titik awal turtle dan mengubah orientasi turtle ke arah barat
kura.up()
kura.setx(-200)
kura.sety(50)
kura.down()
kura.setheading(180)

#Membuat persegi sebanyak 72 buah
for i in range(72):
    
    #Menentukan dan menetapkan warna persegi secara acak
    color_choice = "#{:02x}{:02x}{:02x}".format(randint(0,255),randint(0,255),randint(0,255))
    kura.fillcolor(color_choice)

    #Memberi warna pada persegi yang sisinya selalu bertambah 2 dari sisi sebelumnya
    kura.begin_fill()
    for j in range(4):
        kura.forward(panjang_sisi_awal + 2 * i)
        kura.right(90)
    kura.end_fill()

    #Menyimpan panjang sisi terakhir dari persegi yang dibuat
    panjang_sisi_akhir = panjang_sisi_awal + 2 * i
    
    #Mengatur agar arah turtle berbelok ke kanan sebesar 5 derajat
    kura.right(5)

#Mengubah posisi turtle dan mengubah orientasi turtle menjadi ke arah timur
kura.up()
kura.setx(200)
kura.down()
kura.setheading(0)

#Menentukan jari-jari awal
radius = panjang_sisi_akhir * 0.5

#Membuat lingkaran sebanyak 36 buah
for i in range(36):
    color_choice = "#{:02x}{:02x}{:02x}".format(randint(0,255),randint(0,255),randint(0,255))
    kura.fillcolor(color_choice)
    kura.begin_fill()

    #Membuat lingkaran dengan radius yang berkurang 2 satuan dari radius sebelumnya
    kura.circle(radius - 2 * i)

    kura.end_fill()

    #Mengatur agar arah turtle berbelok ke kiri sebesar 10 derajat
    kura.left(10)
    
#Mengubah posisi turtle
kura.up()
kura.setx(0)
kura.sety(-190 - panjang_sisi_awal)
kura.down()

#Menentukan warna dan membuat isi teks
kura.color("blue")
kura.write("There are 72 Squares and 36 Disks",False, "center",font =("Times New Roman", 20))

#Menutup jendela turtle ketika jendela di klik
jendela.exitonclick()
