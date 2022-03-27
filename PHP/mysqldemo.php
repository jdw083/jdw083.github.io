<!DOCTYPE html>
<?php
//echo phpinfo();
$servername = "1.1.1.1";
$username = "hello";
$password = "W0rLd12";
// Create connection
$conn = new mysqli($servername, $username, $password);
$sql = "SELECT * FROM portfolio.tblElectricChargingStationData;";
$result = $conn->query($sql);
$conn->close();
?>
<html5>
<head>
</head>
<style type="text/css">
	body {
		background-color: lightslategray;
		color: ghostwhite;
		text-align: center;
	}
	footer {
		text-align: center;
	}
		footer table {
			margin-left: auto;
			margin-right: auto;
		}
	a {
		text-decoration: underline;
		color: maroon;
	}
	#tblMain {
		width: 100%;
		text-align: center;
		margin-left: auto;
		margin-right: auto;
		background-color: gainsboro;
		color: black;
	}
		#tblMain thead {
			font-size: 20px;
		}
		#tblMain td {
			border: 1px solid black;
		}
		#tblMain tr:nth-child(even) {
			background-color: #f2f2f2;
			border: 1px solid black;
		}
	#banner {
		text-align: center;
		background-color: maroon;
		border-radius: 10px;
		color: ghostwhite;
	}
	#commentBox {
		height: 100px;
	}
</style>
<div id="banner">
	<h1>
		Google Cloud MySQL Data
	</h1>
</div>
<body>
<h1>
Colorado Electric Charging Station Data
</h1>
<h3>
This is a sample of data pulled from <a href='https://hub.arcgis.com/datasets/183adc24880b41c4be9fd6a14eb6165f_0/explore'>ArcGIS Hub</a> displaying a data pull from <a href='https://cloud.google.com/'>Google Cloud Services</a> using MySQL, PHP and HTML/CSS.
</h3>
<br />
<table id='tblMain' cellspacing=0>
<thead>
<tr>
	<th>#</th>
	<th>Station Name</th>
	<th>Address</th>
	<th>City</th>
	<th>State Province</th>
	<th>Zip/Postal Code</th>
	<th>Start Time</th>
	<th>Start Timezone</th>
	<th>End Time</th>
	<th>End Timezone</th>
	<th>Total Duration</th>
	<th>Charge Time</th>
	<th>Energy in kW/h</th>
	<th>GHG Savings (kg)</th>
	<th>Gasoline Savings (gal)</th>
	<th>Port Type</th>
</tr>
</thead>
<tbody>
    <?php
	if ($result->num_rows > 0) {
	  // output data of each row
	  while($row = $result->fetch_assoc()) {
		echo 
		"<tr> 
		<td>".$row["ObjectId"]."</td>
		<td>".$row["Station_Name"]."</td>
		<td>".$row["Address"]."</td>
		<td>".$row["City"]."</td>
		<td>".$row["State_Province"]."</td>
		<td>".$row["Zip_Postal_Code"]."</td>
		<td>".$row["Start_Date___Time"]."</td>
		<td>".$row["Start_Time_Zone"]."</td>
		<td>".$row["End_Date___Time"]."</td>
		<td>".$row["End_Time_Zone"]."</td>
		<td>".$row["Total_Duration__hh_mm_ss_"]."</td>
		<td>".$row["Charging_Time__hh_mm_ss_"]."</td>
		<td>".$row["Energy__kWh_"]."</td>
		<td>".$row["GHG_Savings__kg_"]."</td>
		<td>".$row["Gasoline_Savings__gallons_"]."</td>
		<td>".$row["Port_Type"]."</td>
		</tr>";
	  }
	} else {
		trigger_error('Invalid query: ' . $conn->error);
		echo "<h1>No results.</h1>";
	}
    ?>
</tbody>
<tfoot>
<tr>
<td></td>
<td>
<label><i>Data originating from:<br/> <a href='https://hub.arcgis.com/datasets/183adc24880b41c4be9fd6a14eb6165f_0/explore'>Electric Vehicle Charging<br/> Station Energy Consumption</a></i></label>
</td>
</tr>
</tfoot>
</table>
</body>
<hr/>
<footer id="footer">
<br />
<form method="post" action="#">
<h1>Leave a comment below:</h1>
<br />
<table>
<tr>
<td><label>Name:</label></td>
<td><input name="name" type="text"/></td>
</tr>
<tr>
<td><label>Phone (optional):</label></td>
<td><input name="phone" type="text"/></td>
</tr>
<tr>
<td><label>Email (optional):</label></td>
<td><input name="email" type="text"/></td>
</tr>
<tr>
<td><label>Comment (optional):</label></td>
<td><textarea id="commentBox" name="comment" type="text"></textarea></td>
</tr>
</table>
<input type="submit" value="Submit" name="submit"/>
</form>
</footer>
</html5>
<?php
	function display()
	{
		/*$to = "jwindham94@gmail.com";
		$subject = "New email from " . $_POST["name"] . " on portfolio page.";
		$message = "Name: " . $_POST["name"] . "<br/>".
					"Phone: " . $_POST["phone"] . "<br/>".
					"Email: " . $_POST["email"] . "<br/>".
					"Comment: " . $_POST["comment"] . "";
		$headers = "MIME-Version: 1.0" . "\r\n";
		$headers .= "Content-type:text/html;charset=UTF-8" . "\r\n";
		$headers .= 'From: <webmaster@jdw083.github.io>' . "\r\n";*/

		echo "<script>alert('Hello, ".$_POST["name"]."! We are glad you left a comment. :)')</script>";
		//mail($to,$subject,$message,$headers);
	} 
	if(isset($_POST['submit']))
	{
		if($_POST["name"]){
			display();
		} else {
			echo "<script>alert('Hello! Please enter at least your name before leaving a comment. Thanks! :)')</script>";
		}
	}
?>