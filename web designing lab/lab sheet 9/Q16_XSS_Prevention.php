<?php
$userText = $_POST["comment"] ?? "";
?>
<form method="post"><input name="comment" placeholder="Write a comment"><button>Submit</button></form>
<h3>Comment:</h3>
<p><?= htmlspecialchars($userText, ENT_QUOTES, "UTF-8") ?></p>
