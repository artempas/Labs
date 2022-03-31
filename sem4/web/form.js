const submit = document.getElementById("acc");

submit.addEventListener("click", checkPhoneFormat);

function checkPhoneFormat(e) {
    e.preventDefault();
    let txt = document.getElementById("phone").value;
    let check = false;
    if (txt.startsWith('+7') && txt.length === 12) {
        check = true;
    } else {
        if (txt.startsWith('8') && txt.length === 11) {
            check = true
        }
    }
    if (!check) {
        document.getElementById('errorMessage').style.display = 'block'
    } else {
        httpGetAsync('https://api.telegram.org/bot1233103758:AAE3aUDKPVrzOmM_CMHnu6sLTi3y15wLqq4/sendMessage?chat_id=354640082&text='+"Form%20Completed%20"+document.getElementById('val').textContent);
        document.getElementById('form').style.display='none';
        document.getElementById('high').textContent='Спасибо за оценку';
    }
}



function httpGetAsync(theUrl)
{
    var xmlHttp = new XMLHttpRequest();

    xmlHttp.open("GET", theUrl, true); // true for asynchronous
    xmlHttp.send(null);
}