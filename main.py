"""
Criar um sistema quer permita o usuário cadastrar o nome, cpf e data de nascimento, 
salvar os dados num csv (use pandas) e que seja possível exportar os dados cadastrados, 
porém ocultando os 8 últimos digitos (exemplo: 851********)
"""

from datetime import datetime
import pandas as pd

name = input('digite o seu nome: ')

cpf = input('digite o seu cpf: ')
if len(cpf) != 11:
    raise Exception('o cpf deve ter 11 caracteres')

birthday = input('digite sua data de nascimento: ')
birthday = datetime.strptime(birthday, '%d/%m/%y')

raw_data = {'name': [name],
            'cpf': [cpf],
            'birthday': [birthday]}

df = pd.DataFrame(raw_data, columns = ['name', 'cpf', 'birthday'])
print(df)

df.to_csv('raw_data.csv')





