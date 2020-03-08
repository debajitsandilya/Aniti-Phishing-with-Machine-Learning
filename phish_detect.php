<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Phishing detection and prevention</title>
<style> 
            pre { 
                font-family: Arial; 
                border: 1px solid #777;
                margin: 25px; 
            }  
</style> 
</head>
<body>
<div style="text-align:center;">
<form action "phish_detect.php" method = "POST">

<input type = "text" name = "url"  
placeholder = "Enter URL" />

<input type = "text" name ="good" size = "40"
placeholder="good email text here" /> 


<input type = "text" name = "bad" size = "40"
placeholder="Enter bad email text here" />

<input type = "submit" value ="Submit"/>

</form>
</div>
</body>

</html>


<?php

$txt_file = "C:/xampp/htdocs/cyber_project/logs_cosine_sim.txt";
#check if URL isset
if(isset($_POST['url'])) {
    $url = $_POST['url'];
    #capture good and bad from text input
    $good = $_POST['good'];
    $bad = $_POST['bad'];

    #storing urls to csv
    $fileName =  "Sample_urls.csv";
    $header = "URL\n";
    if (file_exists($fileName)){
      file_put_contents($fileName, $url,LOCK_EX); 
    }
    else{
      file_put_contents($fileName,$header . $url);
    }
    #execute python file test.py from php file
    $op = shell_exec("python test.py . $url $good $bad");
    echo $op;
    
}

?>


