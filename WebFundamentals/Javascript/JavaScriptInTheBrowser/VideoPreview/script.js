console.log("page loaded...");

var myVideo = document.getElementById("theVideo");

function playTheVideo() {
    if (myVideo.paused)
        myVideo.play();
    else
        myVideo.pause();
}

function pauseTheVideo() {
        myVideo.pause();
}