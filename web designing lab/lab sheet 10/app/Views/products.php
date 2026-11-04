<?php $title='Products'; require __DIR__.'/layout/header.php'; ?>
<h2>Products</h2><ul><?php foreach($products as $p): ?>
<li><a href="index.php?r=product&id=<?=$p['id']?>"><?=e($p['name'])?></a> — ₹<?=e($p['price'])?></li>
<?php endforeach; ?></ul><?php require __DIR__.'/layout/footer.php'; ?>