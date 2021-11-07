def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print(print(f'Error!!! - Digite um número inteiro válido'))
            continue
        except (KeyboardInterrupt):
            print('\nUsuário preferiu não digitar esse número!')
            return 0
        else:
            return n


def linha(tam=42):
    return '-' * tam


def titulo(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    titulo('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    print(linha())
    opc = leiaint('Sua opção: ')
    return opc