from flask import Flask, request, jsonify
from db_config import get_db_connection

app = Flask(__name__)

# Function to check if user is authorized
def is_authorized(auth_token):
    return auth_token == 'your_secure_token'

# POST route to add health data
@app.route('/add_health_data', methods=['POST'])
def add_health_data():
    auth_token = request.headers.get('Authorization')
    if not is_authorized(auth_token):
        return jsonify({"message": "Unauthorized"}), 401

    data = request.json

    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO health_data (pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree_function, age)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, 
        data['pregnancies'], 
        data['glucose'], 
        data['blood_pressure'], 
        data['skin_thickness'], 
        data['insulin'], 
        data['bmi'], 
        data['diabetes_pedigree_function'], 
        data['age'])
        
        conn.commit()
        return jsonify({"message": "Data added successfully!"}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 400
    finally:
        conn.close()

# GET route to retrieve health data
@app.route('/get_health_data', methods=['GET'])
def get_health_data():
    auth_token = request.headers.get('Authorization')
    if not is_authorized(auth_token):
        return jsonify({"message": "Unauthorized"}), 401

    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM health_data")
        rows = cursor.fetchall()

        result = []
        for row in rows:
            result.append({
                'id': row[0],
                'pregnancies': row[1],
                'glucose': row[2],
                'blood_pressure': row[3],
                'skin_thickness': row[4],
                'insulin': row[5],
                'bmi': row[6],
                'diabetes_pedigree_function': row[7],
                'age': row[8]
            })
        
        return jsonify(result), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 400
    finally:
        conn.close()

if __name__ == '__main__':
    app.run(debug=True)
