from flask import Flask, render_template, request

app = Flask(__name__)


def calcular_notas(nota1, nota2, nota3, asistencia):
    promedio = round((nota1 + nota2 + nota3) / 3, 1)
    if promedio >= 40 and asistencia >= 75:
        estado = "APROBADO"
    else:
        estado = "REPROBADO"
    return promedio, estado


def nombre_mas_largo(nombre1, nombre2, nombre3):
    nombres = [nombre1, nombre2, nombre3]
    mayor = max(nombres, key=len)
    return mayor, len(mayor)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        nota1 = float(request.form['nota1'])
        nota2 = float(request.form['nota2'])
        nota3 = float(request.form['nota3'])
        asistencia = float(request.form['asistencia'])

        promedio, estado = calcular_notas(nota1, nota2, nota3, asistencia)
        return render_template(
            'ejercicio1.html',
            promedio=promedio,
            estado=estado,
            nota1=int(nota1) if nota1.is_integer() else nota1,
            nota2=int(nota2) if nota2.is_integer() else nota2,
            nota3=int(nota3) if nota3.is_integer() else nota3,
            asistencia=int(asistencia) if asistencia.is_integer() else asistencia
        )
    return render_template('ejercicio1.html')


@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    if request.method == 'POST':
        nombre1 = request.form['nombre1'].strip()
        nombre2 = request.form['nombre2'].strip()
        nombre3 = request.form['nombre3'].strip()

        mayor, cantidad = nombre_mas_largo(nombre1, nombre2, nombre3)
        return render_template(
            'ejercicio2.html',
            mayor=mayor,
            cantidad=cantidad,
            nombre1=nombre1,
            nombre2=nombre2,
            nombre3=nombre3
        )
    return render_template('ejercicio2.html')


if __name__ == '__main__':
    app.run(debug=True)