function ready(fn) {
    if (document.attachEvent ? document.readyState === "complete" : document.readyState !== "loading") {
        fn();
    } else {
        document.addEventListener('DOMContentLoaded', fn);
    }
}

function d() {
    var input = document.getElementById("valor-digitado")
    var valorDigitado = input.value
    if (isNaN(parseFloat(valorDigitado))) { // Se o valor digitado não for um número
        alert("Valor Digitado não é um número");
        return;
    }
    var cookie = $.cookie("saldo")
    cookie = parseInt(cookie) - parseInt(valorDigitado)
    $.cookie("saldo", cookie)
    alert("Seu saldo atual é: " + cookie)
    input.value = ""
    location.reload()
}

ready(function a() {
    if (isNaN($.cookie("saldo")))
        $.cookie("saldo", 0)

    var valorcookie = $.cookie("saldo")
    var span = document.getElementById("saldoatual")
    span.innerHTML = valorcookie
})