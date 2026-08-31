from datos_usuarios import usuarios_login

def validar_login (usuario, password):
    if usuario in usuarios_login:
       return usuarios_login[usuario] == password
    else: 
       return False
   
   