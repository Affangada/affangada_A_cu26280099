<?php require "00-db.php";if(($_SESSION["role"]??"")!=="admin")die("Admin access only.");
if(isset($_POST["status"]))$pdo->prepare("UPDATE orders SET status=? WHERE id=?")->execute([$_POST["status"],$_POST["id"]]);
$orders=$pdo->query("SELECT orders.*,users.name FROM orders JOIN users ON users.id=orders.user_id ORDER BY orders.id DESC")->fetchAll();?>
<h1>Customer Orders</h1><?php foreach($orders as $o):?><p>#<?=$o["id"]?> <?=h($o["name"])?> ₹<?=$o["total"]?> — <?=h($o["status"])?>
<form method="post"><input type="hidden" name="id" value="<?=$o['id']?>">
<select name="status"><option>Pending</option><option>Shipped</option><option>Delivered</option></select>
<button>Update status</button></form></p><?php endforeach;?>