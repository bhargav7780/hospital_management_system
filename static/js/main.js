document.addEventListener('DOMContentLoaded', () => {
  const toggle = document.getElementById('darkToggle');
  const body = document.body;
  const theme = localStorage.getItem('hms_theme');
  if (theme === 'dark') body.classList.add('dark');
  updateToggle();

  toggle && toggle.addEventListener('click', () => {
    body.classList.toggle('dark');
    localStorage.setItem('hms_theme', body.classList.contains('dark') ? 'dark' : 'light');
    updateToggle();
  });

  const cards = document.querySelectorAll('[data-anim]');
  cards.forEach((c,i)=> c.style.animationDelay = `${i*80}ms`);

  function updateToggle(){
    if(!toggle) return;
    toggle.textContent = body.classList.contains('dark') ? 'Light' : 'Dark';
  }
});
