names = ['Didik', 'Prabowo', 'Joko', 'Budi', 'Setiadi']
print(names)

# Menambahkan element baru di akhir list
names.append('Daniel')
print(names)

# Menambahkan element baru di index yang kita tentukan
names.insert(2, 'Sena')
print(names)

# Menghapus satu element di akhir element
names.pop()
print(names)

# Menghapus element yang kita tentukan
names.remove('Setiadi')
print(names)

# Mengurutkan array berdasarkan angka atau huruf pertama
names.sort()
print(names)