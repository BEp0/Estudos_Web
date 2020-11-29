var lista = [20, 40, 60, 80, 100]
// lista de volocidades
var vel = lista[4] // pega a velocidade da lista
var limite = lista[3] // indica o limite
console.log(`A velocidade é ${vel}`)
//escreve a velocidade
console.log(`O limite é ${limite}`)
// escreve o limite
switch(vel >= limite) {
    // bom para mais de um caso, como aqui so tem dois, pode substituir por um IF
    case true: // se a expressao for verdade, está multado
        console.log('Multado!')
        break
    default: // se não, ta tranquilo
        console.log('Tá trankis')
        break    
}
//mesma coisa só que com o if
if (vel >= limite) {
    console.log('Multa!')
} else {
    console.log('Tranki 0.0')
}