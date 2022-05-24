from flask import Flask,render_template,g,request
import sqlite3
from datetime import datetime

app = Flask(__name__) #instantiate flask


def connect_db():  #connect to the actual database file
    sql = sqlite3.connect('/home/jenith/Desktop/Food_Tracker/food_log.db')
    sql.row_factory = sqlite3.Row #results will be displayed as dictionaries
    return sql

def get_db(): #going to check the global object to see if sqlite3_db exists in there
    if not hasattr(g,'sqlite3_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db  

@app.teardown_appcontext
def close_db(error): #check if there's a sqlite3_db in the global object. If there is then it will close it at the end of every request at the end of every route.
    if hasattr(g,'sqlite_db'):
        g.sqlite_db.close()


@app.route('/', methods = ['POST','GET'])
def index():
    db = get_db()
    if request.method == 'POST':
        date = request.form['date']

        dt = datetime.strptime(date,'%Y-%m-%d')
        database_date = datetime.strftime(dt,'%Y%m%d')
        
        db.execute('insert into log_date(entry_date)values(?)',[database_date])
        db.commit()

    cur = db.execute('select entry_date from log_date order by entry_date desc')
    results = cur.fetchall()

    pretty_results = []
    for i in results:
        single_date = {}
        d= datetime.strptime(str(i['entry_date']), '%Y%m%d')
        single_date['entry_date'] = datetime.strftime(d, '%B %d, %Y')

        pretty_results.append(single_date)

    return render_template('home.html',results=pretty_results)

@app.route('/view/<date>',methods=['GET','POST']) #date is going to be something like 20170520
def view(date):
    db = get_db()
    
    cur =db.execute('select id,entry_date from log_date where entry_date = ?',[date])
    date_result = cur.fetchone()





    if request.method == 'POST':
        db.execute('insert into food_date(food_id, log_date_id) values(?,?)',[request.form['food-select'],date_result['id']])
        db.commit()
        
    


    d = datetime.strptime(str(date_result['entry_date']), '%Y%m%d')
    pretty_date = datetime.strftime(d,'%B %d, %Y')

    food_cur = db.execute('select id,name from food')
    food_results = food_cur.fetchall()
    
    return render_template('day.html',date = pretty_date, food_results=food_results)

@app.route('/food', methods=['GET','POST'])
def food():
    db = get_db() #initialise the database

    if request.method == 'POST':
        name = request.form['food-name'] #values that are posted on the food section is stores in variables
        protein = int(request.form['protein'])
        carbohydrates = int(request.form['carbohydrates'])
        fat = int(request.form['fat'])

        calories = protein*4 + carbohydrates*4 + fat*9

        
        db.execute('insert into food(name,protein,carbohydrates,fat,calories)values(?,?,?,?,?)',\
            [name,protein,carbohydrates,fat,calories]) #inserting values into the database
        db.commit()
    
    cur = db.execute('select name,protein,carbohydrates,fat,calories from food')
    results = cur.fetchall()


    return render_template('add_food.html',results = results)

if __name__ =='__main__':
    app.run(debug=True)