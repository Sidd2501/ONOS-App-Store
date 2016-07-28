This is the README file for the ONOS App Store repository!

The front end of this appstore is Flask(python-based), the database uses sqlite3, and the backend is composed of AngularJS.

The client side:
To run the client server, you need to first set up your environment. Follow this link to do so, https://docs.angularjs.org/tutorial
Make sure to be in the correct directory when you start the server using the "npm run serve" command.

The server side:
To run the server on frontend side, you need to first get your enviornment properly ready. First, have python v2.6 or more installed to be able to install flask. Then, use the "pip install Flask" command. You may alternatively follow this: http://www.tutorialspoint.com/flask/flask_environment.htm
to make sure. 
Once you have everything on your system installed, run the flask webserver with the "python flaskr.py" command. (Make sure you are in the correct directory). 

After this, in a new tab on your terminal, enter "npm run serve" and you should now have two servers running. If not, please make sure you have the correct code and that you are in the right directories for both. Also, that your enviornment is correctly set up.

You may now open your browser, (preferably Chrome) and go to http://localhost:5000/api/apps

In another tab, go to http://localhost:3000

You may have to double check these port numbers by just looking at what your terminal window states.

You are now accessing the work in progress ONOS App Store!

In case you wanted to access the database from your terminal, make sure to have sqlite3 installed on your system. After that, make sure you are in the right directory. Then, enter "sqlite3 AppStore.db". This should now change it so your screen says "sqlite3 >". Now, you can see the available tables by entering ".tables". Then, enter "select * from Applications;" this will give you all the entries that have been made into the app store.

For some great tutorials, visit:
http://flask.pocoo.org/docs/0.11/tutorial/
http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world
https://docs.angularjs.org/tutorial
http://www.tutorialspoint.com/flask/flask_sqlite.htm

Thanks!
- Sid and Matteo :)