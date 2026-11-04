// Navigation, featured carousel and booking form validation.
const menuToggle = document.querySelector("#menuToggle");
const navLinks = document.querySelector("#navLinks");
menuToggle.addEventListener("click", () => {
  const expanded = menuToggle.getAttribute("aria-expanded") === "true";
  menuToggle.setAttribute("aria-expanded", String(!expanded));
  navLinks.classList.toggle("open");
});

const slides = [
  { image: "https://images.unsplash.com/photo-1495474472287-4d71bcdd2085?w=1400", alt: "Freshly brewed coffee on a cafe table" },
  { image: "https://images.unsplash.com/photo-1512621776951-a57141f2eefd?w=1400", alt: "Fresh seasonal vegetable bowl" },
  { image: "https://images.unsplash.com/photo-1509440159596-0249088772ff?w=1400", alt: "Fresh artisan bread" }
];
let currentSlide = 0;
const heroImage = document.querySelector("#heroImage");
const slideCount = document.querySelector("#slideCount");
function showSlide(index) {
  currentSlide = (index + slides.length) % slides.length;
  heroImage.style.backgroundImage = `url("${slides[currentSlide].image}")`;
  heroImage.setAttribute("aria-label", slides[currentSlide].alt);
  slideCount.textContent = `0${currentSlide + 1} / 0${slides.length}`;
}
document.querySelector("#prevSlide").addEventListener("click", () => showSlide(currentSlide - 1));
document.querySelector("#nextSlide").addEventListener("click", () => showSlide(currentSlide + 1));

const dateInput = document.querySelector("#bookingDate");
dateInput.min = new Date().toISOString().split("T")[0];
document.querySelector("#bookingForm").addEventListener("submit", (event) => {
  event.preventDefault();
  const form = event.currentTarget;
  const message = document.querySelector("#formMessage");
  if (!form.checkValidity()) {
    form.reportValidity();
    message.textContent = "Please complete all required fields with valid details.";
    return;
  }
  const name = document.querySelector("#guestName").value.trim();
  message.textContent = `Thank you, ${name}! Your booking request is ready. This demo does not send a live reservation.`;
  form.reset();
  dateInput.min = new Date().toISOString().split("T")[0];
});
