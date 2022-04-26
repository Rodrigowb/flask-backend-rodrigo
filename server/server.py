from flask import Flask, request, jsonify
from playhouse.shortcuts import model_to_dict, dict_to_model
import sys
sys.path.insert(0, "..")
from db.database import Apartments

#------------------------------------CONNECT TO THE SERVER------------------------------------
app = Flask(__name__)

#------------------------------------DEFINE THE API ENDPOINTS------------------------------------
@app.route('/apartments/', methods=['GET', 'POST'])
def root_routes():
  if request.method == 'GET':
    apartmentList = []
    for apartment in Apartments.select():
      apartmentList.append(model_to_dict(apartment))
    return jsonify(apartmentList)
  if request.method == 'POST':
    new_apartment = dict_to_model(Apartments, request.get_json())
    new_apartment.save()
    return {"Added": True, "Row": request.get_json()}

@app.route('/apartments/id/<id>', methods=['GET', 'PUT', 'DELETE'])
def id_routes(id):
  if request.method == 'GET':
    return jsonify(model_to_dict(Apartments.get(Apartments.id == id)))
  if request.method == 'PUT':
    updted_apartment = Apartments.update(request.get_json()).where(Apartments.id == id)
    updted_apartment.execute()
    return {"Updated": True, "Id": id}
  if request.method == 'DELETE':
    delete_apartment = Apartments.delete().where(Apartments.id == id)
    delete_apartment.execute()
    return {"Deleted": True, "Id": id}

  

#------------------------------------RUN SERVER------------------------------------
app.run(debug=True, port=3000)


