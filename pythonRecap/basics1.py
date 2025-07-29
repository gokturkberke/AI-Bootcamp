type(33.34) #float
type("Hello World") #str

z = 8j + 18
type(z) #complex

#Lists
l = [1,2,3,4,"String",3.2,True]
type(l) #list
# siralidir , kapsayicidir , degistirilebilir
l.append(5) # listeye eleman ekler
l.insert(0, 0) # listenin basina eleman ekler
l.remove(3) # listeden eleman siler
l.pop() # listenin sonundaki elemani siler
l.sort() # listeyi siralar
l.reverse() # listeyi ters cevirir
l.clear() # listeyi bosaltir

#Dictionaries
d = { "Name " : "Berke", "Age" : 21, "IsStudent" : True } 
type(d) #dict
# degistirilebilir , anahtar-deger ciftlerinden olusur
d["Name"] = "Ali" # degeri degistirir
d["City"] = "Istanbul" # yeni anahtar-deger cift ekler
d.pop("Age") # anahtar-deger ciftini siler

# Tuple
t = ("Machine Learning", "Data Science")
type(t) #tuple
# siralidir , kapsayicidir , degistirilemez

# Sets
s = {1, 2, 3, 4, 5}
type(s) #set
# sirasiz + essiz , degistirilebilir
s.add(6) # sete eleman ekler
s.remove(3) # setten eleman siler
s.clear() # seti bosaltir

# String functions
text = "Hello World"
text.upper() # "HELLO WORLD"
text.lower() # "hello world"
text.replace("World", "Python") # "Hello Python"
text.split(" ") # Stringi böler ve liste döner ["Hello", "World"]

# Functions
def multiply_three(number):
    print(number * 3)
    
# ön tanimli argüman
def hi(word="World"):
    print("Hello " + word)
    
# Return
def difference(num1,num2=4):
    result = num1 - num2
    return result

difference(10) # 6
difference(10, 3) # 7

#Conditions
def check_name(name):
    if name == "Berke":
        print("Hello Berke")
    elif name == "Ali":
        print("Hello Ali")
    else:
        print("Hello Stranger")
check_name("Berke") # Hello Berke

# loops
bootcamps = ["Python", "Java", "C++", "JavaScript"]
for bc in bootcamps:
    print(bc.upper())
    
#while loop
num = 5
while num > 0:
    print(num)
    num -= 1 