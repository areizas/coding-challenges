let binaryOperation = '';
let equation = '';
let operationPressed = false;

const clickOnNumber = (btn) => {
    let response = document.getElementById("res");
    binaryOperation+=btn.target.getAttribute('value');
    response.innerHTML = binaryOperation;
};

const clickOnOperation = (btn) => {
    if(! operationPressed){
        let response = document.getElementById("res");
        binaryOperation+=btn.target.getAttribute('value');
        response.innerHTML = binaryOperation;
        operationPressed = true
    }
};

const clickOnClear = () => {
    let response = document.getElementById("res");
    binaryOperation="";
    response.innerHTML = binaryOperation;
};

const setButtonFunction = () =>{
    document.getElementById("btn0").onclick = clickOnNumber;
    document.getElementById("btn1").onclick = clickOnNumber;
    document.getElementById("btnSum").onclick = clickOnOperation;
    document.getElementById("btnSub").onclick = clickOnOperation;
    document.getElementById("btnMul").onclick = clickOnOperation;
    document.getElementById("btnDiv").onclick = clickOnOperation;
    document.getElementById("btnClr").onclick = clickOnClear;
};

setButtonFunction();