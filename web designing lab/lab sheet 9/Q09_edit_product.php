<?php
require_once "Q02_db.php";
$id = (int)($_GET["id"] ?? 0);
if ($_SERVER["REQUEST_METHOD"] === "POST") {
    $name = trim($_POST["name"]); $price = (float)$_POST["price"];
    $stmt = $conn->prepare("UPDATE products SET name=?,price=? WHERE id=?");
    $stmt->bind_param("sdi", $name, $price, $id); $stmt->execute();
}
$stmt = $conn->prepare("SELECT name,price FROM products WHERE id=?");
$stmt->bind_param("i", $id); $stmt->execute(); $product = $stmt->get_result()->fetch_assoc();
?>
<?php if($product): ?><form method="post">
<input name="name" value="<?= htmlspecialchars($product["name"]) ?>" required>
<input name="price" type="number" step="0.01" value="<?= htmlspecialchars((string)$product["price"]) ?>" required>
<button>Update</button></form><?php else: ?>Product not found.<?php endif; ?>
