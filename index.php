<?php
ini_set('display_errors', 1);
ini_set('display_startup_errors', 1);
error_reporting(E_ALL);

// Disabled foreign 0
#SET GLOBAL FOREIGN_KEY_CHECKS=1;


$filename = 'dev-entrekids.sql';
$mysql_host = 'localhost';
$mysql_username = 'root';
$mysql_password = '';
$mysql_database = 'entrekids-dev';

$mysqli = new mysqli($mysql_host, $mysql_username, $mysql_password, $mysql_database);



$templine = '';
$lines = file($filename);
foreach ($lines as $line)
{

if (substr($line, 0, 2) == '--' || $line == '')
    continue;


$templine .= $line;

if (substr(trim($line), -1, 1) == ';')
{

    $mysqli->query($templine);
    $templine = '';
}
}
 echo "Tables imported successfully";
?>