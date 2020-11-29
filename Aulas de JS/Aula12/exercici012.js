var Agora = new Date()
var hora = Agora.getHours() // pega a hora do relogio do sistema
console.log(`Agora é ${hora} horas`)
if (hora < 12) {
    console.log('Bom dia!')
} else if (hora <= 18) {
    console.log('Boa tarde')
} else {
    console.log('Boa noite')
}