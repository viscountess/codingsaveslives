
window.history.forward(); 
function noBack() { 
    window.history.forward();}
    
function KeyPress(e) {
    var evtobj = window.event? event : e
    if (evtobj.keyCode == 77 && evtobj.ctrlKey){
        window.location.replace(href="/error_404_display");
    }
}
document.onkeydown = KeyPress;


