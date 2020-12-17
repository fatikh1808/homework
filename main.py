# with open("luckyNumbers.txt", "r") as luckyNumbers:
#     lLines = luckyNumbers.readlines()
# print("lLines", lLines)
#
# with open("primeNumbers.txt", "r") as primeNumbers:
#     pLines = primeNumbers.readlines()
#     print("pLines", pLines)
#
#     result = [a for a in lLines if a not in pLines]
#     print("result", result)
#
# with open("result.txt", "w") as resultText:
#     for line in result:
#         resultText.write(line)
#
# 5
# Писать комментарии

# 1.6 (1)

# Выведите все элементы списка с четными индексами

# K = [1,2,3,4,5,6,7,8,9]

# for el in range(0,len(K)):
#     if el % 2 == 0:
#         print(K[el])
#     else:
#         continue


# (2)

# Дан список чисел.Если в нем есть два соседних элемента одного знака, выведите
# числа. Если соседних элементов одного знака нет, не выводите ничего.

# a = [1,2,3,4,8,-5,-6,-10] #array
# for i in range(1, len(a)):  #пробежка по всем элементам массива
#     if a[i - 1] * a[i] > 0:   # по индексу берём элемента и его соседа 
#         print(a[i - 1], a[i])   #и вывдим их
#         break #если убрать, будет выводить все пары

# (3)

# задача на сортировку) Дан массив из 10 элементов. Отсортировать массив с 1 по 5 по возрастанию, а с 6 по 1- по убыванию

# def main():
#     a = [1,6,8,9,10,52,3,4,6,7] #array
#     m = 5 #index to sort
#     a[:m] = sorted(a[:m])  #to index
#     a[m:] = sorted(a[m:], reverse = True)  #from index
#     print(*a)  #print
# if(1):  #calling func()
#     main()

#(4)

# Имеется массив из 5 элементов. Вывести среднее арифметическое отрицательных элементов

# import random

# def masgen():
#     mlist = [1,2,3,4,5,6,-7,-8,-9.-6] #array
#     for i in mlist:
#         if(i < 0):     #check elem of array
#             mlist1.append(i)    #add elem to array
#     print(sum(mlist1)/len(mlist1))  #sum of array/len of array
# if(1):
#     mlist1 = []
#     masgen()

#(5)

# Имеется двумерный массив 4х4. заполнить его с клавиатуры. Отсортировать глав диагональ по возрастанию, побочную по убыванию

# a = 2 #number of el arrays in main array
# b = 4 #number of els in each array
# mas = [] #shape of main array
# for i in range(a): 
#     mas.append([]) #adding el array to main array 
#     for j in range(b):   
#         r = int(input()) #input for els of el array
#         mas[i].append(r)  #appending el to elArray

# print(mas) 

# print(sorted(mas[0])) #normal sorting
# print(sorted(mas[1], reverse = True))  #descend sorting

# (2.4) task

# (3)
# Дан указатель: double **p = 0; Выполните следующие задания (решения можно оформлять внутри функции main):
#
# * создайте конструкцию, изображенную на рисунке;
#
# * выведите число, указанное в квадратике, на экран;
#
# * после этого удалите все динамические объекты.

#include <iostream>
# using namespace std;
#
# int main( void ) {
# double **p = 0;
# *( *( p = new double* ) = new double ) = 2;
# cout << **p << endl;
# delete *p;
# delete p;
# }

# (5) task

# (1) Создать текстовый файл с набором слов (1000 слов). Найти самое встречающееся слово. Предусмотреть вероятность того что файла может не быть.

# f = open("words.txt").read().split() #import, reading and creating array txt file with words

# word_counter = {} #free array

# for word in f:  
#     if word in word_counter:
#         word_counter[word] += 1
#     else:
#         word_counter[word] = 1

# popular_words = sorted(word_counter, key = word_counter.get, reverse = True) #sorting most words

# top_3 = popular_words[:3] #get and append 3 most words
# print(top_3)

# (2) На прямой даны N отрезков, которые заданы координатами их левого и правого конца. Для каждого данного отрезка необходимо узнать, сколько из данных отрезков полностью находятся в нем. Один отрезок полностью содержится во втором, если левый конец первого отрезка находится правее левого конца второго отрезка, а правый конец первого находится левее правого конца второго. Предложите как можно более эффективный способ решения этой задачи. Гарантируется, что все концы данных отрезков различны.


#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#


#(3) Напишите программу которая будет высчитывать минимальное расстояние (выражаемое количеством слов) между любыми двумя словами в файле

