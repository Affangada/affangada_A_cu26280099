// Add this file to registration, login and checkout forms.
function validateForm(form) {
  const email = form.querySelector('input[type="email"]');
  const password = form.querySelector('input[type="password"]');
  const address = form.querySelector('textarea[name="address"]');
  if (email && !/^[^\\s@]+@[^\\s@]+\\.[^\\s@]+$/.test(email.value)) {
    alert("Enter a valid email."); return false;
  }
  if (password && password.value.length < 8) {
    alert("Password must contain at least 8 characters."); return false;
  }
  if (address && address.value.trim().length < 8) {
    alert("Enter a complete shipping address."); return false;
  }
  return true;
}