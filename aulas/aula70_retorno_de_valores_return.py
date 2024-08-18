'''
Retorno de valores das funções (return)
'''

#-------------------------------------
#def soma(x,y):
#    print(x + y)

#variavel = soma(1,2) #Sem valor (None)
#variavel = int('1')  #Tem o valor (inteiro)
    

#soma1 = soma(2,2) #NoneType
#soma2 = soma(3,3) #NoneType
#print(soma1 + soma2) #ERRO!! não é possivel somar dois NoneTypes
#------------------------------------------

def soma(x,y):
    if x > 10:
        return 10,20
    return x + y 

soma1 = soma(2,2) #Agora tem o valor inteiro
soma2 = soma(3,3) #Agora tem o valor inteiro
#print(soma1 + soma2) #Soma de inteiros =D
print(soma(11,29))