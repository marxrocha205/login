import xml.etree.ElementTree as ET

def load_users_from_xml(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    
    users = []
    for user in root.findall('user'):
        email = user.find('email').text
        password = user.find('password').text
        users.append({'email': email, 'password': password})
    
    return users

def check_credentials(email, password, users):
    for user in users:
        if user['email'] == email and user['password'] == password:
            return True
    return False

def register_user(name, email, password, xml_file_path):
    tree = ET.parse(xml_file_path)
    root = tree.getroot()
    
    # Verificar se o usuário já existe
    for user in root.findall('user'):
        if user.find('email').text == email:
            print("Usuário já registrado.")
            return False
    
    # Adicionar novo usuário
    new_user = ET.SubElement(root, "user")
    ET.SubElement(new_user, "email").text = email
    ET.SubElement(new_user, "password").text = password
    
    tree.write(xml_file_path)
    print(f'Usuário {name} registrado com sucesso.')
    return True

def process_data(email, password, xml_file_path):
    users = load_users_from_xml(xml_file_path)
    if check_credentials(email, password, users):
        print('Usuário encontrado.')
        return True
    else:
        print('Usuário não encontrado.')
        return False
