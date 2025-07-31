text = "The Goal is to turn data into information, and information into insight."
a = text.upper()
splitted_text = a.replace(","," ").replace(".","").split()
print(splitted_text)

lst = ["D","A","T","A","S","C","I","E","N","C","E"]
print(len(lst))
print(lst[0],lst[10])
print(lst[0:4])
lst.pop(8)
lst.append("N")
lst.insert(8,"N")
print(lst)

dict = {'Christian' : ["America",18],
        'Daisy' : ["England",12],
        'Antonio' : ["Spain",22],
        'Dante' : ["Italy",25]}

print(dict.keys())
print(dict.values())

dict['Daisy'][1] =13
