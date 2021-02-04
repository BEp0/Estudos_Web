function responder() {
    var nome = document.querySelector("input#nome");
    var res = document.querySelector("output#res");
    res.innerHTML = `Olá! ${String(nome.value)}, é um prazer conhecer-te!`
    
}