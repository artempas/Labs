from sem3.lab4.Complex import Complex
import pickle
import traceback
from time import sleep

class UserFailed(Exception):
    pass

if __name__ == '__main__':
    obj: list[Complex] = []
    flag = True
    try:
        with open("database.db", 'rb') as db:
            try:
                obj=pickle.load(db)
            except EOFError:
                print("Произошла ошибка во время загрузки файла")
                traceback.print_exc()
    except FileNotFoundError:
        print("Файл для загрузки отсутствует")
        traceback.print_exc()
        try:
            created = open('database.db', 'wb')
        except BaseException:
            traceback.print_exc()
    while flag:
        sleep(0.5)
        print("1) Просмотреть все комплексные числа\n"
              "2) Добавить новое число\n"
              "3) Сохранить\n"
              "0) Выход\n")
        try:
            flag = int(input("Введите пункт меню: "))
        except ValueError:
            try:
                raise UserFailed(f"User should've written a number (not word)")
            except UserFailed as my_exc:
                print(my_exc)
                flag=True

        if flag == 1 and type(flag) is int:
            for ob in obj:
                print(ob)

        elif flag == 2:
            x = input("X: ").replace(',', '.')
            while not x.replace('.', '').isdigit():
                print("Only numbers are allowed")
                x = input("X: ")
            x = float(x)
            y = input("Y: ").replace(',', '.')
            while not y.replace('.', '').isdigit():
                print("Only numbers are allowed")
                y = input("Y: ")
            l = len(obj)
            obj.append(Complex(x, float(y)))
            assert l != len(obj) + 1, "Length of list hasn't increased"

        elif flag == 3:
            try:
                with open('database.db', "wb") as file:
                    pickle.dump(obj, file)
                print("Файл сохранён")
            except BaseException as exc:
                print("Произошла ошибка при сохренении файла")
                traceback.print_exc()
        elif flag!=0:
            try:
                raise UserFailed("User should've written a number from 0 to 3")
            except UserFailed:
                traceback.print_exc()