quantidade = 1;

function less() {
    quantidade--;
    setValue(quantidade);
}
function more() {
    quantidade++;
    setValue(quantidade);
}
function setValue(value) {
    document.getElementById('quantidade').value = value;
}
setValue(quantidade);


document.getElementById("cpf").addEventListener("input", function() {
    var cpf = this.value.replace(/\D/g, '');
    if (cpf.length > 3) {
      cpf = cpf.substring(0, 3) + '.' + cpf.substring(3);
    }
    if (cpf.length > 7) {
      cpf = cpf.substring(0, 7) + '.' + cpf.substring(7);
    }
    if (cpf.length > 11) {
      cpf = cpf.substring(0, 11) + '-' + cpf.substring(11);
    }
    this.value = cpf;
  });
  

  
const quantidadeDisplay = document.getElementById('num');
const quantidade = document.querySelector('input[name="quantidade"]');

quantidadeDisplay.addEventListener('change', () => {
  quantidade.value = quantidadeDisplay.value;
});
