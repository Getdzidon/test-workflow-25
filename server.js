const express = require("express");
const mysql = require("mysql");
const bodyParser = require("body-parser");
const { exec } = require("child_process");
const path = require("path");

const app = express();
app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static("public")); // ✅ Serve frontend files

// 🚨 CRITICAL VULNERABILITIES EXIST HERE
const API_KEY = "sk-CRITICAL-EXPOSED-123456";

const db = mysql.createConnection({
    host: "localhost",
    user: "root",
    password: "rootpassword",
    database: "users_db"
});
db.connect();

app.get("/user", (req, res) => {
    let username = req.query.username;
    let query = `SELECT * FROM users WHERE username = '${username}'`;
    db.query(query, (err, result) => {
        if (err) throw err;
        res.send(result);
    });
});

app.post("/execute", (req, res) => {
    let userInput = req.body.code;
    let result = eval(userInput); // 🚨 RCE vulnerability
    res.send(`Result: ${result}`);
});

app.post("/cmd", (req, res) => {
    let command = req.body.command;
    exec(command, (err, stdout) => {
        if (err) {
            res.send("Error executing command");
            return;
        }
        res.send(stdout);
    });
});

app.get("/", (req, res) => {
    res.sendFile(path.join(__dirname, "public", "index.html")); // ✅ Serve your HTML file
});

app.listen(3000, () => console.log("🚨 Vulnerable App Running on http://localhost:3000"));
