<?php require "00-db.php";
if(empty($_SESSION["user_id"]) || empty($_SESSION["cart"])) die("Login and add books before checkout.");
$msg="";
if($_SERVER["REQUEST_METHOD"]==="POST"){
 try{$pdo->beginTransaction();$total=0;$items=[];
  foreach($_SESSION["cart"] as $id=>$qty){$s=$pdo->prepare("SELECT * FROM books WHERE id=? FOR UPDATE");$s->execute([$id]);$b=$s->fetch();
   if(!$b || $qty>$b["stock"]) throw new Exception("Insufficient stock.");
   $total += $b["price"]*$qty;$items[]=[$b,$qty];}
  $s=$pdo->prepare("INSERT INTO orders(user_id,shipping_address,total) VALUES(?,?,?)");
  $s->execute([$_SESSION["user_id"],trim($_POST["address"]),$total]);$oid=$pdo->lastInsertId();
  foreach($items as [$b,$q]){$pdo->prepare("INSERT INTO order_items(order_id,book_id,quantity,price) VALUES(?,?,?,?)")->execute([$oid,$b["id"],$q,$b["price"]]);
   $pdo->prepare("UPDATE books SET stock=stock-? WHERE id=?")->execute([$q,$b["id"]]);}
  $pdo->commit();$_SESSION["cart"]=[];header("Location: 16-invoice.php?id=$oid");exit;
 }catch(Throwable $e){$pdo->rollBack();$msg="Order not placed: ".$e->getMessage();}
} ?><h1>Checkout</h1><p><?=h($msg)?></p><form method="post">
<textarea name="address" placeholder="Shipping address" required></textarea><button>Place order</button></form>