const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
alert('js ok')
var vote_buttons = document.getElementsByClassName('vote');


function testAlarm(){
    console.log('click');
};


for (let i in vote_buttons){
  vote_buttons[0].addEventListener('click', testAlarm)
};



function sendRequest(csrftoken) {

    // var xhr = new XMLHttpRequest;
    // xhr.open('GET', 'request/');
    // xhr.send();

    fetch('request/', {
        method: 'POST',
        headers: {
            'X-CSRFToken': csrftoken,
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
    });

}

