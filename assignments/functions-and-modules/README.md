# 📘 Atividade: Funções e Módulos em Python

## 🎯 Objetivo

Nesta atividade, você vai aprender a criar funções com parâmetros e valores de retorno, reutilizar código e organizar seu programa em módulos separados com `import`.

## 📝 Tarefas

### 🛠️ Criar funções com parâmetros e retorno

#### Descrição
Defina funções que recebem dados, realizam um cálculo e devolvem um resultado. Comece com funções simples e teste cada uma antes de seguir para a próxima.

#### Requisitos
O programa concluído deve:

- Definir a função `celsius_to_fahrenheit(celsius)` que retorna a temperatura convertida para Fahrenheit.
- Definir a função `is_even(number)` que retorna `True` se o número for par e `False` caso contrário.
- Definir a função `average(numbers)` que retorna a média de uma lista de números.
- Chamar cada função pelo menos uma vez e exibir o resultado com `print()`.


### 🛠️ Usar argumentos padrão e funções que chamam outras funções

#### Descrição
Crie funções mais flexíveis, com valores padrão, e faça uma função usar outra já criada. Isso ajuda a evitar repetição de código.

#### Requisitos
O programa concluído deve:

- Definir a função `greet(name, greeting="Olá")` que retorna a saudação formatada, como `"Olá, Ana!"`.
- Definir a função `describe_number(number)` que retorna `"par"` ou `"ímpar"` usando a função `is_even()` da tarefa anterior.
- Exibir pelo menos duas chamadas de `greet()`: uma usando o valor padrão e outra com um `greeting` personalizado.


### 🛠️ Organizar o código em um módulo

#### Descrição
Mova algumas funções para um arquivo separado e importe-as no programa principal. Isso mostra como dividir um projeto em partes menores e reutilizáveis.

#### Requisitos
O programa concluído deve:

- Criar um arquivo `math_utils.py` contendo as funções `celsius_to_fahrenheit()`, `is_even()` e `average()`.
- Criar um arquivo `main.py` que importa essas funções com `from math_utils import ...` (ou `import math_utils`).
- Executar `python main.py` e obter a mesma saída que na tarefa 1.
- Usar a estrutura `if __name__ == "__main__":` no `main.py`.
