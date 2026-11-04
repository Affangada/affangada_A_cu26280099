<?php
require_once "Q02_db.php";
if ($_SERVER["REQUEST_METHOD"] === "POST") {
    $id = (int)($_POST["id"] ?? 0);
    $stmt = $conn->prepare("DELETE FROM products WHERE id=?");
    $stmt->bind_param("i", $id); $stmt->execute();
    echo "Delete request completed.";
}
?>
<form method="post" onsubmit="return confirm('Delete this product?');">
<input type="number" name="id" placeholder="Product ID" required><button>Delete</button></form>
