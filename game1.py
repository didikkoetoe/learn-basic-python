from random import randint

trying = 0
secret_number = randint(1, 10)
limit = 3

while trying < limit:
    user_number = int(input('Masukan angka pilihan anda dari 1 - 10 : '))
    if user_number == secret_number:
        flag = 1
        break
    else:
        print('Tebakan anda salah, ulangi sekali lagi')
        flag = 0
    trying += 1

if flag == 1:
    print('Selamat, tebakan anda benar')
else:
    print('Anda kalah')
