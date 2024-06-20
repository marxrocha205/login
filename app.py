from flask import Flask, request, render_template
import process  # Importando o módulo de processamento de dados

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('register.html')

@app.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['senha']
        
        xml_file_path = 'users.xml'
        
        if process.register_user(name, email, password, xml_file_path):
            return render_template('welcome.html', name=name)
        else:
            return "Usuário já registrado", 409

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['senha']
        
        xml_file_path = 'users.xml'
        
        if process.process_data(email, password, xml_file_path):
            return render_template('welcome.html', name=email)
        else:
            return "Usuário não encontrado", 401
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
