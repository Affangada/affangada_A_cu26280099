<?php
require_once "Q02_db.php";
$name = "Keyboard"; $category = "Electronics"; $price = 799.00;
$stmt = $conn->prepare("INSERT INTO products(name,category,price) VALUES(?,?,?)");
$stmt->bind_param("ssd", $name, $category, $price);
echo $stmt->execute() ? "Product inserted." : "Insert failed.";
$stmt->close();
?>
