from flask import Flask,request
from webCrawler import webCrawler
from flask import jsonify


app = Flask(__name__)

@app.route('/pdf',methods=['POST'])
def callWebCrawler():
    data = request.get_json()
    result = webCrawler(data["user_input"])
    # result =data["user_input"]
    print("...............API RECEIVED.................")
    print(result)
    return jsonify(data)


if __name__ == '__main__':
    app.run()

    