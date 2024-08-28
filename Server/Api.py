from flask import Flask,request
from webCrawler import webCrawler
from flask import jsonify
import asyncio

app = Flask(__name__)

@app.route('/plag',methods=['POST'])
async def callWebCrawler():
    data = request.get_json()
    result = webCrawler(data["user_input"])
    # result =data["user_input"]
    print("...............API RECEIVED.................")
    print(result)
    if(result):
        return jsonify(result)


if __name__ == '__main__':
    app.run()

    