// document.addEventListener('DOMContentLoaded', function() {
//     const images = ['https://thumbs.dreamstime.com/b/suburban-home-exterior-stone-porch-neighborhood-north-carolina-multi-story-gray-white-house-built-picture-taken-141500306.jpg', 'https://images.pexels.com/photos/106399/pexels-photo-106399.jpeg', 'https://media.istockphoto.com/id/1436217023/photo/exterior-of-a-blue-suburban-home.webp?b=1&s=612x612&w=0&k=20&c=9bA_E6bi430LQiIg7wahxg5aNph5mIzD8SB0oiEtvMs=']; // Add URLs of all images
//     let currentImageIndex = 0;

//     const imageContainer = document.querySelector('.tryimage img');

//     document.querySelector('.arrow-left').addEventListener('click', function() {
//         currentImageIndex = (currentImageIndex - 1 + images.length) % images.length;
//         imageContainer.src = images[currentImageIndex];
//     });

//     document.querySelector('.arrow-right').addEventListener('click', function() {
//         currentImageIndex = (currentImageIndex + 1) % images.length;
//         imageContainer.src = images[currentImageIndex];
//     });
// });


// For navigation bar

(function($) { // Begin jQuery
    $(function() { // DOM ready
      // If a link has a dropdown, add sub menu toggle.
      $('nav ul li a:not(:only-child)').click(function(e) {
        $(this).siblings('.nav-dropdown').toggle();
        // Close one dropdown when selecting another
        $('.nav-dropdown').not($(this).siblings()).hide();
        e.stopPropagation();
      });
      // Clicking away from dropdown will remove the dropdown class
      $('html').click(function() {
        $('.nav-dropdown').hide();
      });
      // Toggle open and close nav styles on click
      $('#nav-toggle').click(function() {
        $('nav ul').slideToggle();
      });
      // Hamburger to X toggle
      $('#nav-toggle').on('click', function() {
        this.classList.toggle('active');
      });
    }); // end DOM ready
  })(jQuery); // end jQuery
