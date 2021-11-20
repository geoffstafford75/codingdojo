console.log("page loaded...");

function changeName() {
    var name = document.querySelector(".card-body h1");
    name.innerHTML = "New Name";
}

var newConnections = document.querySelectorAll(".new-connection");


function accept(num) {
    
    newConnections[num].remove(); 
    document.getElementById("new-connection-badge").innerText--;

    // increment connection badge when accepting
    document.getElementById("connection-badge").innerText++;

}

function decline(num) {
    newConnections[num].remove();
    document.getElementById("new-connection-badge").innerText--;
}
