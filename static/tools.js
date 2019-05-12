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