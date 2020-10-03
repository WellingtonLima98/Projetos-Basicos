let salvo
let resultado

function botao (numero) {
    salvo = document.calc.visor.value += numero
}

function reseta () {
    document.calc.visor.value = ''
}

function calcula () {
    resultado = eval(salvo)
    document.calc.visor.value = resultado.toLocaleString('pt-br') // faz aparecer o ponto para separar dezena, centena e milhar
}