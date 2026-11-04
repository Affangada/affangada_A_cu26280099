<?php $title=$p['name']; require __DIR__.'/layout/header.php'; ?>
<h2><?=e($p['name'])?></h2><p>Price: ₹<?=e($p['price'])?></p>
<?php require __DIR__.'/layout/footer.php'; ?>