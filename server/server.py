from flask import Flask, request, jsonify
from playhouse.shortcuts import model_to_dict, dict_to_model
import sys
sys.path.insert(0, "..")
from db.database import Apartments

#------------------------------------CONNECT TO THE SERVER------------------------------------
app = Flask(__name__)
# Apartments = myModule.Apartments()

#------------------------------------DEFINE THE API ENDPOINTS------------------------------------
@app.route('/apartments/', methods=['GET', 'POST'])
def root():
  if request.method == 'GET':
    apartmentList = []
    for apartment in Apartments.select():
      apartmentList.append(model_to_dict(apartment))
    return jsonify(apartmentList)
  if request.method == 'POST':
    new_apartment = dict_to_model(Apartments, request.get_json())
    new_apartment.save()
    return request.get_json()

@app.route('/apartments/id/<id>', methods=['GET', 'PUT', 'POST', 'DELETE'])

#------------------------------------RUN SERVER------------------------------------
app.run(debug=True, port=3000)


