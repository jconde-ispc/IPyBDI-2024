print("----------------  1  -----------------------------")
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

print("----------------  2  -----------------------------")
#thislist = ["apple", "banana", "cherry"]
print(len(thislist))

print("----------------  3  -----------------------------")
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

print(list1)
print(list2)
print(list3)

print("----------------  4  -----------------------------")
list4 = ["abc", 34, True, 40, "male"]
print(list4)

print("----------------  5  -----------------------------")
mylist = ["apple", "banana", "cherry"]
print(type(mylist))

print("----------------  6  -----------------------------")
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

#----------------
print("----------------  7  -----------------------------")
#Imprima el segundo elemento de la lista:
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

print("----------------  8  -----------------------------")
#Imprima el último elemento de la lista:
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])
#La indexación negativa significa comenzar desde el final.
#-1 se refiere al último elemento, -2 se refiere al penúltimo elemento, etc.

print("----------------  8.1  -----------------------------")
#Imprima el último elemento de la lista:
thislist = ["apple", "banana", "cherry"]
print(thislist[len(thislist)-1])

print("----------------  9  -----------------------------")
#Devuelva el tercer, cuarto y quinto elemento:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

print("----------------  10  -----------------------------")
#Este ejemplo devuelve los elementos desde el principio hasta "kiwi", pero SIN incluirlo:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

print("----------------  11  -----------------------------")
#Este ejemplo devuelve los elementos desde "cereza" hasta el final:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

print("----------------  12  -----------------------------")
#Este ejemplo devuelve los elementos desde "naranja" (-4) hasta "mango" (-1), pero SIN incluirlo:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

print("----------------  13  -----------------------------")
#Compruebe si "manzana" está presente en la lista:
thislist = ["apple", "banana", "cherry"]
if "appleeeee" in thislist:
  print("Yes, 'apple' is in the fruits list")
else:
  print("No esta en la lista")
print("----------------  14  -----------------------------")
#---------------------
#Cambie el segundo elemento:
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)   

print("----------------  15  -----------------------------")
#Cambie los valores "plátano" y "cereza" por los valores "grosella negra" y "sandía":
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

print("----------------  16  -----------------------------")
#Cambie el segundo valor reemplazándolo con dos valores nuevos:
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

print("----------------  17  -----------------------------")
#Para insertar un nuevo elemento de la lista, sin reemplazar ninguno de los valores existentes, podemos usar el insert()método.
# El insert()método inserta un elemento en el índice especificado:
# Insertar "sandía" como tercer elemento:
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

print("----------------  18  -----------------------------")
#Para agregar un elemento al final de la lista, use el método append() :
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

print("----------------  19  -----------------------------")
#El remove()método elimina el elemento especificado.
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)
#Si hay más de un elemento con el valor especificado, el remove()método elimina la primera aparición:

print("----------------  20  -----------------------------")
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)

print("----------------  21  -----------------------------")
#El pop()método elimina el índice especificado.
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

print("----------------  22  -----------------------------")
#Si no especifica el índice, el pop()método elimina el último elemento.
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

print("----------------  23  -----------------------------")
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

print("----------------  24  -----------------------------")
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

print("----------------  25  -----------------------------")
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

print("----------------  26  -----------------------------")
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

print("----------------  27  -----------------------------")
#Los objetos de lista tienen un sort()método que ordenará la lista de forma alfanumérica, ascendente, de forma predeterminada:
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

print("----------------  28  -----------------------------")
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)


