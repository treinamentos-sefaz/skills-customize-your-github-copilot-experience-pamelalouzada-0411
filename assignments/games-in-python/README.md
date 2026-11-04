# 📘 Atividade: Jogo da Forca

## 🎯 Objetivo

Nesta atividade, você vai construir um jogo da Forca em Python para praticar manipulação de strings, loops e condicionais. Ao final, você terá um jogo interativo com regras claras de vitória e derrota.

## 📝 Tarefas

### 🛠️	Preparar a palavra secreta e o estado inicial

#### Descrição
Crie a base do jogo definindo uma lista de palavras possíveis, escolhendo uma palavra secreta aleatoriamente e exibindo o progresso inicial com traços ou sublinhados.

#### Requisitos
O programa concluído deve:

- Definir uma lista predefinida com pelo menos 5 palavras.
- Selecionar uma palavra secreta aleatoriamente dessa lista.
- Exibir a palavra oculta no formato `_ _ _` (um marcador para cada letra).
- Definir um número inicial de tentativas incorretas restantes.


### 🛠️	Implementar a lógica de jogo

#### Descrição
Implemente o loop principal para receber palpites de letras, atualizar o estado do jogo e finalizar quando o jogador vencer ou perder.

#### Requisitos
O programa concluído deve:

- Solicitar uma letra por rodada e validar a entrada do usuário.
- Atualizar a exibição da palavra quando a letra existir na palavra secreta.
- Reduzir tentativas apenas quando o palpite estiver incorreto.
- Encerrar o jogo com mensagem de vitória ao revelar toda a palavra.
- Encerrar o jogo com mensagem de derrota quando as tentativas acabarem.