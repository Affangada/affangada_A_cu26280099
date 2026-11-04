<?php require "00-db.php"; if(($_SESSION["role"]??"")!=="admin")die("Admin access only.");
if($_SERVER["REQUEST_METHOD"]==="POST"){
 if(isset($_POST["add"]))$pdo->prepare("INSERT INTO books(title,author,category,price,stock) VALUES(?,?,?,?,?)")->execute([$_POST["title"],$_POST["author"],$_POST["category"],$_POST["price"],$_POST["stock"]]);
 if(isset($_POST["update"]))$pdo->prepare("UPDATE books SET price=?,stock=? WHERE id=?")->execute([$_POST["price"],$_POST["stock"],$_POST["id"]]);
}
?><h1>Admin Dashboard</h1><form method="post"><h3>Add book</h3>
<input name="title" placeholder="Title" required><input name="author" placeholder="Author">
<input name="category" placeholder="Category"><input name="price" type="number" step=".01" required>
<input name="stock" type="number" required><button name="add">Add book</button></form>
<form method="post"><h3>Update price / stock</h3><input name="id" type="number" placeholder="Book ID" required>
<input name="price" type="number" step=".01" required><input name="stock" type="number" required>
<button name="update">Update</button></form>