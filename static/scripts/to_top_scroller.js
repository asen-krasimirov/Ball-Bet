
//Get the button
const toTopBtn = document.getElementById("to-top");

// When the user scrolls down 20px from the top of the document, show the button
window.onscroll = function() {scrollFunction()};
toTopBtn.addEventListener('click', toTopFun)

function scrollFunction() {
  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    toTopBtn.style.display = "block";
  } else {
    toTopBtn.style.display = "none";
  }
}

// When the user clicks on the button, scroll to the top of the document
function toTopFun() {
  document.body.scrollTop = 0;
  document.documentElement.scrollTop = 0;
}