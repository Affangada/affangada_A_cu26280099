<?php require "00-db.php"; $_SESSION["cart"]=$_SESSION["cart"]??[];
if(isset($_GET["add"])){
 $id=(int)$_GET["add"];$s=$pdo->prepare("SELECT stock FROM books WHERE id=?");$s->execute([$id]);$b=$s->fetch();
 if($b && ($_SESSION["cart"][$id]??0)<$b["stock"]) $_SESSION["cart"][$id]=($_SESSION["cart"][$id]??0)+1;
}
if(isset($_GET["remove"])) unset($_SESSION["cart"][(int)$_GET["remove"]]);
if($_SERVER["REQUEST_METHOD"]==="POST") foreach($_POST["qty"] as $id=>$q)
 $_SESSION["cart"][(int)$id]=max(1,min(99,(int)$q));
$total=0; ?><h1>Shopping Cart</h1><form method="post">
<?php foreach($_SESSION["cart"] as $id=>$q):
$s=$pdo->prepare("SELECT * FROM books WHERE id=?");$s->execute([$id]);$b=$s->fetch();if(!$b)continue;
$total+=$b["price"]*$q; ?><p><?=h($b["title"])?> — ₹<?=h($b["price"])?>
<input type="number" name="qty[<?=$id?>]" value="<?=$q?>" min="1" max="<?=$b['stock']?>">
<a href="?remove=<?=$id?>">Remove</a></p><?php endforeach; ?>
<button>Update cart</button></form><p>Total: ₹<?=$total?></p><a href="07-checkout.php">Checkout</a>