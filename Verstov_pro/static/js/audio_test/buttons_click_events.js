const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

function sendRequest(csrftoken, song_id, answer) {


    fetch('request/', {
        method: 'POST',
        headers: {
            'X-CSRFToken': csrftoken,
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Song-Id': song_id,
            'Answer': answer,
        },
    });

}


function addVoteListeners() {
    var voteButtons = document.getElementsByClassName('vote');

    for (let voteButton of voteButtons) {
        voteButton.addEventListener('click', voteBtnClick);
    }
    ;
};

window.addEventListener('load', addVoteListeners);


function voteBtnClick() {
    var song_id = this.attributes.song_id.value;
    var song_buttons = document.getElementsByClassName(song_id);

    for (let btn of song_buttons) {
        btn.innerText = btn.attributes.tip.value;
        btn.removeEventListener('click', voteBtnClick)
    }
    ;

    var answer = this.attributes.answer.value;
    if (answer === 'wav') {
        this.classList.add("btn-success");
        this.classList.remove("btn-secondary");
    } else {
        this.classList.add("btn-danger");
    };

    this.classList.remove("btn-secondary");

    sendRequest(csrftoken, song_id, answer)
};



