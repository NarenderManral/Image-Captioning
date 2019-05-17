from flask import Flask,jsonify,request
import json
import requests
import predict as pr

app = Flask(__name__)

@app.route('/api/model/test',methods=['POST'])
def imageTestPost():
    incomingData=request.data
    incomingDataDic=json.loads(incomingData)
    imageURL=incomingDataDic['url']
    r=requests.get(imageURL,stream=True)

    if r.status_code!=200:
        output='Model: Image fetching failed'
    else:    
        with open('example.jpg', 'wb') as fd:
            for chunk in r.iter_content(chunk_size=128):
                fd.write(chunk)
        
        output=pr.gen('example.jpg')
    
    return jsonify({'output':output})

@app.route('/api/model/test',methods=['GET'])
def imageTestGet():
    message='you have selected model GET method'
    return jsonify({'message':message})

if __name__ == '__main__':
    app.run(debug=True)