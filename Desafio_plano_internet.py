# TODO: Crie uma Função: recomendar_plano para receber o consumo médio mensal:
def recomendar_plano(consumo):
  primeiro_plano = 'Plano Essencial Fibra - 50Mbps'
  segundo_plano = 'Plano Prata Fibra - 100Mbps'
  terceiro_plano = 'Plano Premium Fibra - 300Mbps'
  
  if consumo <= 10:
    return primeiro_plano
    
  elif 10 < consumo <= 20:
    return segundo_plano
    
  elif consumo >= 21:
    return terceiro_plano
    
  else:
    return 'Valor inválido.'
    
# TODO: Crie uma Estrutura Condicional para verifica o consumo médio mensal 
# TODO: Retorne o plano de internet adequado:
    

# Solicita ao usuário que insira o consumo médio mensal de dados:
consumo = float(input())
# Chama a função recomendar_plano com o consumo inserido e imprime o plano recomendado:
print(recomendar_plano(consumo))