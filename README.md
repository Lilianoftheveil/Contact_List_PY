# Lista telefónica
## Objetivo
Criar um script em Python para gerir uma lista de contactos.
## Dados
- Id: um número único que serve como identificador do contacto.
- Nome: nome do contacto.
- Sobrenome: sobrenome do contacto.
- Email: email do contacto.
- Endereço: endereço de morada do contacto.
- Notas: notas de lembrete.
- Números: lista de números telefónicos associado àquele contacto.
## Pacotes utilizados
import json

from operator import itemgetter

from random import \*
## Listas e Dicionários
- dic\_contactos: dicionário para armazenar as informações dos contactos.
- contactos: lista para armazenar as informações do dicionário dic\_contactos.
- números\_contactos: lista para armazenar as informações dos números de cada contacto.

dic\_contactos = {}

contactos = []

números\_contactos = []
## Funções

**def ajuda()**

- Imprime na tela uma ajuda de como gerir o script da lista de contactos.

```python
def ajuda():

"""

- Ferramenta para gerir uma lista de contactos

Comandos:

lista\_telefonica               Imprime na tela a lista atualizada de contactos

adicionar                      Adiciona um novo contacto

editar [Id]                    Edita o contacto com o identificador [Id]

apagar [Id]                    Elimina o contacto com o identificador [Id]

ordem\_alfabetica               Apresenta a lista total de contactos por ordem alfabética

pesquisar [Nome]               Pesquisa e apresenta os resultados da procura por [Nome] na lista

importar [ficheiro]            Importa uma lista de contactos de um ficheiro [JSON]

extrair [formato][ficheiro]    Extrai a lista de contactos para um ficheiro com um determinado formato 
[YAML],[TXT] ou [XML]. Por padrão será [YAML]

"""
```

help(ajuda)

**def lista\_telefonica()**

- Imprime na tela a lista atualizada de contactos.
- Caso a lista de contactos esteja vazia, imprime na tela uma mensagem para que o usuário utilize a função adicionar() para adicionar contactos a referida lista.

def lista\_telefonica():

`    `print('-' \* 30)

`    `print('\tLista Telefónica')

`    `print('-' \* 30) 

`    `if len(contactos) == 0:

`      `print('Ops, lista vazia!')

`      `print('Utilize a função adicionar() para adicionar contactos.')

`    `else:

`      `for p in contactos:

`        `for k, v in p.items():

`            `print(f'{k}: {v}')

`        `print('-' \* 30)

**def adicionar()**

- Adiciona um novo contacto a lista telefónica.
- Verifica se os números do contacto são do tipo *int*, caso contrário imprime na tela que o formato é inválido e pede ao usuário para digitar a informação novamente.
- Adiciona todos os contactos do dicionário *dic\_contactos* para a lista *contactos*.

def adicionar():

`    `while True:

`        `x = randint(0, 100000) + int(len(contactos))

`        `try:

`            `print(f"ID: {x}")

`            `nome\_contacto = input('Nome: ').strip().title()

`            `sobrenome\_contacto = input('Sobrenome: ').strip().title()

`            `email = input('email: ').strip().lower()

`            `endereço = input('Endereço: ').strip().title()

`            `notas = input('Notas: ').strip().title()

`            `break

`        `except ValueError:

`            `print('Desculpe, formato inválido!')

`            `continue

`    `dic\_contactos['Id'] = x

`    `dic\_contactos['Nome'] = nome\_contacto

`    `dic\_contactos['Sobrenome'] = sobrenome\_contacto

`    `dic\_contactos['email'] = email

`    `dic\_contactos['Endereço'] = endereço

`    `dic\_contactos['Notas'] = notas

`    `while True:

`        `try:

`            `numero = int(input('Quantos números esse contato possui? '))

`            `numeros\_contactos.clear()

`            `for i in range(0, numero):

`                `num = int(input(f'Número {i+1}: '))

`                `numeros\_contactos.append(num)

`                `dic\_contactos['Números'] = numeros\_contactos[:]

`            `contactos.append(dic\_contactos.copy())

`            `break

`        `except ValueError:

`            `print('Desculpe, formato inválido!')

`            `continue

**def editar()**

- Edita um contacto da lista telefónica a partir do id.
- Após o usuário passar o parâmetro Id pretendido, a função irá pedir para o usuário digitar as informações de *id, nome, sobrenome, email, endereço, notas e números do contacto* novamente.
- :param Id: identificador do contacto.

