# Как то вечером три разработчика написали 
# три метода класса `SomeClass`, каждый под себя. 
# Методы по сути своей почти одинаковые.
#
# Напишите свой метод `sorted_func`, 
# учитывая особенности всех представленных методов

# Собрать из 3 методов, один, который будет выполнять данную функцию.
# 1 - создаём класс SomeClass.
class SomeClass:
    # 2 - создаём инициализатор, в нём параметр list[с int значениями]
    def __init__(self):
        self.sort = [3, 2, 1, 4, 2, 1]

    # 3 - создаём ОДИН метод который будет сортировать список.
    def sorted_func(self):
        return sorted(self.sort, reverse=False)


if __name__ == "__main__":
    some = SomeClass()
    print(some.sorted_func())
# class SomeClass:
#     def __init__(self):
#         self.lst = [3, 2, 1, 4, 2, 1]
#
#     def sorted(self):
#         self.lst.sort()
#         return self.lst
#
#     def sorting(self):
#         return sorted(self.lst)
#
#     def asc_sorting(self):
#         return sorted(self.lst, reverse=False)
