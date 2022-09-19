## flask server
from flask import Flask, jsonify, request# 서버 구현을 위한 Flask 객체 import
import joblib
import numpy as np
from flask_cors import CORS, cross_origin

mbti_type = {
    "A" : "대식가",
    "B" : "소식좌",
    "C" : "애주가",
    "D" : "개척자",
    "E" : "분석가",
    "F" : "인스타",
    "G" : "내신1등",
    "H" : "푸드슈타인",
    "I" : "위장 월세형",
    "J" : "위부장님",
    "K" : "앙드레 푸드",
    "L" : "스틸 통규씨",
    "N" : "헨젤이 그랬대",
    "M" : "포세이돈",
    "O" : "배달VVIP",
}

question_num = ["Q"+str(i+1) for i in range(40)]


#from flask_restx import Api, Resource  # Api 구현을 위한 Api 객체 import

app = Flask(__name__) # Flask 객체 선언, 파라미터로 어플리케이션 패키지의 이름을 넣어줌.
CORS(app, resources={r'*': {'origins': '*'}})

# api = Api(app)  # Flask 객체에 Api 객체 등록

model = joblib.load('./mbti.pkl')

@app.route('/data', methods=['POST','OPTIONS'])
def mbti_result():
    if request.is_json is True :
        print('json type in')
        content = request.get_json()
    else:
        print('urlencoded type in')
        content = request.form
    
    try:
        data = []
        for i in question_num :
            data.append(int(content[i]))
        result = np.array(data).reshape(1,40)
        print(result)
        # print(model.predict(result))
        # mbti = mbti_type[model.predict(result)[0]]
        mbti = model.predict(result)[0]
        data.append(mbti)
        print(data)
    except KeyError:
        data = [500]
    

    return jsonify({'success': data})


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=int("5000"))