def editar(Id):

`    `if len(contactos) == 0:

`        `print('Ops, lista vazia!')

`        `print('Utilize a função adicionar() para adicionar contactos.')

`    `else:

`        `Id = int(Id)

`        `for p in range(len(contactos)):

`            `if contactos[p]['Id'] == Id:

`                `x = contactos[p]['Id']

`                `while True:

`                    `try:

`                        `contactos[p]['Nome']  = input('Nome: ').strip().title()

`                        `contactos[p]['Sobrenome'] = input('Sobrenome: ').strip().title()

`                        `contactos[p]['email'] = input('email: ').strip().lower()

`                        `contactos[p]['Endereço'] = input('Endereço: ').strip().title()

`                        `contactos[p]['Notas'] = input('Notas: ').strip().title()

`                        `break

`                    `except ValueError:

`                        `print('Desculpe, formato inválido!')

`                        `continue

`                `while True:

`                    `try:

`                        `numero = int(input('Quantos números esse contato possui? '))

`                        `numeros\_contactos.clear()

`                        `for i in range(0, numero):

`                            `num = int(input(f'Número {i+1}: '))

`                            `numeros\_contactos.append(num)

`                            `contactos[p]['Números'] = numeros\_contactos[:]

`                    `except ValueError:

`                        `print('Desculpe, formato inválido!')

`                        `continue

`                    `else:

`                        `break

**def apagar()**

- Apaga um contacto da lista telefónica a partir do id.
- Após o usuário passar o parâmetro id pretendido, a função irá deletar o contacto da lista telefónica.
- :param Id: identificador do contacto.

def apagar(Id):

`    `if len(contactos) == 0:

`        `print('Ops, lista vazia!')

`        `print('Utilize a função adicionar() para adicionar contactos.')

`    `else:

`        `Id = int(Id)

`        `for p in range(len(contactos)):

`            `if contactos[p]['Id'] == Id:

`                `del contactos[p]

`                `print("ID deletado com sucesso!")

`                `break

**def ordem\_alfabetica()**

- Ordena todos os contactos da lista telefónica por ordem alfabética, a partir do nome.
- Imprime na tela a lista atualizada de contactos por ordem alfabética, a partir do nome.

def ordem\_alfabetica():

`    `if len(contactos) == 0:

`        `print('Ops, lista vazia!')

`        `print('Utilize a função adicionar() para adicionar contactos.')

`    `else:

`        `contactos\_ordenado = sorted(contactos, key=itemgetter('Nome')) 

`        `print('-' \* 30)

`        `print('\tLista Telefónica')

`        `print('       em ordem alfabética')

`        `print('-' \* 30) 

`        `for p in contactos\_ordenado:

`            `for k, v in p.items():

`                `print(f'{k}: {v}')

`            `print('-' \* 30)

**def pesquisar()**

- Imprime na tela o contacto pesquisado.
- :param Nome: nome do contacto.

def pesquisar(Nome):

`    `if len(contactos) == 0:

`        `print('Ops, lista vazia!')

`        `print('Utilize a função adicionar() para adicionar contactos.')

`    `else:

`        `for p in range(len(contactos)):

`            `if contactos[p]['Nome'] == Nome.title(): 

`                `print(contactos[p])

`                `break

`            `else:

`                `print("Desculpa, o Nome deste contacto não se encontra no banco de dados.")

`                `break

**def importar()**

- Importa uma lista de contactos de um ficheiro.
- Adiciona ao ficheiro importado a lista de contactos criada no script.
- Extrai um ficheiro em formato JSON com a lista completa de contactos.
- Extrai um ficheiro com a lista telefónica do script.
- É necessário informar o caminho do ficheiro.
- :param ficheiro: ficheiro a ser importado.

\*\* Usamos o ficheiro *importa\_contactos.json* que é um ficheiro JSON com informações fictícias de contactos. Esse ficheiro possui as seguintes chaves: id, nome, sobrenome e números.

def importar(ficheiro):

`    `f = open(ficheiro)

`    `novos\_contactos = json.load(f)



**This document was truncated here because it was created in the Evaluation Mode.**
**Created with an evaluation copy of Aspose.Words. To discover the full versions of our APIs please visit: https://products.aspose.com/words/**
