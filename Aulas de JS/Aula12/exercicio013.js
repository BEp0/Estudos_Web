var agora = new Date() // pega os dados do sistema
var diasema = agora.getDay() // pega o dia do sistema

switch(diasema) { // cria casos 
    case 0:
        console.log('Domingo')
        break
    case 1:
        console.log('Segunda')
        break
    case (diasema = 2): // exemplo da mesma coisa
        console.log('Terça')
        break
    case 3:
        console.log('Quarta')
        break
    case 4:
         console.log('Quinta')
         break
    case 5:
        console.log('Sexta')
        break
    case 6:
        console.log('Sábado')
        break
}
