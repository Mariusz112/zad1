##Mariusz Raś
# zad1

str = 'napis'
str1 = 'napis1'
int = 6
int1 = 5
float2 = 5,32
float1 = 5,35
complex = complex('5-9j')

list = ["apple", "banana", "cherry"]
list1 = ["cherry", "banana", "apple"]
tuple = ("apple", "banana", "cherry")
tuple1 = ("cherry", "banana", "apple")
range = range(6)

dict = {"name" : "John", "age" : 36}
dict1 = {"name2" : "John", "age" : 36}
set = {"apple", "banana", "cherry"}
set1 = {"3apple", "banana", "3cherry"}
frozenset  = frozenset({"apple", "banana", "cherry"})
bool= True
bool1=  False
bytes = b"Hello"
bytes1 = b"Helo"
bytearray= bytearray(5)


print(str)
print(str1)
print(int)
print(int1)
print(float2)
print(float1)
print(complex)
print(list)
print(list1)
print(tuple)
print(tuple1)
print(range)
print(dict)
print(dict1)
print(set)
print(set1)
print(frozenset)
print(bool)
print(bool1)
print(bytes)
print(bytes1)
print(bytearray)

#zad 2/3

a=6
b=3
print("dodawanie")
print(a, "+", b, "=", (a+b))
print("odejmowanie")
print(a, "-", b, "=", (a-b))
print("mnozenie")
print(a, "*", b, "=", (a*b))
print("dzielenie")
print(a, "/", b, "=", (a/b))
print("potegowanie")
print(a, "**", b, "=", (a**b))
print("modulo")
print(a, "%", b, "=", (a%b))

#zad 4
import math
print(math.e)
print(math.e ** 10)
print("y=ln(5+sin^2*8) ** (1. / 6)")
y=math.log(5+0.8988) ** (1. / 6)
print(y)
print(3,55)
print(4,80)

#zad 5
name1 = "mariusz"
name2 = "ras"
print(name1.capitalize() +" "+ name2.capitalize())

#zad 6
string = "Bardzo łatwo: Pstryk - i światło! Pstryknąć potem jeszcze raz, Zaraz mrok otoczy nas. A jak pstryknąć trzeci raz- Znowu dawny świeci blask."
substring = "Pstryk"
count = string.count(substring)
print("Wyraz Pstryk, występuje w tekscie: ", count ,"razy")

#zad 7
zad7 = "Hello, World!"
print(zad7[1], zad7[-1])

#zad8
zad8 = "Hello, World!"
print(zad8.split(","))

#zad9
napis="to jest napis"
print(napis)

zmienno = float(3)
print(zmienno)

hexa = hex(255)
print(hexa)