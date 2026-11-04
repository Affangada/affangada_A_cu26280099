<?php
require_once "Q02_db.php";
$q = "%".($_GET["q"] ?? "")."%";
$stmt = $conn->prepare("SELECT name,price FROM products WHERE name LIKE ? LIMIT 10");
$stmt->bind_param("s",$q); $stmt->execute(); $rows=$stmt->get_result();
while($r=$rows->fetch_assoc()) {
    echo "<p>".htmlspecialchars($r["name"],ENT_QUOTES,"UTF-8")." - ₹".htmlspecialchars((string)$r["price"])."</p>";
}
?>
