from flask import Flask, render_template, session, request, redirect   # Import Flask to allow us to create our app

app = Flask( __name__ )  # Create a new instance of the Flask class called "app"

app.secret_key = "EsojGnidoc"

@app.route( '/')  #, methods = ['GET'] )   # The "@" decorator associates this route with the function immediately following
def displayIndex():
    return render_template( "index.html" )


@app.route( '/process', methods = ['POST'])
def submit():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comments'] = request.form['comments']
    return redirect('/result')


@app.route( '/result')
def showResult():
    return render_template('result.html')


if __name__=="__main__":
    app.run( debug = True )


