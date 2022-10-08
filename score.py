import pickle

model_file = 'model1.bin'
dv_file = 'dv.bin'

with open (model_file, 'rb') as model_file_in:
    model = pickle.load(model_file_in)

with open (dv_file, 'rb') as dv_file_in:
    dv = pickle.load(dv_file_in)

print(model, dv)

client = {"reports": 0, "share": 0.001694, "expenditure": 0.12, "owner": "yes"}

client_vect = dv.transform(client)

result = model.predict_proba(client_vect)[0,1]

print(result)