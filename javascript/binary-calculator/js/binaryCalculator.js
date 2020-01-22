let binaryEquation = '';
let operationPressed = false;

const clickOnNumber = (btn) => {
    let result = document.getElementById("res");
    binaryEquation+=btn.target.getAttribute('value');
    result.innerHTML = binaryEquation;
};

const clickOnOperation = (btn) => {
    if(! operationPressed){
        let result = document.getElementById("res");
        binaryEquation+=btn.target.getAttribute('value');
        result.innerHTML = binaryEquation;
        operationPressed = true
    }
};

const clickOnClear = () => {
    let result = document.getElementById("res");
    binaryEquation="";
    result.innerHTML = binaryEquation;
    operationPressed = false;
};

const clickOnEql = () => {
    let result = document.getElementById("res");
    let values = [];

    if(binaryEquation.includes("+")){
        values = binaryEquation.split('+');
        let num1 = parseInt(values[0],2);
        let num2 = parseInt(values[1],2);
        result.innerHTML = (num1+num2).toString(2);
    } else if(binaryEquation.includes("-")){
        values = binaryEquation.split('-');
        let num1 = parseInt(values[0],2);
        let num2 = parseInt(values[1],2);
        result.innerHTML = (num1-num2).toString(2);
    } else if(binaryEquation.includes("*")){
        values = binaryEquation.split('*');
        let num1 = parseInt(values[0],2);
        let num2 = parseInt(values[1],2);
        result.innerHTML = (num1*num2).toString(2);
    } else if(binaryEquation.includes("/")){
        values = binaryEquation.split('/');
        let num1 = parseInt(values[0],2);
        let num2 = parseInt(values[1],2);
        result.innerHTML = (Math.floor(num1/num2)).toString(2);
    }
    binaryEquation = '';
    operationPressed = false;

};

const setButtonFunction = () =>{
    document.getElementById("btn0").onclick = clickOnNumber;
    document.getElementById("btn1").onclick = clickOnNumber;
    document.getElementById("btnSum").onclick = clickOnOperation;
    document.getElementById("btnSub").onclick = clickOnOperation;
    document.getElementById("btnMul").onclick = clickOnOperation;
    document.getElementById("btnDiv").onclick = clickOnOperation;
    document.getElementById("btnClr").onclick = clickOnClear;
    document.getElementById("btnEql").onclick = clickOnEql;
};

setButtonFunction();