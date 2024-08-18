# Sets - Conjuntos em Python (tipo set)
# Sets em Python são mutáveis, porém só aceitam tipos imutáveis
#como valor interno.

                        #Criando um set:
# set(iterável) ou {1, 2, 3}


'''s1 = set('Ailton')
s2 = {'Ailton', 5, 9}   # Set com dados
s3 = set()  #Set vazio

print(s1, type(s1))
print(s2)
print(s3)'''




            # Sets são eficientes para remover valores duplicados
            #de iteráveis.
            # - Não aceitam valores mutáveis;
            # - Seus valores serão sempre únicos;
            # - não tem índexes;
            # - Não garantem ordem;
            # - são iteráveis (for, in, not in)

'''l1 = [1, 2, 3, 3, 3, 3, 3, 3, 1]
s1 = set(l1)
l2 = list(s1)
print(l2)
'''

                #Não aceitam valores mutáveis

# s1 = s1 = {1,2,3,{123}} # não aceita valores mutáveis (set dentro de set)

                    
                # Não tem índexes;

'''s1 = {1,2,3}
#print(s1[2]) ERRO!!!
print(3 in s1)
print()
for numero in s1:
    print(numero)
print()
print(4 not in s1)
'''

                # Métodos úteis:
                # add, update, clear, discard

'''s1 = set()
s1.add('Luiz')
s1.add(1)
s1.add(2)
s1.update(('Olá, mundo!',1,2,3,4))
#s1.clear() VAI LIMPAR O SET;
s1.discard('Olá, mundo!') #Elimina um valor especifico;
print(s1)
'''



            #Operadores úteis:
            #união | união (union) - Une;
            #intersecção & (intersection) - Itens presentes em ambos;
            #diferença - Itens presentes apenas no set da esquerda;
            #diferença simétrica ^ - Itens que não estão em ambos.

'''s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = s1|s2 #UNION
#s3 = s1 & s2 #INTERSECTION
#s3 = s2 - s1 #DIFERENCE
#s3 = s1 ^ s2 #SIMETRIAL DIFERENCE

print(s3)'''




                #Exemplo de uso dos sets

letras = set()
while True:
    letra = input('Digite: ')
    letras.add(letra.lower())

    if 'l' in letras:
        print('PARABENS!')
        break
    
    print(letras)