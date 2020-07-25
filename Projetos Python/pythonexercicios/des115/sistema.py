from des115.lib.interface import *
from des115.lib.arquivo import *
from time import sleep

arq = 'ListaPessoas'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver Pessoas Cadastradas', 'Cadastrar Nova Pessoa', 'Sair do Sistema'])

    if resposta == 1:
        # Opção de listar o conteúdp de um arquivo
        lerArquivo(arq)

    elif resposta == 2:
        # Opção de cadastrar uma nova pessoa
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)

    elif resposta == 3:
        cabeçalho('Saindo do sistema... Até logo!')
        break

    else:
        print('\033[31mERRO: Digite uma opção válida!\033[m')
    sleep(2)
