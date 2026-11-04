<?php
$notice = "";
if ($_SERVER["REQUEST_METHOD"] === "POST" && isset($_FILES["photo"])) {
    $file = $_FILES["photo"]; $allowed = ["image/jpeg"=>"jpg","image/png"=>"png","image/webp"=>"webp"];
    $mime = mime_content_type($file["tmp_name"]);
    if ($file["error"] !== UPLOAD_ERR_OK || $file["size"] > 2*1024*1024 || !isset($allowed[$mime])) {
        $notice = "Upload JPG, PNG or WEBP up to 2 MB.";
    } else {
        if (!is_dir("uploads")) mkdir("uploads",0755,true);
        $filename = bin2hex(random_bytes(12)).".".$allowed[$mime];
        $notice = move_uploaded_file($file["tmp_name"],"uploads/".$filename) ? "Uploaded: ".$filename : "Upload failed.";
    }
}
?>
<form method="post" enctype="multipart/form-data"><input type="file" name="photo" accept="image/*" required><button>Upload</button></form>
<p><?= htmlspecialchars($notice) ?></p>
