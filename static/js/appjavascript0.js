//explaining the 'm a' Error page shortcut
var welcome = "Welcome to Maia! If you ever need to hide your screen, just click the button on the side, or type 'm a' and we will show an Error page!";
alert(welcome);

//m a trigger
document.addEventListener('keydown', function(event) {
    if (event.key === 'm' && event.key === 'a') {
      alert('Undo!');
    }
  });