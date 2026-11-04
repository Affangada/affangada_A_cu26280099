<?php require "00-db.php";
$books = $pdo->query("SELECT * FROM books WHERE stock > 0 ORDER BY id DESC")->fetchAll(); ?>
<link rel="stylesheet" href="19-style.css"><h1>Available Books</h1><div class="grid">
<?php foreach($books as $b): ?><div class="card">
<h3><?=h($b['title'])?></h3><p>By <?=h($b['author'])?></p>
<p>₹<?=h($b['price'])?></p><a href="04-book-detail.php?id=<?=$b['id']?>">View details</a>
</div><?php endforeach; ?></div>