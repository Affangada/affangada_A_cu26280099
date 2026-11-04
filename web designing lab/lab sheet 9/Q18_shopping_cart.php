<?php
session_start();
if (!isset($_SESSION["cart"])) $_SESSION["cart"]=[];
if ($_SERVER["REQUEST_METHOD"]==="POST") {
    $id=(int)($_POST["id"]??0); $action=$_POST["action"]??"add"; $qty=max(1,(int)($_POST["qty"]??1));
    if($action==="add") $_SESSION["cart"][$id]=($_SESSION["cart"][$id]??0)+$qty;
    if($action==="update") $_SESSION["cart"][$id]=$qty;
    if($action==="remove") unset($_SESSION["cart"][$id]);
}
?>
<form method="post"><input type="number" name="id" placeholder="Product ID" required>
<input type="number" name="qty" value="1" min="1"><button name="action" value="add">Add</button>
<button name="action" value="update">Update</button><button name="action" value="remove">Remove</button></form>
<h3>Cart</h3><?php foreach($_SESSION["cart"] as $id=>$qty) echo "Product ".(int)$id.": ".(int)$qty."<br>"; ?>
