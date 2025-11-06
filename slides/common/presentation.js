// Load Lucide Icons
(function() {
  const script = document.createElement('script');
  script.src = 'https://unpkg.com/lucide@latest';
  script.onload = function() {
    // Initialize icons after script loads
    if (typeof lucide !== 'undefined') {
      lucide.createIcons();
    }
  };
  document.head.appendChild(script);
})();

// Automatically detect total number of slides
function detectTotalSlides() {
  const slideFiles = [];
  let slideNum = 1;
  
  // Try to fetch slides synchronously to count them
  // This creates a temporary XMLHttpRequest to check if slide files exist
  while (true) {
    const xhr = new XMLHttpRequest();
    xhr.open('HEAD', `slide${slideNum}.html`, false);
    try {
      xhr.send();
      if (xhr.status === 200) {
        slideFiles.push(slideNum);
        slideNum++;
      } else {
        break;
      }
    } catch (e) {
      break;
    }
  }
  
  return slideFiles.length > 0 ? slideFiles.length : 10; // Default to 10 if detection fails
}

// Get current slide number from filename (e.g., slide1.html -> 1)
const currentSlide = parseInt(window.location.pathname.match(/slide(\d+)\.html/)[1]);
const totalSlides = detectTotalSlides();

// Presentation mode scaling
function scaleSlide() {
  const slide = document.querySelector('.slide');
  const scale = Math.min(window.innerWidth / 1280, window.innerHeight / 720);
  slide.style.transform = document.body.classList.contains('presentation-mode') 
    ? `scale(${scale})` 
    : 'scale(1)';
}

// Toggle presentation mode
function togglePresentationMode() {
  document.body.classList.toggle('presentation-mode');
  
  // Save state to sessionStorage
  if (document.body.classList.contains('presentation-mode')) {
    sessionStorage.setItem('presentationMode', 'true');
  } else {
    sessionStorage.removeItem('presentationMode');
  }
  
  scaleSlide();
}

// Check if presentation mode was previously enabled
function initPresentationMode() {
  if (sessionStorage.getItem('presentationMode') === 'true') {
    document.body.classList.add('presentation-mode');
  }
  scaleSlide();
}

// Keyboard navigation
document.addEventListener('keydown', function(event) {
  if (event.key === 'ArrowRight' || event.key === 'ArrowDown') {
    // Next slide
    if (currentSlide < totalSlides) {
      window.location.href = `slide${currentSlide + 1}.html`;
    }
  } else if (event.key === 'ArrowLeft' || event.key === 'ArrowUp') {
    // Previous slide
    if (currentSlide > 1) {
      window.location.href = `slide${currentSlide - 1}.html`;
    }
  } else if (event.key === 'f' || event.key === 'F') {
    // Toggle presentation mode
    togglePresentationMode();
  }
});

// Rescale on window resize
window.addEventListener('resize', scaleSlide);

// Initialize presentation mode on page load
initPresentationMode();

// Re-initialize Lucide icons after page navigation
// (in case icons are added dynamically or page is restored from cache)
window.addEventListener('load', function() {
  if (typeof lucide !== 'undefined') {
    lucide.createIcons();
  }
});
