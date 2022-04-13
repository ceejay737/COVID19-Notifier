<?php
$data = isset($_REQUEST['availbiltyData']) ? $_REQUEST['availbiltyData'] : "";
print_r($data);
$myDataArray = json_decode($data, true);
search_available_capacity($myDataArray, 'available_capacity');

// function to search by available capacity
function search_available_capacity($json_data_array, $searchkey)
{
	foreach ($json_data_array as $key => $val) {
		if (is_array($val)) {
			search_available_capacity($val, $searchkey);
		} else {
			if ($searchkey == $key) {
				$age_limit = "$json_data_array[min_age_limit]";
				if ($age_limit == 45) {

					$message_to_go = "$json_data_array[name] (District name - $json_data_array[district_name] ) -- Total Availbilty = $val (Age Limit -  $json_data_array[min_age_limit])</br>";
					$subject = "Vaccine Availbilty - Pincode - $json_data_array[pincode] - $json_data_array[name]";
					echo $subject;
					echo $message_to_go;
					send_mail("rishish.xyz@gmail.com", $subject, $message_to_go);
				}
			}
		}
	}
	return;
}

function send_mail($mailid, $subject, $message_to_go)
{

	$to      = $mailid;
	$subject = $subject;
	$message = '<html><body>';
	$message .= $message_to_go;
	$message .= '</body></html>';
	$headers = array(
		'From' => 'admin@rishish.xyz',
		'Reply-To' => 'admin@rishish.xyz',
		'MIME-Version' => '1.0',
		'Content-type' => 'text/html; charset=iso-8859-1'
	);

	mail($to, $subject, $message, $headers);
}