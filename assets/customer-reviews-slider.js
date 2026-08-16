document.addEventListener('DOMContentLoaded', function() {
  // Initialize the Swiper slider
  initReviewsSlider();

  // Set up button padding and click event
  setupClaimButton();
});

/**
 * Initializes the reviews slider with Swiper.
 * Sliders marked data-autoscroll="false" become a normal swipeable carousel
 * instead of a continuous marquee, which is what video cards need.
 */
function initReviewsSlider() {
  var sliders = document.querySelectorAll('.reviewSwiper');

  sliders.forEach(function (el) {
    var autoScroll = el.dataset.autoscroll !== 'false';

    new Swiper(el, {
      slidesPerView: "auto",
      spaceBetween: 15,
      centeredSlides: false,
      loop: autoScroll,
      speed: autoScroll ? parseInt(el.dataset.speed || 5000) : 400,
      autoplay: autoScroll
        ? {
            delay: 1,
            disableOnInteraction: false
          }
        : false,
      allowTouchMove: true,
      grabCursor: true,
      freeMode: {
        enabled: !autoScroll
      }
    });
  });
}

/**
 * Sets up the claim button padding and event handling
 */
function setupClaimButton() {
  var claimButton = document.querySelector('.claim-button');
  if (claimButton) {
    // Button padding is now handled via inline styles
  }
}

/**
 * Scrolls to the top of the page
 * @param {Event} event - The click event
 */
function scrollToTop(event) {
  // Always prevent default since we're always using '#' as href
  event.preventDefault();

  // Smooth scroll to top
  window.scrollTo({
    top: 0,
    behavior: 'smooth'
  });
}