# f = open("words.txt").read().split() #import, reading and creating array txt file with words
# array = []  #array for word within words 

# firstWord = "noise" 
# secondWord = "gather"

# fI = f.index(firstWord) #find index of words
# sI = f.index(secondWord)

# while fI < sI + 1:
#     array.append(f[fI]) #add to array within words by idex of them
#     fI = fI + 1


# print(array)

# (1.Лабараторная работа)
# (1)

# Создайте класс Rectangle. Этот класс хранит только декартовы координаты четырех
# углов прямоугольника. Конструктор вызывает набор функций, которые принимают
# четыре группы координат и проверяют, чтобы каждая из координат х и у находилась
# в первом квадранте, в диапазоне от 0.0 до 20.0. Это множество функций должно
# также проверять, что переданные координаты действительно определяют
# прямоугольник. Должны быть предусмотрены функции-элементы, вычисляющие
# length, width, perimeter, и area. Длиной должно считаться большее из двух
# измерений. Включите предикатную функцию square, которая определяла бы, не
# является ли прямоугольник квадратом

# class Rectangle(object):

#     def __init__(self, x1, x2, y1, y2):
#         """Constructor"""
#         self.x0 = 0
#         self.xMax = 20
#         self.x1 = x1
#         self.x2 = x2
#         self.y0 = 0
#         self.yMax = 20
#         self.y1 = y1
#         self.y2 = y2
#         self.width
#         self.length

#     def length(self):
#         self.length = self.y2 - self.y1
#         return "length of rectangle -> %s" % (self.length)


#     def width(self):
#         self.width = self.x2 - self.x1
#         return "width of recangle -> %s" % (self.width)

#     def perimeter(self):
#         return "perimeter of rectangle -> %s" % ((self.length + self.width) * 2)

#     def area(self):
#         return "area of rectangle -> %s" % (self.width * self.length)

#     def isSquare(self):
#         if (self.width == self.length):
#             return "it is cuadrad"
#         else:
#             return "it is rectangle"


# if __name__ == "__main__":
#     custom = Rectangle(2, 5, 4, 5)
#     print(custom.length())
#     print(custom.width())
#     print(custom.area())
#     print(custom.perimeter())
#     print(custom.isSquare())

# (2)

# Имеется квадрат со сторонами 20см. Пользователь вводит радиусы 2-х кругов.
# Определить могут ли эти круги быть вписанными в указанный квадрат без
# пересечений между собой и со стенками.

# class isCirclesInSquares(object):

#     def __init__(self, r1, r2):
#         """Constructor"""
#         self.side = 20
#         self.r1 = r1
#         self.r2 = r2
#         self.diagonal = (self.r1 + self.r2) * 2

#     def isCircles(self):
#         if (self.side - 3) > self.diagonal:  #минус 3, потому что лини вообще не должны пересекаться
#             return "вписывается "
#         else:
#             return "не вписывается"


# if __name__ == "__main__":
#     custom = isCirclesInSquares(2, 5)
#     print(custom.isCircles())

# (3)

# Создать класс сотрудников организации, где вводимыми параметрами являются
# фамилия, имя, отчество, возраст, должность и заработная плата. Вывести на экран 2
# списка сотрудников в порядке убывания возраста и заработной платы.

# class FactoryEmployees(object):

#     def __init__(self, employess):
#         """Constructor"""
#         self.employees = employess

#     def ageDown(self):
#         agelist = sorted(self.employees, key=lambda x: x[2], reverse=False)
#         return agelist

#     def salaryDown(self):
#         salarylist = sorted(self.employees, key=lambda x: x[3], reverse=False)
#         return salarylist

# if __name__ == "__main__":
#     custom = FactoryEmployees([
#         ('John Fanks Albert', 'employee', 23, 10000),
#         ('Jane Alberto Arthur', 'manager', 18, 8000),
#         ('Dave Ronaldo Cristiano', 'boss', 35, 5000),])
#     print(custom.ageDown())
#     print(custom.salaryDown())

# (4)

# Описать класс матрица, в котором содержаться следующие параметры: 3 матрица
# одинаковой размерности 3на3. Третья матрица содержит максимальные элементы
# первых двух. Отсортировать элементы главной диагонали по возрастанию.

# class Matrix(object):

#     def __init__(self, firstAndSecondElems):
#         """Constructor"""
#         self.firstAndSecondElems = firstAndSecondElems
#         self.matrix = []
#         self.n = 3

#     def matrixContinue(self):
#         for val in self.firstAndSecondElems:
#             sumArr = sum(val)
#             val.append(sumArr)
        
#         self.matrix = self.firstAndSecondElems
    
