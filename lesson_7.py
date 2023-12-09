# # #  Dictionary - слорвари 
# # # int str boolean float list tuple set frozenset dictionary
# # student = {'name': 'Alihan', 'age' : 18}
# # print(student)
# # print(type(student))
# # print(student['name'])
# # print(student['age'])
# # student.setdefault('language', 'python')
# # print(student)
# # print(len(student))
# # print(student.get('name')) 
# # student.pop('age') 
# # # метод для удаления ключа и значения
# # print(student)
# # del student['language']
# # print(student)
# # # student['name'] = "Davud"
# # # print(student)
# # car_tesla = {
# #     'id' : 103,
# #     'brand' : 'tesla',
# # #     'model' : 'Model x',
# # #     'year' : '23',
# # #     'color' : 'white',
# # # } 
# # # print(car_tesla)
# # print(car_tesla['id'])
# # car_tesla['color'] = "red"
# # print(car_tesla)
# # # car_tesla.popitem() удалят последний элемент из списка
# # car_tesla.setdefault('odometr', 654)
# # print(car_tesla)
# import time 

# contact = [
#     {'name' : 'Davud',
#      'surname': 'Baltabaev',
#      'phone' : '084349320'
#     },
# ]
# print(contact) 
# while True:
#     command = input("1 - посмотреть контакты, 2 - добавить, 3 - удалить, 4 - обновить: ")
#     if command == "1":
#         for c in contact:
#             print(c)
#     elif command == "2":
#         add_name = input("name: ")
#         add_surname = input("Surname: ")
#         add_number = input("Number: ")
#         result = {'name':add_name, 'surname':add_surname, 'phone' :add_number, 'created':time.ctime()}
#         contact.append(result)
#         print("Контакт успешно добавлен")
#     elif command == "3":
#         delete_number = input("delete number: ")
#         for cont in contact:
#             for key, value in cont.items():
#                 if value == delete_number:
#                     contact.remove(cont)
#                     print("контакт успешно удален")
#         else:
#             print("Не найден")

language = {"name" : "python", "version" : "3.10.1", "date" : "08 septenber 08"}
print(language)
for key, value in language.items():
    print(key, value)

# Functions - Функции
def hitoka():
    print("Hello world and geeks")
hitoka()

def add():
    num1 = int(input("num1: "))
    num2 = int(input("num2: "))
    print(num1 + num2)
add()

def dava(num1, num2):
    print(num1 * num2)
dava(27, 32)

def welcome(name:str="Geeks") -> str:
    print("Welcome", name)
    print("How are you?", name)
welcome("Davud")



