# all the imports
import os
import sqlite3
import json
from flask import Flask, request, session, g, redirect, url_for, abort, \
    render_template, flash, jsonify
from flask_api import status
from flask_cors import CORS, cross_origin


# create application
app = Flask(__name__)
CORS(app)
app.config.from_object(__name__)

# Load default config and override config from an environment variable
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'AppStore.db'),
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
))

app.config.from_envvar('FLASKR_SETTINGS', silent=True)
def connect_db():
    """Connects to the specific database."""
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv

def init_db():
    db = get_db()
    with app.open_resource('AppStore.db', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()

@app.cli.command('initdb')
def initdb_command():
    """Initializes the database."""
    init_db()
    print 'Initialized the database.'

def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
        print (g.sqlite_db)
    return g.sqlite_db

@app.teardown_appcontext
def close_db(error):
    """Closes the database again at the end of the request."""
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

@app.route('/')
def show_entries():
    db = get_db()
    cur = db.execute('AppID, State, Description, Version, Origin, URL')
    entries = cur.fetchall()
    return json.dumps(entries)

@app.route('/api/apps', methods=['POST'])
def add_entry():
    #if not session.get('logged_in'):
        #abort(401)
    db = get_db()
    # db.execute("create table Test2(AppID integer)")
    # db.execute("INSERT INTO Test2(AppID) values (3)")
    #var response = JSON.parse(Applications);
    print ("after APPId")
    # db.execute("insert into Applications (AppID, State, Description, Version, Origin, URL) values (400, Installed, Bla Bla Bla, 1.0.0.1, Open Networking Laboratory, go.com)")
    cur = db.execute("insert into Applications (AppID, State, Description, Version, Origin, URL) values (400, \"Installed\", \"Bla Bla Bla\", \"1.0.0.1\", \"Open Networking Laboratory\", \"go.com\")");
    entries = cur.fetchall()
    db.commit()
    print ('New entry was successfully posted')
    return json.dumps(entries)

@app.route('/api/apps/<id>', methods=['PUT'])
def update_entry(id):
    db = connect_db()
    cur = db.cursor()
    data = json.loads(request.data)
    data['id'] = id
    print type(data), data
    cur.execute('update Applications set AppID = %(AppId)s,State = "%(State)s", Description = "%(Description)s", Version = "%(Version)s", URL = "%(URL)s" where id = %(id)s' % data)
#    cur.fetchall()
    db.commit()
    return "App has been updated"

#     entries = [entry for entry in entries if entry['id'] == entry_id]
#    if len(entry) == 0:
#        abort(404)
#    if not request.json:
#        abort(400)
#    if 'title' in request.json and \
#            not isinstance(request.json['title'], six.string_types):
#        abort(400)
#    if 'description' in request.json and \
#            not isinstance(request.json['description'], six.string_types):
#        abort(400)
#    if 'done' in request.json and type(request.json['done']) is not bool:
#        abort(400)
#    entries[0]['title'] = request.json.get('title', entry[0]['title'])
#    entries[0]['description'] = request.json.get('description',
#                                              entry[0]['description'])
#    entries[0]['done'] = request.json.get('done', entry[0]['done'])
#    return jsonify({'entry': (entry[0])})


@app.route('/api/apps/<id>', methods=['DELETE'])
def delete_entry(id):
    db = connect_db()
    cur = db.cursor()
    cur.execute("delete from Applications where id = "+id)
    db.commit()
    return "App has been deleted"

@app.route('/api/apps/<id>', methods=['GET'])
def get_entries(id):
    db = connect_db()
    cur = db.cursor()
    cur.execute("select * from Applications where id = "+id)
    entries = cur.fetchall()
    print entries
    if len(entries) < 1:
        return "Not Found", status.HTTP_404_NOT_FOUND
    else:
        entry = entries[0]
        app = {
            "AppID" : entry[1],
            "State" : entry[2],
            "Description" : entry[3],
            "Version" : entry[4],
            "Origin" : entry[5],
            "URL" : entry[6]
        }
        return jsonify(app)

@app.route('/api/apps',methods= ['GET'])
def query_entry():
    db = connect_db()
    cur = db.cursor()
    cur.execute("select * from Applications")
    entries = cur.fetchall()
    print entries

    apps = []

    for entry in entries:
        print entry[0]
        app = {
            "AppID" : entry[1],
            "State" : entry[2],
            "Description" : entry[3],
            "Version" : entry[4],
            "Origin" : entry[5],
            "URL" : entry[6]
        }
        apps.append(app)

    return jsonify({'apps':apps})


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('show_entries'))
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_entries'))

if __name__ == '__main__':
    app.run(debug=True)
