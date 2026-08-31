import pytest
import requests
from usuarios_service import validar_login
from datos_usuarios import usuarios

  
    
@pytest.fixture
def url_base():
    return "https://jsonplaceholder.typicode.com"



@pytest.mark.parametrize("usuario, password, resultado_esperado", [
    ("admin", "1234", True),
    ("jose", "hummus", True),
    ("luismi", "434599", False),
    ("juan", "1234", False),
    ("admin" ,"", False)
])

#test de login
def test_validar_login(usuario, password, resultado_esperado):
    assert validar_login(usuario, password) == resultado_esperado
     
   
@pytest.mark.parametrize("usuario", usuarios)
    
#Solo para usuarios existentes cogiendo desde datos_usuarios         
def test_obtener_usuario(url_base, usuario):
    respuesta = requests.get(
        f"{url_base}/users/{usuario['id']}"
    )
   
    assert respuesta.status_code == 200
    
    datos = respuesta.json()
    
    assert datos["id"] == usuario["id"]
    assert datos["name"] == usuario["name"]
    assert datos["email"] == usuario["email"]
    assert datos["company"]["name"] == usuario["company"]["name"]
    
    print("DATOS ESPERADOS:", usuario)
    print("DATOS RECIBIDOS:", datos)
    

#Parametrize para usuarios que no existen 
@pytest.mark.parametrize("usuario_id, status_esperado",[
    (23, 404),
    (67, 404)
     ])

#Comprueba que devuelve error 404 por lo tanto no existe
def test_obtener_usuario_inexistente(url_base, usuario_id, status_esperado):
    
    respuesta = requests.get(
        f"{url_base}/users/{usuario_id}"
    )
   
    assert respuesta.status_code == status_esperado