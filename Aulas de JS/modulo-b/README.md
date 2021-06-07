# Módulo B

Neste módulo é apresentado como armazenar variáveis, assim como tratar-las, converter-las. Juntamente a isso os tipos primitivos e as  operações básicas.

## Variáveis e Tipos Primitivos

### Declarando a variável

Para criar uma variável, no JS, temos que declara-la, mas diferente da linguagem C, não precisamos dizer seu tipo, somente dizer que é uma variável.

Dessa forma, a variável possui a declaração que pode ser: var, let e const. Elas possuem diferença com seu escopo, mas essa diferença não será abordada aqui.

### Nomes de variáveis

No JavaScript as variáveis podem receber `letras`, `$` ou `_`. Porém, não podem começar com números no início, mas pode ser usado acentos e não pode haver espaços dentre o nome da variável. Ademais, as letras maiúsculas e minúsculas fazem diferença.

### Tipos Primitivos

O JS não diferencia float, int ... todos podem ser um Number, mas há a possibilidade de se usar especificamente um tipo específico. Dessa forma, para saber o tipo do dado podemos usar o método `typeof()`. Os tipos primitivos são:
    
1. Number
    - Infinity
    - NaN ( Not a Number)
2. String
3. Boolean
4. Null
5. Undefined
6. Object
    - Array
7. Function

## Tratamento de dados

Tratar os dados é muito importante, para que assim possamos, por exemplo, realizar a soma de dois números. Em alguns casos, o usuário pode dar os seguintes dados: '1' e '2', e desta forma caso haja uma atribuição, o resultado será 12 e não 3. Para que a operação seja feita com sucesso devemos converter os dados que, nesse caso estão em string, para um número do tipo que será trabalhado ( int, float ...).

### Converter String para Número

Quando temos um dado em string e queremos converter para um tipo onde podemos calcular, temos a opção de passar para o tipo específico que queremos, ou simplesmente passar para um NUMBER, das seguintes formas abaixo:

- `Number.parseInt(número)` → transforma de string para inteiro
- `Number.parseFloar(número)` → transforma de string para float
- `Number(número)` → transforma de string para o tipo que o JS identificar

### Converter Número para String

Assim como é necessário converter de string para número, também se é necessário em alguns momentos transformar de número para string. Para isso, os dois métodos abaixo nos ajudam nesse problema:

- `String(variável)`
- `variável.toString()`

### Formatando Strings

Dentro das strings é muito importante nos tratarmos elas, as fazer usando elas todas em minúsculas, ou todas em maiúsculas. Ou até mesmo, substituir um elemento por outro, para isso estão listadas algumas formas de se fazer isso aqui abaixo:

- `variável.length` → Ajuda a ver o tamanho da string
- `variável.toUpperCase()` → Deixa a string toda em maiúsculo
- `variável.toLowerCasa()` → Deixa a string toda em  minúsculo
- `variável.toFixed(quantidade de casas)` → Aqui podemos dizer quantas casas após a virgula queremos, no caso de um Float
- `variável.toFixed(quantidade de casas).replace('.', ',')` → Nesse caso esta substituindo o ponto (.) por uma vírgula (,)
- `document.write('escreve o que tem aqui no body')` → Aqui o que é escrito aparece no body, podemos usar tags html também

### Template String

Este método surgiu para facilitar um pouco na hora de escrever a string junto com variáveis. Pois, ao invés de se usar, por exemplo, `console.log('EU ESTOU APRENDENDO' + VARIÁVEL + '!')` podemos usar desta forma: `console.log(`EU ESTOU APRENDENDO ${VARIÁVEL}!`)`, aqui fica difícil de mostrar, porém ao invés da primeira onde usamos '' (aspas simples, mas poderia usar também aspas duplas "") usamos `` (crase)

## Operadores

### Tipos de operadores

### Aritméticos
### Atribuição
### Relacionais
### Lógicos
### Ternário