//explaining the m Error page shortcut;
var welcome = "Welcome to Maia! If you ever need to hide your screen, just click the button on the side, or type 'm' and we will show an Error page! For your safety, it will not be possible to see what you were previously looking at by then pressing the 'back' button.";
    (alert(welcome));


//m trigger;
(document.addEventListener('keypress', function(event) {
    if (event.key === 'm');{
        window.location.replace(href="..templates\Error_404_Display.html");
    }
  }));