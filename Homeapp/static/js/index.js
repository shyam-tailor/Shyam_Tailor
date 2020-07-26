// console.log('working');
// if(localStorage.getItem('cart') == null){
// var cart = {};
// }
// else
// {
// cart = JSON.parse(localStorage.getItem('cart'));
// }
// $('.cart').click(function(){
// console.log('clicked');
// var idstr = this.id.toString();
// console.log(idstr);
// if (cart[idstr] !=undefined){
// cart[idstr] = cart[idstr] + 1;
// }
// else
// {
// cart[idstr] = 1;
// }
// console.log(cart);
// localStorage.setItem('cart', JSON.stringify(cart));
// });







function openNav() {

  console.log("HEllo baba")
  document.getElementById("side").style.display = "block";
  // document.getElementById("sidebody").style.width = "10px";
}

function closeNav() {
  document.getElementById("side").style.display = "none";
}

// function cartfun(id)
// {
//   console.log("I Am Clicked")
//   // var idstr="Heeloo"
//   var idstr=id.toString();
//   console.log(idstr);
//   // console.log(cart[idstr])
//   if(cart != undefined)
//   {
//     cart[idstr]=cart[idstr]+1;
//     console.log("cart not empty")
//   }
//   else
//   {
//     cart[idstr]=1;
//     // console.log("cart empty")
//   }
//   console.log(cart);
  // localStorage.setItem('cart', JSON.stringify(cart));


// }










function check()
{

$grid= $('.grid')


    


if($grid.length)
{
$grid.isotope({
itemSelector: '.product',
layoutMode: 'fitRows',
getSortData: {
// name: '.name',
// symbol: '.symbol',
// number: '.number parseInt',
category: '[data-category]',
weight: function( itemElem ) {
  var weight = $( itemElem ).find('.weight').text();
  return parseFloat( weight.replace( /[\(\)]/g, '') );
}
}
});


   
   
var filterFns = {
// show if number is greater than 50
numberGreaterThan50: function() {
var number = $(this).find('.number').text();
return parseInt( number, 10 ) > 50;
},
// show if name ends with -ium
ium: function() {
var name = $(this).find('.name').text();
return name.match( /ium$/ );
}
};

// bind filter button click
$('#filters').on( 'click', 'button', function() {
var filterValue = $( this ).attr('data-filter');
// use filterFn if matches value
filterValue = filterFns[ filterValue ] || filterValue;
$grid.isotope({ filter: filterValue });
});
}
// bind sort button click
$('#sorts').on( 'click', 'button', function() {
var sortByValue = $(this).attr('data-sort-by');
$grid.isotope({ sortBy: sortByValue });
});



$('.button-group').each( function( i, buttonGroup ) {
  var $buttonGroup = $( buttonGroup );
  $buttonGroup.on( 'click', 'button', function() {
    $buttonGroup.find('.is-checked').removeClass('is-checked');
    $( this ).addClass('is-checked');
  });
});
}



// change is-checked class on buttons


     
   
   

// $('#owl-demo-2').owlCarousel({
// autoplay: true,
// lazyLoad: true,
// loop: true,
// margin: 20,
// /*
// animateOut: 'fadeOut',
// animateIn: 'fadeIn',
// */
// responsiveClass: true,
// autoHeight: true,
// autoplayTimeout: 7000,
// smartSpeed: 800,
// // nav: true,
// })

// $('#owl-demo').owlCarousel({
//   loop:true,
// animateOut: 'fadeOut',
// items:1,
//   responsiveClass:true,
//   autoplay:true,
// dots:true,
// nav:true,
// autoplaySpeed:15000,
// })
