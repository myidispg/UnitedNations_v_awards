$(document).ready(function() {

	var $toggleButton = $('.toggle-button'),
    	$menuWrap = $('.menu-wrap'),
    	$sidebarArrow = $('.sidebar-menu-arrow');

	// Hamburger button

	$toggleButton.on('click', function() {
		$(this).toggleClass('button-open');
		$menuWrap.toggleClass('menu-show');
	});

	// Sidebar navigation arrows

	$sidebarArrow.click(function() {
		$(this).next().slideToggle(300);
	});


	// animations
	$(".js--wp--1").waypoint(function(direction) {

		if(direction == 'down'){
		  $(".js--wp--1").addClass('animated fadeInLeft');
		}else if(direction == 'up'){
		  $(".js--wp--1").addClass('animated fadeInLeft');
		}
	  },{
		  offset:"80%"
	  }
	);


  $(".js--wp--2").waypoint(function(direction) {

		if(direction == 'down'){
		  $(".js--wp--2").addClass('animated fadeInRight');
		}else if(direction == 'up'){
		  $(".js--wp--2").addClass('animated fadeInRight');
		}
	  },{
		  offset:"50%"
	  }
	);









	// ==================navigation scroll start===================
  // Select all links with hashes
  $('a[href*="#"]')
    // Remove links that don't actually link to anything
    .not('[href="#"]')
    .not('[href="#0"]')
    .click(function(event) {
      // On-page links
      if (
        location.pathname.replace(/^\//, "") ==
          this.pathname.replace(/^\//, "") &&
        location.hostname == this.hostname
      ) {
        // Figure out element to scroll to
        var target = $(this.hash);
        target = target.length
          ? target
          : $("[name=" + this.hash.slice(1) + "]");
        // Does a scroll target exist?
        if (target.length) {
          // Only prevent default if animation is actually gonna happen
          event.preventDefault();
          $("html, body").animate(
            {
              scrollTop: target.offset().top
            },
            800,
            function() {
              // Callback after animation
              // Must change focus!
              var $target = $(target);
              $target.focus();
              if ($target.is(":focus")) {
                // Checking if the target was focused
                return false;
              } else {
                $target.attr("tabindex", "-1"); // Adding tabindex for elements not focusable
                $target.focus(); // Set focus again
              }
            }
          );
        }
      }
    });

  // ==========================navigation scroll start=========================
});


// ======================modal button configuration=======

// get modal
var modal = document.getElementById('simple_modal');
// get modal button
var modalBtn = document.getElementById('modal_btn');
// get close button
var closebtn = document.getElementsByClassName('close_Btn')[0];


// click event to open modal
modalBtn.addEventListener('click',openModal);
//click event to close modal
closebtn.addEventListener('click',closeModal);
// click outside
window.addEventListener('click',click_outside);

// openModal function
function openModal(){
  modal.style.display = 'block';
}

//closeModal function
function closeModal(){
  modal.style.display = 'none';
}

//closeModal function
function click_outside(e){
  if(e.target == modal){
  modal.style.display = 'none';
  }
}


