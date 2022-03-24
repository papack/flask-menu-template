from flask import Flask
app = Flask(__name__, static_folder='public', static_url_path='')

#Serve the frontend
@app.route('/')
def root():
    return app.send_static_file('index.html')

#Demo function 1
@app.route('/api/v1/func1')
def func1():

    #do some stuff
    print("I likes turtles")

    #Status code 200 is "OK"
    #https://developer.mozilla.org/de/docs/Web/HTTP/Status
    return ("",200)

#Demo function 2
@app.route('/api/v1/func2')
def func2():
    
    #do something useful
    hello="hello "
    world="world"
    print(hello+world)
    
    #Status code 200 is "OK"
    return ("",200)

#run the server
if __name__ == "__main__":
    app.run()