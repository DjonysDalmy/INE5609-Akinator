# Akinator

## Descrição

A idéia para o trabalho é utilizar uma árvore de grau 2.

A Árvore vai coletando informações sobre um tipo de coisas e, num jogo de perguntas e respostas, vai aprendendo mais e mais. Por exemplo, sobre animais. Ela deve começar com alguma informação já incluída para começar o "jogo" (no nosso exemplo de animais, pode ser uma baleia). O jogo começa assim:

1 - O software pede para o usuário "Pense em um animal\*!" (neste exemplo)

2 - O software acessa a raiz da árvore e, se é um animal, pergunta ao usuário se é aquele animal ("Você pensou em uma baleia?")

3 - a) Caso a resposta seja positiva, o jogo recomeça.

3 - b) Caso seja negativa, o software então pergunta "Qual foi o animal que você pensou?" (ao que o usuário responderá, por exemplo "Cachorro") e em seguida, o software pergunta "Como uma baleia é diferente de Cachorro?" ou "Diga uma característica da baleia que é diferente de cachorro" Exemplo de respostas: "É aquático". Assim, o software deverá incluir na árvore essas informações que diferenciam cachorro e baleia e reiniciar o jogo (agora ele poderá perguntar "É aquático?" e caso positivo o software chutará "Baleia"e caso negativo ele chutará "Cachorro" e o jogo recomeça.

Árvore:

```
   Pergunta
  /        \
Sim         Não
```

Json:

```json
["Pergunta", ["Sim", "Não"]]
```

Essa árvore tem 2 tipos de nó:

- O que contém animais

- O que contém perguntas

Árvore:

```
    Pergunta
    /      \
 Animal   Pergunta
          /      \
       Animal   Animal
```

Json:

```json
["Pergunta", ["Animal", ["Pergunta", ["Animal", "Animal"]]]]
```

Os animais serão sempre folhas, as perguntas sempre terão 2 saídas (resposta positiva e negativa), que poderá levar a outra pergunta ou a um animal.

Usem algum esquema para guardar a árvore no disco ao final de uma sessão de jogo (comandada por alguma opção de menu), e recarregar a árvore ao iniciar uma nova sessão (também pode ser por menu).

## Utilização

```bash
python3 index.py
```

## Sistema de Saves

É possível manipular diferentes árvores com dados novos/diferentes a partir das opções do menu principal. Por padrão a primeira lista (Árvore) do Json será o "save" selecionado.

## Exemplo de árvore

Árvore:

```
   Faz miau?
  /        \
Gato      Sabe Voar?
          /         \
      Gaivota    É Selvagem?
                /           \
    Sobe em árvores?        Dá pra andar em cima?
    /              \              /           \
Macaco        Tem tromba?      Cavalo      Cachorro
              /         \
         Elefante       Lobo
```

Json:

```json
["Faz miau?",["Gato",["Sabe voar?",["Gaivota",["É selvagem?",[["Sobe em árvores?",["Macaco",["Tem uma tromba?",["Elefante", "Lobo"]]]],["Dá pra andar em cima?",["Cavalo", "Cachorro"]]]]]]]],
```
