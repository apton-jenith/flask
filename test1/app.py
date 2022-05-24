from flask import Flask,session,render_template,request,redirect,g,url_for
import os


app = Flask(__name__)

app.secret_key = os.urandom(24)


@app.route('/', methods= ['GET','POST'])
def index():
    if request.method =='POST':
        session.pop('user',None)

        if request.form['password'] =='password':
            session['user'] = request.form['username']
            return redirect(url_for('protected'))
    
    return render_template('index.html')

@app.route('/protected')
def protected():
    if g.user:
        return render_template('protected.html',user=session['user'])
    return redirect(url_for('index')) 

@app.before_request
def before_request():
    g.user = session['user']

    if 'user' in session:
        g.user = session['user']


if __name__=='__main__':
    app.run(Debug=True)