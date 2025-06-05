from random import choice
lista_de_palavras = ["amor", "Brasil", "casa", "cachorro", "gato", "foca", "salada", "fruta", "barco", "gramatica"]
limite_de_erros = 6
gameplay = 1

def preenche_underlines(entrada="e", desafio="teste"):
    underlines = "_"*len(entrada)
    for e in entrada:
        for d in desafio:
            for _ in underlines:
                if e==d:
                    underlines = underlines.replace("_", e, desafio.index(e))
        print(underlines)


while gameplay: 
    desafio = choice(lista_de_palavras)
    letras_acertadas, letras_erradas, enforcado = [], [], False
    vitoria = 0

    while not enforcado and not vitoria:
        if not (len(letras_erradas) <= limite_de_erros):
            enforcado = True
            ativar_replay = (input(f'Não foi dessa vez! A palavra era: {desafio} \nQuer jogar de Novo? s/n')).lower()
        elif len(letras_acertadas) >= len(desafio):
            vitoria = True
            ativar_replay = input("Parabéns, você venceu o desafio acertando a palavra {desafio}! \nQuer jogar de Novo? s/n").lower()
        else:
            entrada_jogador = input('Digite a próxima letra: \n')
            if entrada_jogador in desafio:
                underscores = preenche_underlines(entrada_jogador)
                for letra in desafio:
                    if letra == entrada_jogador:
                        letras_acertadas.append(letra)
            print(f'Letras acertadas: {letras_acertadas}')
            print(f'Letras erradas: {letras_erradas}')

    if "n" in ativar_replay:
        print("Até logo! Obrigada por jogar.")
        gameplay = 0



### ideias nao implementadas
# from random import choice

# PALAVRAS = ["amor", "Brasil", "casa", "cachorro", "gato", "foca", "salada", "fruta", "barco", "gramatica"]
# LIMITE_ERROS = 6

# def mostrar_progresso(palavra, letras_certas):
#     return ''.join([letra if letra in letras_certas else "_" for letra in palavra])

# def solicitar_letra():
#     return input('Digite a próxima letra: \n').lower()

# def jogar_rodada(palavra):
#     letras_certas = []
#     letras_erradas = []
    
#     while True:
#         progresso = mostrar_progresso(palavra, letras_certas)
#         print(f"\nPalavra: {progresso}")
#         print(f"Letras erradas ({len(letras_erradas)}/{LIMITE_ERROS}): {', '.join(letras_erradas)}")

#         if "_" not in progresso:
#             print(f"\nParabéns, você venceu o desafio acertando a palavra '{palavra}'!")
#             return True

#         if len(letras_erradas) >= LIMITE_ERROS:
#             print(f"\nNão foi dessa vez! A palavra era: '{palavra}'.")
#             return False

#         letra = solicitar_letra()

#         if letra in palavra:
#             if letra not in letras_certas:
#                 letras_certas.append(letra)
#         else:
#             if letra not in letras_erradas:
#                 letras_erradas.append(letra)

# def deseja_rejogar():
#     resposta = input("\nQuer jogar de novo? (s/n): ").strip().lower()
#     return resposta == 's'

# def main():
#     print("=== Jogo da Forca ===")
#     while True:
#         palavra = choice(PALAVRAS).lower()
#         jogar_rodada(palavra)
#         if not deseja_rejogar():
#             print("Até logo! Obrigada por jogar.")
#             break

# if __name__ == "__main__":
#     main()
