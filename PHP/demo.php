<!DOCTYPE html>
<?php
$str = file_get_contents('http://api.open-notify.org/astros.json');
$str1 = json_decode($str);
$i = 0;
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
		width: 50%;
		text-align: center;
		margin-left: auto;
		margin-right: auto;
	}
		#tblMain thead {
			font-size: 25px;
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
		NASA JSON DATA
	</h1>
</div>
<body>
<h1>
See the astronauts currently in space in table below.
</h1>
<br />
<table id='tblMain'>
<thead>
<tr>
	<th>#</th>
	<th>Name</th>
	<th>Craft</th>
</tr>
</thead>
<tbody>
    <?php
	foreach ($str1->people as $v) {
		echo 
		"<tr> 
		<td>$i</td>
		<td>$v->name</td>
		<td>$v->craft</td>
		</tr>";
		$i += 1;
	}
    ?>
</tbody>
<tfoot>
<tr>
<td></td>
<td>
<label><i>JSON data from: <a href='http://api.open-notify.org/astros.json'>NASA/ISS Open Data</a></i></label>
</td>
<td></td>
</tr>
</tfoot>
</table>
</body>
<hr/>
<footer id="footer">
<br />
<form method="post" action="demo.php">
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
		echo "<script>alert('Hello, ".$_POST["name"]."! We are glad you left a comment. :)')</script>";
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