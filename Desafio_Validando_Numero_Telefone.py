'''Forma na qual permite que o parentêses seja opcional.
# Conheça mais sobre o Regex: https://docs.python.org/pt-br/3.8/howto/regex.html
# Conheça mais sobre o 're' do python: https://docs.python.org/pt-br/3/library/re.html

# Módulo 're' que fornece operações com expressões regulares.
import re


# TODO: Crie uma função chamada 'validate_numero_telefone' que aceite um argumento 'phone_number':
def validate_numero_telefone(phone_number):
    
    # TODO: Defina um padrão de expressão regular (regex) para validar números de telefone no formato (XX) 9XXXX-XXXX:
    # O padrão deve começar (^) e terminar ($) para garantir que a string inteira corresponda.
    # \(?\d{2}\)?  -> Opcional parênteses no DDD (ex: (11) ou 11)
    # \s?         -> Espaço opcional
    # 9\d{4}-\d{4} -> O '9' fixo, seguido de 4 dígitos, hífen e mais 4 dígitos
    pattern = r"^\(?\d{2}\)?\s?9\d{4}-\d{4}$"
    
    # A função 're.match()' para verifica se o padrão definido corresponde ao número de telefone fornecido.
    # O 're.match()' retorna um objeto 'match' se houver correspondência no início da string, caso contrário, retorna 'None'.
    if re.match(pattern, phone_number): 
        
        # TODO: Agora crie um return, para retornar que o número de telefone é válido:
        return "Número de telefone válido."
        
    # TODO: Crie um else e return, caso não o número de telefone seja inválido:
    else:
        return "Número de telefone inválido."
    

# Solicita ao usuário que insira um número de telefone e armazena o valor fornecido na variável 'phone_number'.
phone_number = input()  

# TODO: Chame a função 'validate_numero_telefone()' com o número de telefone fornecido como argumento e armazene o resultado retornado na variável 'result'.
result = validate_numero_telefone(phone_number)

# Imprime o resultado:
print(result)'''


# Conheça mais sobre o Regex: https://docs.python.org/pt-br/3.8/howto/regex.html
# Conheça mais sobre o 're' do python: https://docs.python.org/pt-br/3/library/re.html

# Módulo 're' que fornece operações com expressões regulares.
import re


# TODO: Crie uma função chamada 'validate_numero_telefone' que aceite um argumento 'phone_number':
def validate_numero_telefone(phone_number):
    
    # TODO: Defina um padrão de expressão regular (regex) para validar números de telefone no formato (XX) 9XXXX-XXXX:
    # Ajustado para OBRIGAR o DDD entre parênteses e o espaço após.
    # r"^\(\d{2}\)\s9\d{4}-\d{4}$"
    # ^             -> Início da string
    # \(            -> Abre parênteses LITERAL (precisa escapar com \)
    # \d{2}         -> Dois dígitos (DDD)
    # \)            -> Fecha parênteses LITERAL (precisa escapar com \)
    # \s            -> Um espaço em branco LITERAL
    # 9\d{4}        -> O '9' fixo seguido de 4 dígitos
    # -             -> Hífen LITERAL
    # \d{4}         -> Quatro dígitos
    # $             -> Fim da string
    pattern = r"^\(\d{2}\)\s9\d{4}-\d{4}$"
    
    # A função 're.match()' para verifica se o padrão definido corresponde ao número de telefone fornecido.
    # O 're.match()' retorna um objeto 'match' se houver correspondência no início da string, caso contrário, retorna 'None'.
    if re.match(pattern, phone_number): 
        
        # TODO: Agora crie um return, para retornar que o número de telefone é válido:
        return "Número de telefone válido."
        
    # TODO: Crie um else e return, caso não o número de telefone seja inválido:
    else:
        return "Número de telefone inválido."
    

# Solicita ao usuário que insira um número de telefone e armazena o valor fornecido na variável 'phone_number'.
phone_number = input()  

# TODO: Chame a função 'validate_numero_telefone()' com o número de telefone fornecido como argumento e armazene o resultado retornado na variável 'result'.
result = validate_numero_telefone(phone_number)

# Imprime o resultado:
print(result)