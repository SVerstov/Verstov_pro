// shuffle audio elements

var songs = document.getElementsByClassName('song')

for (song of songs){
    for (var i = song.children.length; i >= 0; i--) {
    song.appendChild(song.children[Math.random() * i | 0]);
    };
};
