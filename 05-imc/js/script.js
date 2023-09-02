function start(){
    var buttonCalculateImc = document.querySelector('#button-calculate-imc')
    buttonCalculateImc.addEventListener('click', habdleButtonClick);

    var inputWeight = document.querySelector('#input-weight');
    var inputHeight = document.querySelector('#input-height');

    inputWeight.addEventListener('input', handleButtonClick);
    inputHeight.addEventListener('input', handleButtonClick);

    handleButtonClick();

}

function calculateImc(weight, height){
    return weight / (height * height);
}

function habdleButtonClick(){
    var inputWeight = document.querySelector('#input-weight');
    var inputWeight = document.querySelector('#input-height');
    var imcResult = document.querySelector('#imc-result');

    var weight = inputWeight.value;
    var height = inputWeight.value;

    var imc = calculateImc(weight, height);
    var formattedImc = imc.toFixed(2).replace('.', ',');
    
    imcResult.textContent = formattedImc;


    
}

start();