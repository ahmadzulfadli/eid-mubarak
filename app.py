from dbClass import *

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/success')
def success():
    return render_template('success.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        pesan = request.form['pesan']
        print(pesan)
        newData = Pesan(text=pesan)
        db.session.add(newData)
        db.session.commit()
    return redirect('/success')

if __name__ == '__main__':
    app.run(debug=True)