#         for i in range (len(self.matrix)):
#             for j in range (len(self.matrix[i])):
#                 print("{:4d}".format(self.matrix[i][j]), end = "" )
#             print()
#         print()

#         for i in range(self.n):
#             for j in range(i+1,self.n):
#                 if self.matrix[i][i] > self.matrix[j][j]:
#                     self.matrix[i][i],self.matrix[j][j] = self.matrix[j][j],self.matrix[i][i]
        
#         for i in range (len(self.matrix)):
#             for j in range (len(self.matrix[i])):
#                 print("{:4d}".format(self.matrix[i][j]), end = "" )
#             print()
#         print()
        
#         return self.matrix

# if __name__ == "__main__":
#     custom = Matrix([[3, 6], [4, 6], [2, 1]])
#     print(custom.matrixContinue())

# (2 лабараторная работа)
# (1)

# Имеется класс Гражданин, у которого определены следующие свойства: Имя,
# Фамилия, Отчество, год рождения; и функции: ввода данных (можно использовать
# конструктор), вывода (ФИО, возраст). Создать дочерний класс Студент, для
# которого помимо указанных данных родительского класса запрашиваются данные:
# место учебы, номер группы. Предусмотреть вывод (ФИО, возраст, Место учебы,
# номер группы).

# class Citizen(object):
#     def __init__(self, name, lastName, patronymic, dateOfBirth):
#         self.name = name
#         self.lastName = lastName
#         self.patronymic = patronymic
#         self.dateOfBirth = dateOfBirth

#     def infoAboutCitizen(self):
#         return "i am %s %s %s and was born in %s" % (self.name, self.lastName, self.patronymic, self.dateOfBirth)

# class Student(Citizen):
#     def __init__(self, name, lastName, patronymic, dateOfBirth, university, groupNr):
#         Citizen.__init__(self, name, lastName, patronymic, dateOfBirth)
#         self.university = university
#         self.groupNr = groupNr

#     def infoAboutUni(self):
#         return"i study in %s and my group number is %s" % (self.university, self.groupNr)

# if __name__ == "__main__":
#     custom = Student("fotikh", "tashlanov", "Oybek ugli", "18.08.1997", "knitu", "6.13")
#     print(custom.infoAboutCitizen())
#     print(custom.infoAboutUni())

# (2)

# Создать класс Фигура, в котором предусмотрены функции расчета площади и
# периметра геометрической фигуры. Создать дочерние классы для Круга,
# Четырехугольника (прямоугольник, квадрат, трапеция)

# class Figure(object):
#     def __init__(self, height, width):
#         self.height = int(height)
#         self.width = int(width)
#         self.isCircle = False
#         self.isFourSquare = False
#         self.isTrapezoid = False

#     def area(self):
#         if (self.isCircle):
#             return (self.diameter * self.diameter) * 3.14
#         elif (self.isFourSquare):
#             return self.side * self.heightSide
#         elif (self.isTrapezoid):
#             return ((self.height + self.width) / 2) * self.sideHeight
#         else:
#             return self.height * self.width  


#     def perimeter(self):
#         if (self.isCircle):
#             return (self.diameter + self.diameter) * 3.14
#         elif (self.isTrapezoid):
#             return (self.height + self. width + self.height2 + self.width2)
#         else:
#             return (self.height + self.width) * 2
        

# class Circle(Figure):
#     def __init__(self, height, width, isCircle, diameter):
#         Figure.__init__(self, height, width)
#         self.isCircle = isCircle
#         self.diameter = diameter

# class Paralelogram(Figure):
#     def __init__(self, height, width, isFourSquare, side, heightSide):
#         Figure.__init__(self, height, width)
#         self.isFourSquare = isFourSquare
#         self.side = side
#         self.heightSide = heightSide

# class Rectangle(Figure):
#     def __init__(self, height, width):
#         Figure.__init__(self, height, width)

# class Square(Figure):
#     def __init__(self, height, width):
#         Figure.__init__(self, height, width)

# class Trapezoid(Figure):
#     def __init__(self, height, width, isTrapezoid, height2, width2, sideHeight):
#         Figure.__init__(self, width, height)
#         self.isTrapezoid = isTrapezoid
#         self.height2 = height2
#         self.width2 = width2
#         self.sideHeight = sideHeight


# if __name__ == "__main__":
#     custom = Trapezoid(5, 5, True, 10, 8, 12)
#     print(custom.area())
#     print(custom.perimeter())


# (3)
# 3. Используя абстрактные классы и виртуальные функции решить задачу №2.
# C++ --> booom!