print ("Operador XNOR")
a = True
b = True
print (not((a or b) and not (a and b)))
a = True
b = False
print (not((a or b) and not (a and b)))
a = False
b = True
print (not((a or b) and not (a and b)))
a = False
b = False
print (not((a or b) and not (a and b)))
