<?php require "00-db.php";$q=trim($_GET["q"]??"");$s=$pdo->prepare("SELECT * FROM books WHERE title LIKE ? OR author LIKE ? OR category LIKE ?");
$s->execute(["%$q%","%$q%","%$q%"]);?><h1>Search Results</h1>
<?php foreach($s as $b):?><p><a href="04-book-detail.php?id=<?=$b['id']?>"><?=h($b["title"])?></a> — <?=h($b["author"])?></p><?php endforeach;?>