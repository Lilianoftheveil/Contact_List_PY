import time
import json
from operator import itemgetter
from random import *

dic_contactos = {}
contactos = []
numeros_contactos = []

def ajuda():
	print(
"""
Comandos:

	lista_telefonica               
	- Imprime na tela a lista atualizada de contactos

	adicionar                      
	- Adiciona um novo contacto

	editar [Id]                    
	- Edita o contacto com o identificador [Id]

	apagar [Id]                    
	- Elimina o contacto com o identificador [Id]

	ordem_alfabetica               
	- Apresenta a lista total de contactos por ordem alfabética

	pesquisar [Nome]               
	- Pesquisa e apresenta os resultados da procura por [Nome] na lista

	importar [ficheiro]            
	- Importa uma lista de contactos de um ficheiro [JSON]

	extrair [formato][ficheiro]    
	- Extrai a lista de contactos para um ficheiro com um determinado formato 
	[YAML],[TXT] ou [XML]. Por padrão será [YAML]
""")


def lista_telefonica():
	print('-' * 30)
	print('\tLista Telefónica')
	print('-' * 30) 

	if len(contactos) == 0:
		print('Ops, lista vazia!')
		print('Utilize a função adicionar() para adicionar contactos.')
	else:
		for p in contactos:
			for k, v in p.items():
				print(f'{k}: {v}')
			print('-' * 30)


def adicionar():
	while True:
		x = randint(0, 100000) + int(len(contactos))
		try:
			print(f"ID: {x}")
			nome_contacto = input('Nome: ').strip().title()
			sobrenome_contacto = input('Sobrenome: ').strip().title()
			email = input('email: ').strip().lower()
			endereço = input('Endereço: ').strip().title()
			notas = input('Notas: ').strip().title()
			break
		except ValueError:
			print('Desculpe, formato inválido!')
			continue

	dic_contactos['Id'] = x
	dic_contactos['Nome'] = nome_contacto
	dic_contactos['Sobrenome'] = sobrenome_contacto
	dic_contactos['email'] = email
	dic_contactos['Endereço'] = endereço
	dic_contactos['Notas'] = notas

	while True:
		try:
			numero = int(input('Quantos números esse contato possui? '))
			numeros_contactos.clear()
			for i in range(0, numero):
				num = int(input(f'Número {i+1}: '))
				numeros_contactos.append(num)
				dic_contactos['Números'] = numeros_contactos[:]
			contactos.append(dic_contactos.copy())
			break
		except ValueError:
			print('Desculpe, formato inválido!')
			continue


def editar(Id):
	if len(contactos) == 0:
		print('Ops, lista vazia!')
		print('Utilize a função adicionar() para adicionar contactos.')
	else:
		Id = int(Id)
		for p in range(len(contactos)):
			if contactos[p]['Id'] == Id:
				x = contactos[p]['Id']
				while True:
					try:
						contactos[p]['Nome']  = input('Nome: ').strip().title()
						contactos[p]['Sobrenome'] = input('Sobrenome: ').strip().title()
						contactos[p]['email'] = input('email: ').strip().lower()
						contactos[p]['Endereço'] = input('Endereço: ').strip().title()
						contactos[p]['Notas'] = input('Notas: ').strip().title()
						break
					except ValueError:
						print('Desculpe, formato inválido!')
						continue

				while True:
					try:
						numero = int(input('Quantos números esse contato possui? '))
						numeros_contactos.clear()
						for i in range(0, numero):
							num = int(input(f'Número {i+1}: '))
							numeros_contactos.append(num)
							contactos[p]['Números'] = numeros_contactos[:]
					except ValueError:
						print('Desculpe, formato inválido!')
						continue
					else:
						break

def apagar(Id):
	if len(contactos) == 0:
		print('Ops, lista vazia!')
		print('Utilize a função adicionar() para adicionar contactos.')
	else:
		Id = int(Id)
		for p in range(len(contactos)):
			if contactos[p]['Id'] == Id:
				del contactos[p]
				print("ID deletado com sucesso!")
				break
	

def ordem_alfabetica():
	if len(contactos) == 0:
		print('Ops, lista vazia!')
		print('Utilize a função adicionar() para adicionar contactos.')

	else:
		contactos_ordenado = sorted(contactos, key=itemgetter('Nome')) 

		print('-' * 30)
		print('\tLista Telefónica')
		print('       em ordem alfabética')
		print('-' * 30) 

		for p in contactos_ordenado:
			for k, v in p.items():
				print(f'{k}: {v}')
			print('-' * 30)


def pesquisar(Nome):
	if len(contactos) == 0:
		print('Ops, lista vazia!')
		print('Utilize a função adicionar() para adicionar contactos.')
	else:
		for p in range(len(contactos)):
			if contactos[p]['Nome'] == Nome.title(): 
				print(contactos[p])
				break
			else:
				print("Desculpa, o Nome deste contacto não se encontra no banco de dados.")
				break


def importar(ficheiro):
	f = open(ficheiro)
	novos_contactos = json.load(f)
	
	contactos2 = []
	contactos2 = contactos.copy() 
	contactos2.append(novos_contactos)

	with open('lista_contactos_completa.json', 'w', encoding='utf8') as f:
			json.dump(contactos2, f, ensure_ascii=False)

	with open('lista_telefonica', 'w', encoding='utf8') as f:
			json.dump(contactos, f, ensure_ascii=False)

def extrair(formato, ficheiro):
	if formato == "YAML" or formato == "yaml" or formato == "":
		f = open(ficheiro + ".yaml", "w")
		for x in contactos:
			for key, value in x.items():
				f.write(f'{key}: {value}\n')
			f.write("\n")		
	elif formato == "TXT" or formato == "txt":
		f = open(ficheiro + ".txt", "w")
		for x in contactos:
			for key, value in x.items():
				f.write(f'{key}: {value}\n')
			f.write("\n")  
	elif formato == "XML" or formato == "xml":
		f = open(ficheiro + ".xml", "w")
		f.write(f'<lista_telefonica>\n')
		for x in contactos:
			for key, value in x.items():
				f.write(f'	<{key}>{value}</{key}>\n')
		f.write("</lista_telefonica>\n")  
	else:
		print("ERRO: Formato Inválido.")
		print("Não foi possível gerar o resultado.")

print("Olá, gostaria de gerir sua lista telefónica?\nDigite (--help) para receber a lista de comandos.")

while True:
	x = input("Digite o comando desejado: ").lower()
	if x == ("--help"):
		ajuda()
		continue
	elif x == ("lista_telefonica"):
		lista_telefonica()
		continue
	elif x == ("adicionar"):
		adicionar()
		continue
	elif x == ("editar"):
		y = input("ID: ")
		editar(y)
		continue
	elif x == ("apagar"):
		try:
			y = int(input("ID: "))
			apagar(y)
			continue
		except ValueError:
			print('Desculpe, formato inválido!')
			continue
	elif x == ("ordem_alfabetica"):
		ordem_alfabetica()
		continue
	elif x == ("pesquisar"):
		y = input("Nome: ")
		pesquisar(y)
		continue
	elif x == ("importar"):
		y = input("Ficheiro: ")
		importar(y)
		continue
	elif x == ("extrair"):
		y = input("Formato: ")
		z = input("Ficheiro: ")
		extrair(y, z)
		continue
	elif x == "exit":
		break
	else:
		pass
