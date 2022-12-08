

while True:
    a = input("Введите номер: ")
    b = input("Введите другой номер:  ")
    
    try:
        a = int(a); b = int(b)
        maximum = max(a,b)
        print()
        print(f' найбольшее число равно {maximum}')
        break
        
    except  ValueError:
        print("введите правильный выбор")
        
    
