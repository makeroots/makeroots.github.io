function on() {
    document.getElementById("overlay").style.display = "block";
}
function off() {
    document.getElementById("overlay").style.display = "none";
}
$(window).on('load', function() {
   $("#cover").hide();
});
