
// Pause all audios except one, and restart audio current time

document.addEventListener('play', function(e){
    var audios = document.getElementsByTagName('audio');
    for(var i = 0, len = audios.length; i < len;i++){
        if(audios[i] != e.target){
            audios[i].currentTime = 0;
        }
    }
}, true);