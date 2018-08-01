# -*- coding: UTF-8 -*-

class Perfil():
	'Classe padrão para perfis de usuários'
	
	def __init__(self, nome, telefone, empresa):
		self.nome = nome
		self.telefone = telefone
		self.empresa = empresa
		self.__curtidas = 0
	def imprimir (self):
		print "Nome: %s, telefone: %s, empresa: %s" % (self.nome, self.telefone. self.empresa)
	def curtir(self):
		self.__curtidas+=1
	def obter_curtidas(self):
		return self.__curtidas