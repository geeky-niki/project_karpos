// preloader
window.onload = function() {
    const ring = document.querySelector('.ring');
    const loadingText = document.querySelector('.loading-text');
    const preloader = document.querySelector('.center'); // Target the preloader

    // Simulate an estimated preload time (you can adjust this logic for real-time network speed)
    const preloadDuration = 3000; // Default 3 seconds
    const maxDuration = 10000; // Max duration (for slow network speed)
    
    let loadTime = Math.min(preloadDuration, Math.max(maxDuration, window.performance.timing.loadEventEnd - window.performance.timing.navigationStart));

    // Set the animation time for the ring and text loading
    ring.style.animationDuration = `${loadTime / 1000}s`;
    loadingText.style.animationDuration = `${loadTime / 1000}s`;

    // Hide the preloader after everything is loaded (or after the animation completes)
    setTimeout(function() {
        preloader.style.display = 'none';  // Hide the preloader
    }, loadTime); // Ensure it hides after the preloader's animation duration

};

function clearPlaceholder(input) {
    input.dataset.placeholder = input.placeholder; // Save the placeholder
    input.placeholder = ''; // Clear the placeholder
};

function handleBlur(input) {
    if (input.value === '') {
        input.placeholder = input.dataset.placeholder; // Restore the placeholder
    }
};

