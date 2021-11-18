console.log("page loaded...");

function changeName() {
    var name = document.querySelector(".card-body h1");
    name.innerHTML = "New Name";
}

var newConnections = document.querySelectorAll(".new-connection");


function accept(num) {
    
    newConnections[num].remove(); 
    decrementNewConnectionBadge();

    // increment connection badge when accempting
    var connectionBadge = document.getElementById("connection-badge");
    var badge = connectionBadge.innerHTML;
    badge++;
    connectionBadge.innerHTML = badge;


}

function decline(num) {
    newConnections[num].remove();
    decrementNewConnectionBadge();
}

// Decrement New Connection Badg
function decrementNewConnectionBadge() {
    var newConnectionBadge = document.getElementById("new-connection-badge");
    var badge = newConnectionBadge.innerHTML;
    console.log(newConnectionBadge);
    badge--;
    newConnectionBadge.innerHTML = badge;
}
