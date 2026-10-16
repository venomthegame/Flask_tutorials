from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB Atlas connection
MONGO_URI = "mongodb+srv://abhinav12345:Abhinav12345@cluster0.7e1kcyg.mongodb.net/?appName=Cluster0"

client = MongoClient(MONGO_URI)

# Database
db = client["studentDB"]

# Collection
collection = db["students"]


@app.route("/", methods=["GET", "POST"])
def form():

    error = None

    if request.method == "POST":
        try:
            name = request.form["name"]
            email = request.form["email"]
            course = request.form["course"]

            # Insert data into MongoDB
            collection.insert_one({
                "name": name,
                "email": email,
                "course": course
            })

            # Redirect after successful submission
            return render_template("success.html")

        except Exception as e:
            # Display error on same page
            error = str(e)

    return render_template("form.html", error=error)


if __name__ == "__main__":
    app.run(debug=True)




    # id- abhinav12345
    # password-Abhinav12345

    # uri-mongodb+srv://abhinav12345:<db_password>@cluster0.7e1kcyg.mongodb.net/?appName=Cluster0