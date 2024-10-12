
from flask import Flask, render_template, request, redirect, url_for
import csv

app = Flask(__name__)

# Chemin vers le fichier CSV
CSV_FILE = 'data/transports.csv'

# Route pour afficher la liste des transports
@app.route('/')
def index():
    transports = []
    with open(CSV_FILE, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            transports.append(row)
    return render_template('index.html', transports=transports)

# Route pour ajouter un nouveau transport
@app.route('/add', methods=['GET', 'POST'])
def add_transport():
    if request.method == 'POST':
        new_transport = {
            'id': request.form['id'],
            'patient': request.form['patient'],
            'from': request.form['from'],
            'to': request.form['to'],
            'time': request.form['time']
        }
        with open(CSV_FILE, 'a', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=new_transport.keys())
            writer.writerow(new_transport)
        return redirect(url_for('index'))
    return render_template('add.html')

if __name__ == '__main__':
    app.run(debug=True, port=5001)
