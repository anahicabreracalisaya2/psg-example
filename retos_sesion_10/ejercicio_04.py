jane={'Lemon Pie', 'Brownie', 'Tarta de Manzana',' Helado de Chocolate', 'Flan'}
jhon={'Carrot Cake', 'Croissant de Chocolate','Lemon Pie',"Brownie de Manzana", "Pudding"} 

comunes = jane & jhon
total_postres = jane | jhon
compatibilidad = len(comunes) / len(total_postres) * 100
replantear = compatibilidad <= 50

print("¿Deben replantear su relación?",replantear)
print("Debido a que su ompatibilidad es del:",compatibilidad,"%")
