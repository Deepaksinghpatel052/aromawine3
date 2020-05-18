$(document).ready(function(){
  
  $('#stars li').on('mouseover', function(){
    var onStar = parseInt($(this).data('value'), 10); // The star currently mouse on
   
    // Now highlight all the stars that's not after the current hovered star
    $(this).parent().children('li.star').each(function(e){
      if (e < onStar) {
        $(this).addClass('hover');
      }
      else {
        $(this).removeClass('hover');
      }
    });
    
  }).on('mouseout', function(){
    $(this).parent().children('li.star').each(function(e){
      $(this).removeClass('hover');
    });
  });
  
  
  /* 2. Action to perform on click */
  $('#stars li').on('click', function(){
    var onStar = parseInt($(this).data('value'), 10); // The star currently selected
    var stars = $(this).parent().children('li.star');
    
    for (i = 0; i < stars.length; i++) {
      $(stars[i]).removeClass('selected');
    }
    
    for (i = 0; i < onStar; i++) {
      $(stars[i]).addClass('selected');
    }
    
    // JUST RESPONSE (Not needed)
    var ratingValue = parseInt($('#stars li.selected').last().data('value'), 10);
    var msg = "";
    if (ratingValue > 1) {
        msg = "" + ratingValue + " Review.";
    }
    else {
        msg = "" + ratingValue + " Review.";
    }
    responseMessage(msg);
    
  });
  
  
});


function responseMessage(msg) {
  $('.success-box').fadeIn(200);  
  $('.success-box div.text-message').html("<span>" + msg + "</span>");
}








 
  $("#cart").on("click", function() {
	  $(".shopping-cart").slideToggle();
	  
	
	
  });
  


$(".shopping-cart").click(function(e){
    e.stopPropagation();
});

$(document).click(function(){
    $(".shopping-cart").hide();
});


$(document).ready(function(){
  
  $("#addcard_btn").click(function(){
    $(".payment_card").show();
	 $(".nopayd").hide();
	
  });
});	


      var snapSlider = document.getElementById('slider-snap');
      var min = parseInt($("#get_min_price").val());
      var max = parseInt($("#get_max_price").val());
      noUiSlider.create(snapSlider, {
      	start: [ min, max ],
      	snap: false,
      	connect: true,
          step: 1,
      	range: {
      		'min': min,
      		'max': max
      	}
      });
      var snapValues = [
      	document.getElementById('slider-snap-value-lower'),
      	document.getElementById('slider-snap-value-upper')
      ];
      snapSlider.noUiSlider.on('update', function( values, handle ) {
      	snapValues[handle].innerHTML = values[handle];
      });
	  
	  
	  
	  
	  
	  var snapSlider1 = document.getElementById('slider-snap1');
      
      noUiSlider.create(snapSlider1, {
      	start: [ 1, 250 ],
      	snap: false,
      	connect: true,
          step: 1,
      	range: {
      		'min': 0,
      		'max': 500
      	}
      });
      var snapValues1 = [
      	document.getElementById('slider-snap-value-lower1'),
      	document.getElementById('slider-snap-value-upper1')
      ];
      snapSlider1.noUiSlider.on('update', function( values, handle ) {
      	snapValues1[handle].innerHTML = values[handle];

});
	  
   
	
 
  
