# Modulo C - Eventos D. O. M



Eventos do mouse...
mouseenter - quando o mouse entra
mousemove - quando o mouse se move dentro
mousedown - quando o mouse é clicado e segurado
mouseup - quando se solta o mouse
click - é um clique
mouseout - quando o mouse sai

Podemos saber a lista completa no guia de referência da Mozilla ([clicando aqui te leva para a lista](https://developer.mozilla.org/pt-BR/docs/Web/Events))

Para tratar um evento usamos uma função, a função é um bloco que será executado quando o evento acontecer. Delimitamos um bloco com {}, esse bloco devemos nomealo como function, detalhe: podemos ter funções anonimas no JS. Mas, para funcionar devemos dar um nome para essa função e geralmente nomeados com a ação que ocorrerá, nomeado esse nome deve vir acompanhado de parenteses e dentro deles podem ser adicionados paramentros.

Logo abaixo há um exemplo de função:

    function restart() {
            console.log('Olá, mundo!')
        }

Podemos nomear os eventos tanto no HTML e no JS.