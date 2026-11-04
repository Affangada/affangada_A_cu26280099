<?php
require dirname(__DIR__,2).'/config/config.php';
require dirname(__DIR__,2).'/app/Core/Database.php';
header('Content-Type: application/json');
function reply($data,int $code=200){http_response_code($code);echo json_encode($data);exit;}
$auth=$_SERVER['HTTP_AUTHORIZATION'] ?? '';
if (!preg_match('/Bearer\s+(.+)/i',$auth,$m)) reply(['error'=>'Unauthorized'],401);
$hash=hash('sha256',trim($m[1]));
$s=Database::get()->prepare("SELECT id FROM api_tokens WHERE token_hash=?");
$s->execute([$hash]); if(!$s->fetch()) reply(['error'=>'Invalid token'],401);
$db=Database::get(); $method=$_SERVER['REQUEST_METHOD'];
if($method==='GET'){
 $id=(int)($_GET['id']??0);
 if($id){$s=$db->prepare("SELECT * FROM products WHERE id=?");$s->execute([$id]);$p=$s->fetch();reply($p ?: ['error'=>'Not found'],$p?200:404);}
 reply($db->query("SELECT * FROM products")->fetchAll());
}
$body=json_decode(file_get_contents('php://input'),true) ?? [];
if($method==='POST'){
 $s=$db->prepare("INSERT INTO products(name,price) VALUES(?,?)");
 $s->execute([trim($body['name']??''),(float)($body['price']??0)]);
 reply(['id'=>$db->lastInsertId(),'created'=>true],201);
}
if($method==='PUT'){
 $s=$db->prepare("UPDATE products SET name=?,price=? WHERE id=?");
 $s->execute([trim($body['name']??''),(float)($body['price']??0),(int)($body['id']??0)]);
 reply(['updated'=>$s->rowCount()]);
}
if($method==='DELETE'){
 $s=$db->prepare("DELETE FROM products WHERE id=?");$s->execute([(int)($body['id']??0)]);
 reply(['deleted'=>$s->rowCount()]);
}
header('Allow: GET, POST, PUT, DELETE');reply(['error'=>'Method not allowed'],405);
?>