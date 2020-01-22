const changeButtonValue = (btnId,newValue) => {
    var btn1 = document.getElementById("btn"+btnId);
    var oldValue = btn1.innerHTML;
    btn1.innerHTML = newValue;
    return oldValue
}

const moveButtonOrientation = (btn) => {
    var oldValue = 0;
    var changeOrder = [1,2,3,6,9,8,7,4]
    changeOrder.forEach( i => {
        if(i==1){
            let newValueButton = document.getElementById("btn4")
            oldValue = newValueButton.innerHTML
        }
        oldValue = changeButtonValue(i,oldValue)
    })
        
}

const buttonGenerator = () => {
    var buttonContainer = document.createElement('Div')
    buttonContainer.className = "buttonContainer"
    buttonContainer.id = "btns"
    for(let i=1;i<10;i++){
        let btn = document.createElement('Button')
        btn.id = "btn"+i
        btn.className = "buttonClass"
        btn.innerHTML = i
        if(i==5){btn.onclick = moveButtonOrientation}
        buttonContainer.appendChild(btn)
    }
    return buttonContainer
}
console.log(buttonGenerator())
document.body.appendChild(buttonGenerator())