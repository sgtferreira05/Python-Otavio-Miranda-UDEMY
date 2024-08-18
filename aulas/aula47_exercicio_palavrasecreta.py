'''
Faça um jogo para o usuário adivinhar qual a palavra secreta.

Voce vai propor uma palavra secreta qualquer e vai dar a possibilidad
para o usuário digitar apenas uma letra.

Quando a letra for digitada, voce irá conferir se letra stá na palavr
    Se a letra digitada estiver na palvra, exiba a letra;
    Se não tiver, exiba *
Faça a contagem de tentativas do usuário.
'''
import os
palavra_chave = 'cafe'
letras_acertadas = ''
numero_tentativas = 0

while True:
    letra_digitada = input('Digite uma letra: ')
    numero_tentativas += 1

    if len(letra_digitada) > 1:
        print('Digite apenas uma letra.')
        continue

    if letra_digitada in palavra_chave:
        letras_acertadas += letra_digitada
    
    palavra_formada = ''

    for letra_secreta in palavra_chave:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'
    print('Palavra formada:', palavra_formada)

    if palavra_formada == palavra_chave:
        os.system('cls')
        print('Você conseguiu, Parabéns!')
        print('A palavra era: ', palavra_chave)
        print('Tentativas: ', numero_tentativas)
        letras_acertadas = ''
        numero_tentativas = 0




    


