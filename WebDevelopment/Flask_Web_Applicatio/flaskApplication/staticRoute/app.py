from flask import Flask
# Creating a Flask object
app = Flask(__name__)

# Assign a URL route in function
@app.route("/")
def home():
    return "Hello World to the HomePage!"
@app.route("/educative")
def learn():
    return "Happy Learning at Educatuve!"

# Run the application in main
if __name__ == "__main__":
    app.run(debug = True, host = "0.0.0.0", port = 3000)




