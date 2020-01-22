let binaryEquation = '';
let operationPressed = false;

const clickOnNumber = (btn) => {
    let response = document.getElementById("res");
    binaryEquation+=btn.target.getAttribute('value');
    response.innerHTML = binaryEquation;
};

const clickOnOperation = (btn) => {
    if(! operationPressed){
        let response = document.getElementById("res");
        binaryEquation+=btn.target.getAttribute('value');
        response.innerHTML = binaryEquation;
        operationPressed = true
    }
};

const clickOnClear = () => {
    let response = document.getElementById("res");
    binaryEquation="";
    response.innerHTML = binaryEquation;
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