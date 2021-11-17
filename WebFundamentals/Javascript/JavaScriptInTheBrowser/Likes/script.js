var like = document.querySelectorAll(".likes");

function addLike(post) {
    var numLike = like[post].innerHTML;
    numLike++;
    like[post].innerHTML=numLike;
}