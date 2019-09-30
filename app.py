from fnclass import *
from flask import Flask,render_template,request,redirect,url_for

app = Flask(__name__)

#first page is index
@app.route("/")
def index():
        return render_template("index.html")

#Show data in menu.txt to page showmenu
@app.route("/showmenu")
def Showmenu():
        show = Menu().showdata("menu")
        return render_template("showmenu.html",dataH = show)

#Delete data in menu.txt
@app.route("/delete/<string:id>")
def Delete(id):
        Menu().delete(id,"menu")
        return redirect("/showmenu")

#Push data product to munu.txt
@app.route("/push" ,methods=["POST"])
def Push():
        if request.method == "POST":
                pid = request.form["id"]
                pname = request.form["name"]
                pprice = request.form["price"]
                Menu().push(pid,pname,pprice,"menu")
                return redirect("/showmenu")

#Show data in order.txt to page order
@app.route("/ordershow")
def Ordershow():
        show = Menu().showdata("menu")
        data = menuOrder().showdata()        
        return render_template("order.html",dataO = data,dataH = show)

#get data form page order and push it to order.txt 
@app.route("/getorder",methods=["POST"])
def getOrder():
        if request.method=="POST":
                oId = request.form["id"]
                amount = request.form["amount"]                          
                data = Menu().search(oId,"menu")
                if data != None:
                        menuOrder().push(data.id,data.name,data.price,amount)
                return redirect("/ordershow")

#delete data.id in order.txt 
@app.route("/deleteorder/<string:id>")
def DeleteOrder(id):
        menuOrder().delete(id)
        return redirect("/ordershow")

#clear data in order.txt
@app.route("/checkbill")
def CheckBil():
        menuOrder().clear()
        return redirect("/ordershow")

if __name__ == "__main__":
        app.run(host = "0.0.0.0", port=80, debug=True)