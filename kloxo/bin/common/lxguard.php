<?php 

$clearflag = false;

if ($argv) {
	$since = $argv[1];
} else {
	$since = false;
}

include_once "htmllib/lib/include.php"; 
include_once "htmllib/lib/lxguardincludelib.php";

debug_for_backend();
lxguard_main($clearflag, $since);

