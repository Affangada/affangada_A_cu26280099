<?php require "00-db.php";$limit=5;$page=max(1,(int)($_GET["page"]??1));$offset=($page-1)*$limit;
$total=(int)$pdo->query("SELECT COUNT(*) FROM books")->fetchColumn();
$s=$pdo->prepare("SELECT * FROM books LIMIT ? OFFSET ?");$s->bindValue(1,$limit,PDO::PARAM_INT);$s->bindValue(2,$offset,PDO::PARAM_INT);$s->execute();
foreach($s as $b)echo "<p>".h($b["title"])."</p>";
for($i=1;$i<=ceil($total/$limit);$i++)echo '<a href="?page='.$i.'">'.$i.'</a> '; ?>