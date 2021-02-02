function verificar() {
    var data = new Date()
    var ano = data.getFullYear()
    var fano = document.getElementById('txtano')
    var res = document.querySelector('div#resultado')
    if (fano.value.length == 0 || Number(fano.value) > ano) {
        alert('[ERRO] Verifique e tente novamente')
    } else {
        var fradgen = document.getElementsByName('radgen')
        var idade = ano - Number(fano.value)
        var genero = ''
        var img = document.createElement('img')
        img.setAttribute('id', 'foto') // cria img com id foto
        if (fradgen[0].checked) {
            genero = 'Masculino'
            if (idade >= 0 && idade < 14) {
                //crianca
                img.setAttribute('src', 'images/homem-crianca-250.png')
            } else if (idade < 20) {
                //jovens
                img.setAttribute('src', 'images/homem-jovem-250.png')
            } else if (idade < 50) {
                // adulto
                img.setAttribute('src', 'images/homem-adulto-250.png')
            } else {
                //idoso
                img.setAttribute('src', 'images/homem-idoso-250.png')
            }

        } else if (fradgen[1].checked) {
            genero = 'Feminino'
            if (idade >= 0 && idade < 14) {
                //crianca
                img.setAttribute('src', 'images/mulher-crianca-250.png')
            } else if (idade < 20) {
                //jovens
                img.setAttribute('src', 'images/mulher-jovem-250.png')
            } else if (idade < 50) {
                // adulto
                img.setAttribute('src', 'images/mulher-adulta-250.png')
            } else {
                //idoso
                img.setAttribute('src', 'images/mulher-idos-250.png')
            }
        } else {
            genero = 'Não Binário'
            img.setAttribute('src', 'images/n-bi-250.png')
        }
        res.innerHTML = `Detactamos ${genero} com ${idade} anos.`//14:47
        res.appendChild(img)
    }
}