<?php
    // Check if file got posted
    if(isset($_FILES['harFile'])){
        $errors= array();
        $file_name = $_FILES['harFile']['name'];
        $file_size = $_FILES['harFile']['size'];
        $file_tmp = $_FILES['harFile']['tmp_name'];
        $file_type = $_FILES['harFile']['type'];
        $file_ext=strtolower(end(explode('.',$_FILES['harFile']['name'])));
        
        $extensions= array("har");
        
        // Check if posted file is an .har file
        if(in_array($file_ext,$extensions)=== false){
            $errors[]="extension not allowed, please choose a har file.";
        }
        
        // Check if posted file is smaller than 50 Mb [Not final]
        if($file_size > 52428800) {
            $errors[]='File size must be smaller than 50 MB';
        }
        
        // If no errors occured: Parse har file with harParser.py and parse the output json file
        if(empty($errors)==true) {
            mkdir("../Storage/".$_POST['uploadOwnerName']."_".$_POST['uploadSessionName']."/");
            move_uploaded_file($file_tmp,"../Storage/".$_POST['uploadOwnerName']."_".$_POST['uploadSessionName']."/tmpHarFile.har");
            
            $path = "./Storage/".$_POST['uploadOwnerName']."_".$_POST['uploadSessionName']."/";
            $python = exec("python ../Python/harParser.py .$path");

            parsePythonOutput();

        }else{
            print_r($errors);
        }
    }

    // Navigate back to index.php
    // NOTE: Doesn't work if this file echoes
    // header("Location: ../index.php");
    // exit;



    // Parse the json output file that harParser.py generates
    // TODO Extract all data from the output file
    // TODO Establish DB connection
    // TODO Enter data into DB
    // TODO Save specific 
    function parsePythonOutput()
    {
        // Load content of Result.json files
        $pythonOutput = file_get_contents("../Storage/".$_POST['uploadOwnerName']."_".$_POST['uploadSessionName']."/Result.json");
        
        // Decode json to array
        $array = json_decode($pythonOutput, true);

        // Check if array contains #remote_avatar Key
        if($array['#remote_avatar']!= NULL)
        {
            // Print for testing purposes only
            // var_dump($array['#remote_avatar'][0]);


            // Iterate over every element in #remote_avatar
            foreach ($array['#remote_avatar'] as $value) {

                // Store sessionId
                $sessionId = $value['sessionId'];


                // Store data
                $data = $value['data'];

                // Iterate over every element of data
                foreach ($data as $dataElement)
                {
                    // Store time
                    $time = $dataElement['time'];


                    // Store components
                    $components = $dataElement['components'];
                    // Print for testing
                    echo nl2br("SessionId: ".$sessionId."\nTime: ".$time);

                    // Iterate over every element of components
                    foreach ($components as $componentsElement)
                    {
                        $componentName = $componentsElement['componentName'];
                        $x = $componentsElement['x'];
                        $y = $componentsElement['y'];
                        $z = $componentsElement['z'];

                        // Print for testing
                        echo nl2br("\ncomponentName: " .$componentName. "\nx: " .$x. "\ny: " .$y. "\nz: " .$z);
                    }
                }

            }       
            
        }
        
    }

?>