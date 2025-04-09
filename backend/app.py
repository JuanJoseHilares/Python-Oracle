import os
import sys
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

# Asegúrate de que Flask pueda encontrar el archivo config.py dentro de la carpeta 'config'
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'config'))

# Inicializar la aplicación Flask
app = Flask(__name__)
CORS(app)

# Cargar configuración desde el archivo config.py
app.config.from_pyfile('config/config.py')


db = SQLAlchemy(app)

class Alumno(db.Model):
    __tablename__ = 'CUSTOMER'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email
        }

# Ruta para obtener todos los alumnos
@app.route('/alumnos', methods=['GET'])
def get_alumnos():
    alumnos = Alumno.query.all()
    return jsonify([alumno.to_dict() for alumno in alumnos])

# Ruta comentada  para obtener un alumno por ID

# @app.route('/alumnos/<int:id>', methods=['GET'])
# def get_alumno(id): #define la funcion y recibe un id como parámetro
#     # Busca el alumno por ID en la base de datos
#     alumno = Alumno.query.get(id)
#     z
#     if alumno:
#         # Si el alumno existe, devuelve su información
#         # en formato JSON
#         return jsonify(alumno.to_dict())
#     else:
#         # Si el alumno no existe, devuelve un error 404
#         return jsonify({'error': 'Alumno no encontrado'}), 404 


# Ruta mejorada para obtener un alumno por ID
@app.route('/alumnos/<int:id>', methods=['GET'])
def get_alumno(id): 
    try:
        alumno = Alumno.query.get(id)
        
        if alumno:
            
            return jsonify(alumno.to_dict())
        
        else:

            return jsonify({'error': 'Alumno no encontrado'}), 404
    except Exception as e:

        return jsonify({'error': f'Error al procesar la solicitud: {str(e)}'}), 500


# Ruta para crear un nuevo alumno
@app.route('/alumnos', methods=['POST'])
def create_alumno():
    data = request.get_json()
    if not data or 'name' not in data or 'email' not in data:
        return jsonify({'error': 'Los datos estan incompletos'}), 400
    
    new_alumno = Alumno(
        name=data['name'],
        email=data['email']
    )
    
    db.session.add(new_alumno)
    db.session.commit()
    
    return jsonify(new_alumno.to_dict()), 201


# Ruta para actualizar un alumno 
@app.route('/alumnos/<int:id>', methods=['PUT'])
def update_alumno(id):
    data = request.get_json()
    alumno = Alumno.query.get(id)
    
    if not alumno:
        return jsonify({'error': 'Alumno no encontrado'}), 404
    
    if 'name' in data:
        alumno.name = data['name']
    if 'email' in data:
        alumno.email = data['email']
    
    db.session.commit()
    
    return jsonify(alumno.to_dict())

# Ruta para eliminar un alumno
@app.route('/alumnos/<int:id>', methods=['DELETE'])
def delete_alumno(id): 
    alumno = Alumno.query.get(id)
    
    if not alumno:
        return jsonify({'error': 'Alumno no encontrado'}), 404
    
    db.session.delete(alumno)
    db.session.commit()
    
    return jsonify({'message': 'Alumno eliminado'}), 204



print("SQLALCHEMY_DATABASE_URI:", app.config['SQLALCHEMY_DATABASE_URI'])

# Ejecutar la aplicación
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)