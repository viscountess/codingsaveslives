from flask import Flask, render_template, request, Response #importds functions to use python with html

app = Flask("saves_lives_app") #making an app

@app.route("/")    #@ makes it a 'decorator'. line tells peple where to look inside flask framework. Decorators always followed by function.
def landing_page():
        return render_template("landing_page.html") #runs the landing page

#Forum pages
@app.route("/forum")  
def forum_landing_page():
        return render_template("forum_landing_page.html") #runs the forum landing page

@app.route("/forum/ask_a_question")
def forum_ask_a_question():
        return render_template("forum_ask_a_question.html") #runs the new question submission page

#Resources
@app.route("/resources")
def resources_landing_page():
        return render_template("resources_landing_page.html") #runs the resources page

#Decoy
@app.route("/error_404_display")
def Error_404_Display():
        return render_template("Error_404_Display.html") #runs the fact that this url shows the display an error page

#about Maia pages
@app.route("/about")
def about_us():
        return render_template("about_us.html") #runs the fact that this url shows the about page

@app.route("/privacy")
def privacy_policy():
        return render_template("privacy_policy.html") #runs the fact that this url shows the PP page

@app.route("/code_of_conduct")
def Code_of_Conduct():
        return render_template("Code_of_Conduct.html") #runs the fact that this url shows the code of conduct page

#debugging
app.run(debug=True) #runs the app. the debug part - unlocks debugging feature.