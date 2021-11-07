from main.lib.interface import*
from main.lib.arquivo import *
from time import sleep


arq = 'cursoemvideo.txt'

if not arqExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas ','Cadastrar nova Pessoa','Sair do Sistema'])
    if resposta == 1:
        # opção de listar o conteúdo de um arquivo!
        lerArquivo(arq)
    elif resposta == 2:
        titulo('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaint('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        titulo('Saindo do sistema...Até logo!')
        break
    else:
        print('Erro! Digite uma opção válida!')
    sleep(1)