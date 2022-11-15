function detectar_fecha_actual () {
    let fechaInicial = document.getElementById('fecha_inicial');
    let fechaFinal = document.getElementById('fecha_final');
    let fecha = new Date();
    // const options = { year: 'numeric', month: 'numeric', day: 'numeric' };
    fechaInicial.setAttribute('max', fecha.toLocaleDateString().split('/').reverse().join('-'));
    fechaFinal.setAttribute('max', fecha.toLocaleDateString().split('/').reverse().join('-'));
    fechaInicial.setAttribute('value', fecha.toLocaleDateString().split('/').reverse().join('-'));
    fechaFinal.setAttribute('value', fecha.toLocaleDateString().split('/').reverse().join('-'));
}


document.addEventListener('DOMContentLoaded', e => {
    detectar_fecha_actual();
    let fechaInicial = document.getElementById('fecha_inicial');
    let fechaFinal = document.getElementById('fecha_final');
    fechaFinal.addEventListener('click', e => {
        fechaFinal.setAttribute('min', fechaInicial.value)
        fechaInicial.setAttribute('max', fechaFinal.value)
    })
    fechaInicial.addEventListener('click', e => {
        fechaInicial.setAttribute('max', fechaFinal.value)
        fechaFinal.setAttribute('min', fechaInicial.value)
    })
});