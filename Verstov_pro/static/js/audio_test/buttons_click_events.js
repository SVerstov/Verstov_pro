const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
var user_score = [0,0];

function sendStatistic(csrftoken, song_id, answer) {

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
        voteButton.addEventListener('click', showAudioQuality);
    };
};

window.addEventListener('load', addVoteListeners);


function showAudioQuality() {
    let song_id = this.attributes.song_id.value;
    let song_buttons = document.getElementsByClassName(song_id);

    for (let btn of song_buttons) {
        btn.innerText = btn.attributes.tip.value;
        btn.removeEventListener('click', showAudioQuality)
    }
    ;


    let answer = this.attributes.answer.value;
    if (answer === 'wav') {
        this.classList.add("btn-success");
        this.classList.remove("btn-secondary");
        user_score[0]++
        user_score[1]++
    } else {
        this.classList.add("btn-danger");
        user_score[1]++
    };
    updateUserScore();


    this.classList.remove("btn-secondary");
    sendStatistic(csrftoken, song_id, answer);
};

function updateUserScore(){
    let res = document.getElementById('userScore');
    res.innerText = user_score[0] + ' из ' + user_score[1];

};

