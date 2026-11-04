<?php
require dirname(__DIR__).'/config/config.php';
$msg='';
if($_SERVER['REQUEST_METHOD']==='POST' && isset($_FILES['file'])){
 $f=$_FILES['file'];$allowed=['image/jpeg'=>'jpg','image/png'=>'png','application/pdf'=>'pdf'];
 $mime=(new finfo(FILEINFO_MIME_TYPE))->file($f['tmp_name']);
 if($f['error']!==UPLOAD_ERR_OK || $f['size']>2*1024*1024) $msg='Upload error or file exceeds 2 MB.';
 elseif(!isset($allowed[$mime])) $msg='Only JPG, PNG and PDF files allowed.';
 else {$name=bin2hex(random_bytes(16)).'.'.$allowed[$mime];
  if(move_uploaded_file($f['tmp_name'],UPLOAD_DIR.$name))$msg='Uploaded safely: '.$name;else $msg='Upload failed.';}
} ?>
<h2>Secure File Upload</h2><p><?=e($msg)?></p>
<form method="post" enctype="multipart/form-data"><input type="file" name="file" required><button>Upload</button></form>