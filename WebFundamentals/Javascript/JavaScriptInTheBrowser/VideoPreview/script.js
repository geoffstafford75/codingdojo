console.log("page loaded...");

var myVideo = document.getElementById("theVideo");

function playTheDamnVideo() {
    if (myVideo.paused)
        myVideo.play();
    else
        myVideo.pause();
}

function pauseTheDamnVideo() {
        myVideo.pause();
}