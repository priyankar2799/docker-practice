# importing flask class from flask framework, request: incoming request, redirect: redirect user to another entrypoint, url_for:creates url for new entrypoint
from flask import Flask, redirect, url_for, request

# python speacial variable, defines root path of application
app = flask(__name__)

#route defines the root of url, when the user vists the root url flask will call the function and returns the string
@app.route('/success/<name>')
def success(name):
 return 'Hello %s' % name 
  
#This code defines a route /login that accepts both POST and GET requests. If the request method is POST, it retrieves the value of the nm form field submitted by the user, and redirects the user to the /success/<name> route using redirect(url_for('success', name=user)). If the request method is GET, it retrieves the value of the nm query parameter from the URL and performs the same redirection.
@app.route('/login' , methods['POST','GET'] )
def login():
 if request.method = "POST"
        user = request.form['nm']
        return redirect(url_for('success', name=user))
    else:
        user = request.args.get('nm')
        return redirect(url_for('success', name=user))
 
 
if __name__ == '__main__':
    app.run(debug=True)


