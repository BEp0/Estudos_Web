# Modulo C - Eventos D. O. M

Vimos primeiramente como escrever no HTML usando o JS, através de `.write()`. Também, vimos como atribuir a uma variável a tag HTML usando `.querySelector()` e os diferentes "getElements" que existem. Com isso, podemos mudar o style de um parágrafo, por exemplo, mudando ele de vermelho para azul. Além disso, vimos no `.querySelector()` a diferença de usar "#" e ".", já que o primeiro é para id e o segundo para class.

Na segunda aula vimos os eventos que podemos usar, alguns pois há vários.
Alguns eventos de mouse que vimos:

- mouseenter - quando o mouse entra
- mousemove - quando o mouse se move dentro
- mousedown - quando o mouse é clicado e segurado
- mouseup - quando se solta o mouse
- click - é um clique
- mouseout - quando o mouse sai

> Podemos saber a lista completa no guia de referência da Mozilla ([clicando aqui te leva para a lista](https://developer.mozilla.org/pt-BR/docs/Web/Events))

Para tratar um evento usamos uma função, a função é um bloco que será executado quando o evento acontecer. Delimitamos um bloco com {}, esse bloco devemos nomealo como function, detalhe: podemos ter funções anonimas no JS. Mas, para funcionar devemos dar um nome para essa função e geralmente nomeados com a ação que ocorrerá, nomeado esse nome deve vir acompanhado de parenteses e dentro deles podem ser adicionados paramentros.

Logo abaixo há um exemplo de função:

    function restart() {
            console.log('Olá, mundo!')
        }

Podemos nomear os eventos tanto no HTML e no JS.