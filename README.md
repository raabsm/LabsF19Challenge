Hi!

The main page with no endpoint renders index.html.  If you query the endpoint "information/<library_name>", information on room availability in that library will be rendered onto the libraries.html page.  This is accomplished via a template.  

If you query the endpoint "information/<number>", that number of libraries will be presented to you, in order of least-occupied to most-occupied.  
  
I created a variable at the top of app.py to input the correct API-key.  
