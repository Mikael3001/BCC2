function ready(fn) {
    if (document.attachEvent ? document.readyState === "complete" : document.readyState !== "loading") {
        fn();
    } else {
        document.addEventListener('DOMContentLoaded', fn);
    }
}

function d() {
    $.cookie("saldo", 0)
    location.reload()
}

ready(function a() {
    if (isNaN($.cookie("saldo")))
        $.cookie("saldo", 0)

    var valorcookie = $.cookie("saldo")
    var span = document.getElementById("saldoatual")
    span.innerHTML = valorcookie
})