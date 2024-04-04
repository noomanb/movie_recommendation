from flask import Flask, jsonify, request
app = Flask(__name__)
from user_user import findTop10

@app.route("/recommend", methods = ["GET", "POST"])
def recommend():
    if request.method == "POST":
        data = eval(request.json)
        print(data)
        user = data["user_id"]
        recommendation = findTop10(user)
        return jsonify(recommendation)
    else:
        return jsonify({"msg":"pls upload your user-id"})

if __name__ == "__main__":
    app.run(debug = True)