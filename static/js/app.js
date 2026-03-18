// 🌌 Start → Portale
setTimeout(() => {
    document.getElementById("startscreen").style.display = "none";
    document.getElementById("portal-screen").classList.remove("hidden");
}, 2000);

// 💥 Welt betreten
function enterWorld(world) {

    document.getElementById("portal-screen").style.display = "none";
    document.getElementById("explosion").classList.remove("hidden");

    setTimeout(() => {
        document.getElementById("explosion").style.display = "none";
        document.getElementById("chat-container").classList.remove("hidden");

        addMessage("System", "🌌 Willkommen in: " + world);
    }, 1000);
}

// 🤖 Chat
function send() {
    let input = document.getElementById("input");
    let msg = input.value;

    if (!msg) return;

    addMessage("Du", msg);

    fetch("/chat", {
        method:"POST",
        headers:{"Content-Type":"application/json"},
        body:JSON.stringify({message:msg})
    })
    .then(res=>res.json())
    .then(data=>{
        addMessage("MasterCat", data.reply);
    });

    input.value="";
}

function addMessage(sender,text){
    let box=document.getElementById("chat-box");
    let div=document.createElement("div");
    div.innerHTML="<b>"+sender+":</b> "+text;
    box.appendChild(div);
    box.scrollTop=box.scrollHeight;
}
