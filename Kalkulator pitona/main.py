from models import Calculator

calc = Calculator()

while True:
    print()
    print("Калкулатор")
    print("1. Събиране")
    print("2. Изваждане")
    print("3. Умножение")
    print("4. Деление")
    print("5. Изход")

    choice = input("Изберете операция: ")

    if choice == "5":
        print("Довиждане!")
        break

    if choice in ["1", "2", "3", "4"]:
        a = float(input("Първо число: "))
        b = float(input("Второ число: "))

        if choice == "1":
            print("Резултат:", calc.add(a, b))

        elif choice == "2":
            print("Резултат:", calc.subtract(a, b))

        elif choice == "3":
            print("Резултат:", calc.multiply(a, b))

        elif choice == "4":
            print("Резултат:", calc.divide(a, b))

    else:
        print("Невалиден избор")