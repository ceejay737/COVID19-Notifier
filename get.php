<h2>Welcome</h2>
<script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>

<script type="text/javascript" language="javascript">
	var jsondata;

	$(document).ready(function() {
		start_point('110031', '20-05-2021');
	});


	var getCowinJSON = function(url, callback) {
		var xhr = new XMLHttpRequest();
		xhr.open('GET', url, true);
		xhr.responseType = 'json';
		xhr.onload = function() {
			var status = xhr.status;
			if (status === 200) {
				callback(null, xhr.response);
			} else {
				callback(status, xhr.response);
			}
		};
		xhr.send();
	};



	function start_point(pincode, date) {
		getCowinJSON('https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode=' + pincode + '&date=' + date,
			function(err, data) {
				if (err !== null) {
					alert('Oops there are some issues ' + err);
				} else {
					jsondata = data;
					send_data_to_processor(jsondata);
				}
			});
	}


	function send_data_to_processor(jsondata) {
		$.ajax({
			url: "process.php",
			type: "POST",
			data: {
				"availbiltyData": JSON.stringify(jsondata)
			}
		}).done(function(data) {
			console.log(data);
		});

	}
</script>