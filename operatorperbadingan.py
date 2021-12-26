grade = input('Masukan nilai anda : ')

if type(grade) == int:

    if grade >= 9:
        print('Nilai kamu adalah A')
    elif grade >= 8:
        print('Nilai kamu adalah B')
    elif grade >= 7:
        print('Nilai kamu adalah C')
    else:
        print('Kamu tidak lulus')
elif type(grade) == str:
    print('Yang anda masukan bukan angka')
