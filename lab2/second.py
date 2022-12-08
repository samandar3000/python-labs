

while True:
    a = input("Введите номер: ")
    b = input("Введите другой номер:  ")
    
    try:
        a = int(a); b = int(b)
        minimum = min(a,b)
        print(minimum)
        break
        
    except  ValueError:
        print("введите правильный выбор")
        
    
