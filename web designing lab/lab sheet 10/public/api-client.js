const API = "api/products.php";
const TOKEN = "PASTE_DEVELOPMENT_TOKEN_HERE"; // do not expose a real secret in public production JS
async function loadProducts() {
  const res = await fetch(API, {headers:{Authorization:`Bearer ${TOKEN}`}});
  const data = await res.json();
  document.querySelector("#result").textContent = JSON.stringify(data, null, 2);
}
async function addProduct(name, price) {
  return fetch(API, {method:"POST", headers:{
    "Content-Type":"application/json", Authorization:`Bearer ${TOKEN}`
  }, body:JSON.stringify({name,price})});
}
