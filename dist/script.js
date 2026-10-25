const root = document.documentElement;
root.classList.add("js");
const savedTheme = localStorage.getItem("portfolio-theme");
if (savedTheme) root.dataset.theme = savedTheme;

document.querySelector(".theme-toggle").addEventListener("click", () => {
  const next = root.dataset.theme === "light" ? "dark" : "light";
  root.dataset.theme = next;
  localStorage.setItem("portfolio-theme", next);
});

document.querySelector("#year").textContent = new Date().getFullYear();

const observer = new IntersectionObserver(
  (entries) => entries.forEach((entry) => {
    if (entry.isIntersecting) {
      entry.target.classList.add("visible");
      observer.unobserve(entry.target);
    }
  }),
  { threshold: 0.12 }
);

document.querySelectorAll(".reveal").forEach((node) => observer.observe(node));

window.addEventListener("pointermove", (event) => {
  root.style.setProperty("--mouse-x", `${event.clientX}px`);
  root.style.setProperty("--mouse-y", `${event.clientY}px`);
});

if (!window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
  document.querySelectorAll(".tilt-card").forEach((card) => {
    card.addEventListener("pointermove", (event) => {
      const rect = card.getBoundingClientRect();
      const x = (event.clientX - rect.left) / rect.width - 0.5;
      const y = (event.clientY - rect.top) / rect.height - 0.5;
      card.style.transform = `perspective(1000px) rotateX(${-y * 4}deg) rotateY(${x * 5}deg) translateY(-2px)`;
    });
    card.addEventListener("pointerleave", () => {
      card.style.transform = "";
    });
  });
}
