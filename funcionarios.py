import pandas as pd

# Lê o arquivo excel original
arq_funcionarios = pd.read_excel('funcionarios.xlsx')

# Filtrar apenas quem ganha acima de 3000
valor = float(input('Qual o valor minimo do salário? '))
arq_funcionarios_filtrado = arq_funcionarios[arq_funcionarios['salario'] > valor]

# Salva o novo arquivo excel
arq_funcionarios_filtrado.to_excel('funcionarios_acima_3000.xlsx', index=False)
print("Arquivo 'funcionarios_acima_3000.xlsx' criado com sucesso!")


