function print(text) {
    console.log(text);
}

function checkUserExists(usersList) {
    var inputBox = document.getElementById('participant-id');
    var warningCont = document.getElementById('warning-container')
    var submitElem = document.getElementById('submit-participant-id')
    if (usersList.indexOf(inputBox.value) != -1) {
        warningCont.removeAttribute('hidden')
        submitElem.setAttribute('disabled', '')
    } else {
        warningCont.setAttribute('hidden', '')
        submitElem.removeAttribute('disabled')
    }
}

function hide(elemArray) {
    for (i = 0; i < elemArray.length; i++) {
        document.getElementById(elemArray[i]).setAttribute('hidden', '')
    }
}

function show(elemArray) {
    for (i = 0; i < elemArray.length; i++) {
        document.getElementById(elemArray[i]).removeAttribute('hidden')
    }
}

function clickRadioButton(clickedCell) {
    clickedCell.childNodes[0].click();
}