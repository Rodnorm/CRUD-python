# -*- coding: UTF-8

import re
from mod import *   
def cadastrar(nomes):
	print'****Cadastro****'
	print 'Digite o nome:'
	nome = raw_input()
	nomes.append(nome)
	print'****Nome inserido com sucesso!****'

def menu():
	nomes = []
	escolha = ''
	while (escolha != '0'):
		print 'Digite 1 para cadastrar, 2 para listar os nomes, 3 pra deletar, 4 para alterar, 5 para procurar e 0 para sair: '
		escolha = raw_input()
		
		if (escolha == '1'):
			cadastrar(nomes)
			
                if (escolha == '2'):
                        listar(nomes)
                if (escolha == '3'):
                        remover_nomes(nomes)
                if (escolha == '4'):
                        alterar(nomes)
                if (escolha == '5'):
                       procurar(nomes) 

def listar(nomes):
        print '****Listando nomes**** '
        print (perfil.curtidas)
        for nome in nomes:
                print nome
     	print'!*!Fim da Lista***'
def remover_nomes(nomes):
	print'****Remover nomes****'
        print 'Qual nome será removido?'
        nome = raw_input()
        if (nome in nomes):
        	nomes.remove(nome)
        	print'****Nome removido com sucesso****'
        else:
        	print'!*!Nome não encontrado***'	

def alterar(nomes):
		print '****Alterando nomes****'
		print 'Digite um nome para alterar: '
		nome = raw_input()
		if (nome in nomes):
			pos = nomes.index(nome)
			print 'Insira a nova versão do nome: '
			nome_nove = raw_input()
			nomes[pos] = nome_nove
			print '****Nome alterado com sucesso!****'
		else:
			print '!*!Nome não encontrado!***'

def procurar(nomes):
	print '****Procurando nome****'
        nomes_concatenados = ' '.join(nomes)
        print 'Digite o nome a procurar: '
        regex = raw_input()
        resultados = re.findall(regex, nomes_concatenados)
        if (resultados == regex):
        	print('Nome %s encontrado!'%(resultados))
        else:
        	print'!*!Nome não encontrado***'
        
menu()
