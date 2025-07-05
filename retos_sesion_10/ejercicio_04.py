jane={'Lemon Pie', 'Brownie', 'Tarta de Manzana',' Helado de Chocolate', 'Flan'}
Jhon={'Carrot Cake', 'Croissant de Chocolate','Lemon Pie',"Brownie de Manzana", "Pudding"} 
largo=len(jane)
aux=jane.intersection(Jhon)
laux=len(aux)
aux2=laux<=(largo/2)
print("¿Deben replantear su relación?", aux2)