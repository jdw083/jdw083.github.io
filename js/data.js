var mysql = require('mysql');
const fs = require('fs');

var con = mysql.createConnection({
    host: "localhost",
    user: "root",
    password: "",
    database: "test"
});

con.connect(function (err) {
    if (err) throw err;
    console.log("Connected!");


    //con.query("CREATE DATABASE web_db", function (err, result) {
    //    if (err) throw err;
    //    console.log("Database created");
    //});

    //var sql = "CREATE TABLE `tblvisitors` (`datetime` datetime(6) DEFAULT current_timestamp(6),`firstname` text NOT NULL,`lastname` text NOT NULL,`phone` varchar(10) NOT NULL,`comment` text NOT NULL);";
    //con.query(sql, function (err, result) {
    //    if (err) throw err;
    //    console.log("Table created");
    //});

    //var sql = "INSERT INTO tblvisitors (datetime, firstname, lastname, phone, comment) VALUES ('now()', 'James', 'Windham', '3187583880', 'Hello there bro!')";
    //con.query(sql, function (err, result) {
    //    if (err) throw err;
    //    console.log("1 record inserted");
    //});

    var sql = "select * from tblvisitors;"
    con.query(sql, function (err, result, fields) {
        if (err) throw err;
        result = JSON.stringify(result);
        fs.writeFileSync('data.json', result);
    });
});