<?php
// Example: validate input, escape output and use prepared statements.
require "00-db.php";
$id=filter_input(INPUT_GET,"id",FILTER_VALIDATE_INT);
if(!$id)die("Invalid book ID.");
$stmt=$pdo->prepare("SELECT title,price FROM books WHERE id=:id");
$stmt->execute([":id"=>$id]);$book=$stmt->fetch();
if($book)echo h($book["title"])." — ₹".h($book["price"]);
else echo "Book not found.";
?>