<?php
// Install: composer require phpmailer/phpmailer
require dirname(__DIR__).'/vendor/autoload.php';
use PHPMailer\PHPMailer\PHPMailer;
$mail=new PHPMailer(true);
try {
 $mail->isSMTP();$mail->Host=getenv('SMTP_HOST');$mail->SMTPAuth=true;
 $mail->Username=getenv('SMTP_USER');$mail->Password=getenv('SMTP_PASS');
 $mail->SMTPSecure=PHPMailer::ENCRYPTION_STARTTLS;$mail->Port=587;
 $mail->setFrom(getenv('SMTP_USER'),'Lab 10 App');
 $mail->addAddress('student@example.com'); // replace with verified recipient
 $mail->Subject='Registration confirmation';$mail->Body='Your registration is confirmed.';
 $mail->send();echo 'Email sent.';
} catch(Throwable $e) { error_log($e->getMessage());echo 'Email could not be sent.'; }
?>