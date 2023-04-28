# kalkulator-sederhana
import tkinter as tk

# fungsi untuk menambahkan digit ke layar
def tambah_digit(digit):
    layar.insert(tk.END, digit)

# fungsi untuk menghapus semua isi layar
def hapus_layar():
    layar.delete(0, tk.END)

# fungsi untuk melakukan operasi perhitungan
def hitung():
    try:
        hasil = eval(layar.get())
        hapus_layar()
        layar.insert(tk.END, str(hasil))
    except:
        hapus_layar()
        layar.insert(tk.END, "Error")

# inisialisasi GUI
root = tk.Tk()
root.title("Kalkulator Sederhana")

# membuat layar
layar = tk.Entry(root, width=35, borderwidth=5)
layar.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# membuat tombol-tombol angka
tombol_1 = tk.Button(root, text="1", padx=40, pady=20, command=lambda: tambah_digit(1))
tombol_2 = tk.Button(root, text="2", padx=40, pady=20, command=lambda: tambah_digit(2))
tombol_3 = tk.Button(root, text="3", padx=40, pady=20, command=lambda: tambah_digit(3))
tombol_4 = tk.Button(root, text="4", padx=40, pady=20, command=lambda: tambah_digit(4))
tombol_5 = tk.Button(root, text="5", padx=40, pady=20, command=lambda: tambah_digit(5))
tombol_6 = tk.Button(root, text="6", padx=40, pady=20, command=lambda: tambah_digit(6))
tombol_7 = tk.Button(root, text="7", padx=40, pady=20, command=lambda: tambah_digit(7))
tombol_8 = tk.Button(root, text="8", padx=40, pady=20, command=lambda: tambah_digit(8))
tombol_9 = tk.Button(root, text="9", padx=40, pady=20, command=lambda: tambah_digit(9))
tombol_0 = tk.Button(root, text="0", padx=40, pady=20, command=lambda: tambah_digit(0))

# membuat tombol-tombol operasi
tombol_tambah = tk.Button(root, text="+", padx=40, pady=20, command=lambda: tambah_digit("+"))
tombol_kurang = tk.Button(root, text="-", padx=40, pady=20, command=lambda: tambah_digit("-"))
tombol_kali = tk.Button(root, text="x", padx=40, pady=20, command=lambda: tambah_digit("*"))
tombol_bagi = tk.Button(root, text="/", padx=40, pady=20, command=lambda: tambah_digit("/"))

# membuat tombol-tombol lainnya
tombol_hapus = tk.Button(root, text="Clear", padx=80, pady=20, command=hapus_layar)
tombol_sama_dengan = tk.Button(root, text="=", padx=80, pady=20, command=hitung)

# menempatkan tombol-tombol di grid
tombol_1.grid(row=3, column=0)
tombol_2.grid(row=3, column=1)
tombol_3.grid(row=3, column=2)

tombol_4.grid(row=2, column=0)
tombol_5.grid(row=2, column=1)
tombol_6.grid(row=2, column=2)

tombol_7.grid(row=1, column=0)
tombol_8.grid(row=1, column=1)
tombol_9.grid(row=1, column=2)

tombol_0.grid(row=4, column=0)
tombol_hapus.grid(row=4, column=1, columnspan=2)
tombol_sama_dengan.grid(row=5, column=0, columnspan=4)

tombol_tambah.grid(row=1, column=3)
tombol_kurang.grid(row=2, column=3)
tombol_kali.grid(row=3, column=3)
tombol_bagi.grid(row=4, column=3)

root.mainloop()
