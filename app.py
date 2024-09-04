from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    productos = [
        {"nombre": "Producto 1", "precio": 10.00},
        {"nombre": "Producto 2", "precio": 15.00},
        {"nombre": "Producto 3", "precio": 20.00},
    ]
    return render_template('index.html', productos=productos)

@app.route('/producto/<nombre>')
def producto(nombre):
    producto = {"nombre": nombre, "descripcion": f"Descripción del {nombre}", "precio": 10.00}
    return render_template('producto.html', producto=producto)

if __name__ == '__main__':
    app.run(debug=True)
