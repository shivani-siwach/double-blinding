<html>
<body>
<style>
input[type=text], select {
  width: 100%;
  padding: 12px 20px;
  margin: 8px 0;
  display: inline-block;
  border: 1px solid #ccc;
  border-radius: 4px;
  box-sizing: border-box;
}

input[type=submit] {
  width: 100%;
  background-color: #4CAF50;
  color: white;
  padding: 14px 20px;
  margin: 8px 0;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

input[type=button] {
  width: 25%;
  background-color: #4CAF50;
  color: white;
  padding: 14px 20px;
  margin: 8px 0;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}


input[type=submit]:hover {
  background-color: #45a049;
}

div {
  border-radius: 5px;
  background-color: #f2f2f2;
  padding: 20px;
}
</style>
<h2>Register the Authorised labs</h2>
<div>
    <form action="/lab_names" method = "POST">
          <label for="ln">Enter the Lab name :</label>
          <input type="text"  id="ln" name="ln" required>
          <br>
          <label for="lp">Enter Place of Lab :</label>
          <input type="text" id="lp" name="lp" required>
          <br><br>
          <input type="submit" value="Submit">
          <center>
          <input type="button" value="Back" onclick="window.location.href='http://127.0.0.1:5000/register'"></center>
    </form>
</div>
</body>
</html>
