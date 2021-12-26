# Calculator
command = ''
while command != 'exit':
    command = input('Masukan perintah anda : ')

    if command != 'exit':
        break

    if command != '+' and command != '-' and command != '*' and command != '/':
        print('Perintah tidak ada, ulangi')
        continue

    a = int(input('Masukan angka pertama : '))
    b = int(input('Masukan angka kedua : '))

    if command == '+':
        result = a + b
    elif command == '-':
        result = a - b
    elif command == '*':
        result = a * b
    else:
        result = a / b

    print(f"Hasil : {result}")
    break
