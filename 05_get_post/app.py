from flask import Flask, request, jsonify
from flask_cors import CORS   # Cross-Origin Resource Sharing


app = Flask(__name__)
CORS(app)
# Dictionary as a  data store
guestbook = [
    {"id": 1, "name": "Venkata Lakshmi", "message": "Hello from Venkata Lakshmi!"}
]

@app.route('/guests', methods=['GET'])
def get_guests():
    # GET is used to retrieve data
    return jsonify({"status": "success", "data": guestbook}), 200

@app.route('/guests', methods=['POST'])
def add_guest():
    # POST is used to send/create data
    new_data = request.get_json() # json data
    print(new_data)
    
    if not new_data or 'name' not in new_data:
        return jsonify({"error": "Missing name"}), 400
    
    new_entry = {
        "id": len(guestbook) + 1,
        "name": new_data['name'],
        "message": new_data.get('message', 'No message')
    }
    guestbook.append(new_entry)
    
    return jsonify({"status": "created", "added": new_entry}), 201

if __name__ == '__main__':
    app.run(debug=True, port=5000)