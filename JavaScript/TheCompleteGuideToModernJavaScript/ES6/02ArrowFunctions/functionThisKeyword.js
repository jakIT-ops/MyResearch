document.addEventListener("DOMContentLoaded", function () {
  const box = document.querySelector(".box");
// listen for a click event
box.addEventListener("click", function() {
  // toggle the class opening on the div
  this.classList.toggle("opening");
  setInterval(function(){
    // try to toggle again the class
    this.classList.toggle("opening");
    },500);
});
});
