
tespecies = (
    ('canino', '🐶'),
    ('felino', '🐱'),
    ('aves', ['🐦', '🦅'])
)

especies = dict(tespecies)
print(especies)
# Obtener y eliminar el valor de la clave 'aves'
aves_valor = especies.pop('aves')
print(aves_valor)
print(especies)
# Modificar el valor de 'felino'
especies['felino'] = '🐈'
print(especies)
# Cambiar la clave 
especies['caninos'] = especies.pop('canino')
especies['caninos']=['🐶','🐕']
print(especies)