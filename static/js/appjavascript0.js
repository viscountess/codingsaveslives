
// trigger for ctrl m
function KeyPress(e) {
    var evtobj = window.event? event : e
    if (evtobj.keyCode == 77 && evtobj.ctrlKey){
        window.location.replace(href="/error_404_display");
    }
}
document.onkeydown = KeyPress;



