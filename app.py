from flask import Flask, jsonify, render_template
from db import Session, engine
from models import Usuarios


app = Flask(__name__)
session = Session()


@app.route('/')
def hello_world():  # put application's code here
    personas = session.query(Usuarios).all()

    return render_template('index.html', personas=personas)


@app.route('/crearusuario', methods=["POST"])
def create():
    with engine.connect() as con:
        nuevo_usuario = Usuarios(nombre="Cabo")
        session.add(nuevo_usuario)
        session.commit()
    return jsonify({"respuesta":"Usuario creado correctamente"})

if __name__ == '__main__':
    app.run()