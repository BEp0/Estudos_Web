function verificar(){
    var data = new Date()
    var ano = data.getFullYear()
    var fano = document.getElementById('txtano')
    var res = document.querySelector('div#resultado')
    if (fano.value.length == 0 || Number(fano.value) > ano){
        alert('[ERRO] Verifique e tente novamente')
    }else {
        var fradgen = document.getElementsByName('radgen')
        var idade = ano - Number(fano.value)
        var genero = ''
        if (fradgen[0].checked) {
            genero = 'Masculino'
        } else if (fradgen[1].checked){
            genero = 'Feminino'
        } else {
            genero = 'Não Binário'
        }
        res.innerHTML = `Detactamos ${genero} com ${idade} anos.`//14:47
    }
}