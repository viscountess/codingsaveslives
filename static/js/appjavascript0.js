
function KeyPress(e) {
    var evtobj = window.event? event : e
    if (evtobj.keyCode == 77 && evtobj.ctrlKey){
        window.location.replace(href="Error_404_Display.html");
    }
}
document.onkeydown = KeyPress;


