from flask import Flask, render_template, request, Response #importds functions to use python with html

app = Flask("saves_lives_app") #making an app

@app.route("/")    #@ makes it a 'decorator'. line tells peple where to look inside flask framework. Decorators always followed by function.
def our_landing_page():
        return render_template("landing_page.html") #runs the fact that our base url shows the landing page

@app.route("/resources")    #@ makes it a 'decorator'. line tells peple where to look inside flask framework. Decorators always followed by function.
def our_landing_page():
        return render_template("resources_landing_page.html") #runs the fact that this url shows the resources page

@app.route("/forum")    #@ makes it a 'decorator'. line tells peple where to look inside flask framework. Decorators always followed by function.
def our_landing_page():
        return render_template("forum_landing_page.html") #runs the fact that this url shows the forum page