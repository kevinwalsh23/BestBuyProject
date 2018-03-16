$("#myCarousel").carousel();

$('.carousel').carousel({
  interval: 5000
});

$(".left").click(function(){
    $("#myCarousel").carousel("prev");
});
$(".right").click(function(){
    $("#myCarousel").carousel("next");

});
