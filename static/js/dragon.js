//loader
$(window).on('load', function() {
    $('#loaderenv').delay(1000).fadeOut(300);
    $('#loadertext').delay(1000).fadeOut(300);
});


//botones
Waves.attach('.btn', ['waves-effect']);

//carousel
$('.carousel').carousel({
    touch: true,
    interval: 5000,
    pause: false // default
})


$('.carousel.carousel-multi-item.v-2 .carousel-item').each(function(){
    var next = $(this).next();
    if (!next.length) {
      next = $(this).siblings(':first');
    }
    next.children(':first-child').clone().appendTo($(this));
  
    for (var i=0;i<4;i++) {
      next=next.next();
      if (!next.length) {
        next=$(this).siblings(':first');
      }
      next.children(':first-child').clone().appendTo($(this));
    }
  });