from distutils.log import debug
import pickle
from flask import Flask
from flask import request

app = Flask('score')

model_file = 'model1.bin'
dv_file = 'dv.bin'

with open (model_file, 'rb') as model_file_in:
        model = pickle.load(model_file_in)

with open (dv_file, 'rb') as dv_file_in:
    dv = pickle.load(dv_file_in)    

@app.route('/score', methods= ['POST'])
def score():
    client = request.get_json()  
    client_vect = dv.transform(client)
    score = model.predict_proba(client_vect)[0,1]
    card_granted = score >=0.5

    result = {
        'score': float(score),
        'card_granted': bool(card_granted)
    }

    return result

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)