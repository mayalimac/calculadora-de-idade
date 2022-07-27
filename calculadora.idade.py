#calculadora de idade#

Ano_real = False
Nome=str(input('Digite seu nome completo:'))
while (Ano_real == False):
    try:
       Ano_nasc=int(input('Digite o ano em que você nasceu:'))
       if (Ano_nasc > 1922 and Ano_nasc < 2021):
           idade = 2022 - Ano_nasc
           Ano_real = True
           print(f"{Nome}, você tem/terá {idade} anos em 2022.")
       else :
           print("Informe um ano entre 1922 e 2021!")
    except:
       print("Informaçaõ inválida!  Insira o ano de nascimento:")