document.addEventListener('DOMContentLoaded', function () {
  const animEls = document.querySelectorAll('.anim');

  if ('IntersectionObserver' in window) {
    const io = new IntersectionObserver((entries, observer) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('in-view');
          // if you want animations only once, unobserve:
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.18 });

    animEls.forEach(el => io.observe(el));
  } else {
    // fallback: simply add in-view after short delay
    animEls.forEach(el => setTimeout(()=> el.classList.add('in-view'), 120));
  }
});
