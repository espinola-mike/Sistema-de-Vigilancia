document.addEventListener('DOMContentLoaded', e => {
    let fechaInicial = document.getElementById('fecha_inicial');
    let fechaFinal = document.getElementById('fecha_final');
    let fecha = new Date();
    // const options = { year: 'numeric', month: 'numeric', day: 'numeric' };
    fechaInicial.setAttribute('max', fecha.toLocaleDateString().split('/').reverse().join('-'));
    fechaFinal.setAttribute('max', fecha.toLocaleDateString().split('/').reverse().join('-'));
    fechaInicial.setAttribute('value', fecha.toLocaleDateString().split('/').reverse().join('-'));
    fechaFinal.setAttribute('value', fecha.toLocaleDateString().split('/').reverse().join('-'));
});