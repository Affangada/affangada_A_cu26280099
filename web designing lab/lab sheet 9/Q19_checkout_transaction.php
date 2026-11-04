<?php
session_start(); require_once "Q02_db.php";
$userId = (int)($_SESSION["user_id"] ?? 0);
if (!$userId || empty($_SESSION["cart"])) die("Login and add products first.");
$conn->begin_transaction();
try {
    $total=0;
    $find=$conn->prepare("SELECT price FROM products WHERE id=?");
    foreach($_SESSION["cart"] as $id=>$qty) {
        $id=(int)$id; $qty=(int)$qty; $find->bind_param("i",$id); $find->execute();
        $p=$find->get_result()->fetch_assoc();
        if(!$p) throw new Exception("Product not found.");
        $total += (float)$p["price"]*$qty;
    }
    $stmt=$conn->prepare("INSERT INTO orders(user_id,total) VALUES(?,?)");
    $stmt->bind_param("id",$userId,$total); $stmt->execute();
    $conn->commit(); unset($_SESSION["cart"]); echo "Order placed. Total: ₹".number_format($total,2);
} catch(Throwable $e) { $conn->rollback(); echo "Checkout failed: ".htmlspecialchars($e->getMessage()); }
?>
