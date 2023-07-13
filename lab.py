import re
import turtle
from flask import Flask,flash, request,redirect, render_template,url_for
from importlib_metadata import method_cache
from sqlalchemy import false, true

app = Flask(__name__)  
app.secret_key = 'aieoifjhaejsdfeeksd'

@app.route('/', methods =["GET", "POST"])
def check_password():
    return render_template("index.html")

@app.route("/results",methods = ["GET","POST"])
def validator():
    user_n = request.form.get("user_n")
    user_p = str(request.form.get("user_p"))
    regular_pass = "^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9]).{8,}$"
    return_pass = re.search(regular_pass,user_p)
    init_case = false
    fail_case = true
    if return_pass:
        last_char = "[0-9]$"
        last_character_return = re.search(last_char,user_p)
        if last_character_return:
            init_case=true
            fail_case=false
    isTureCheck = str(init_case)[9:14].strip()
    final_check = isTureCheck == "true"
    return render_template("report.html",final_check=final_check,fail_case=fail_case)

if __name__=='__main__':
   app.run()