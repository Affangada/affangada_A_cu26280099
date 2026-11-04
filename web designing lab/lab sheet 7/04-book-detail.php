<?php require "00-db.php";
$id = filter_input(INPUT_GET, "id", FILTER_VALIDATE_INT);
$stmt = $pdo->prepare("SELECT * FROM books WHERE id=?"); $stmt->execute([$id ?: 0]);
$b = $stmt->fetch(); if(!$b) die("Book not found."); ?>
<h1><?=h($b['title'])?></h1><p>Author: <?=h($b['author'])?></p>
<p>Category: <?=h($b['category'])?></p><p>Price: ₹<?=h($b['price'])?></p>
<p>Stock: <?=h($b['stock'])?></p><a href="06-cart.php?add=<?=$b['id']?>">Add to cart</a>
<form action="15-reviews.php" method="post"><input type="hidden" name="book_id" value="<?=$b['id']?>">
<input type="number" name="rating" min="1" max="5" required><input name="comment" placeholder="Your review">
<button>Review</button></form>