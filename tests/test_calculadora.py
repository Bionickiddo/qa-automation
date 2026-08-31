import pytest

def sumar(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Los valores deben ser numéricos")
    return a + b

def dividir(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Los valores deben ser numéricos")
    if b== 0:
        raise ZeroDivisionError("No se puede dividir entre cero")
    return a / b


@pytest.mark.parametrize("a, b, resultado",
    [
        (2,3,5),
        (4,5,9),
        (10,10,20),
        (-8, -2, -10),
        (-10, 4, -6),
        (-8, -5, -13)
    ]
  )

def test_suma(a,b, resultado):
    resultado_real = sumar(a, b)
    assert resultado_real == resultado
    
    
def test_suma_con_texto():
        with pytest.raises(TypeError) as error:
            sumar("a", "h")
            
        print(error.value)


@pytest.mark.parametrize(
    "a, b, resultado",
    [
        (10, 2, 5),
        (7, 2, 3.5),
        (-10, 2, -5)
    ]
)
        
        
def test_dividir(a,b, resultado):
    resultado_real = dividir(a, b)
    assert resultado_real == resultado
    
    
def test_division_con_texto():
        with pytest.raises(TypeError) as error:
            dividir("j", "m")
            
        print(error.value)
        
      
        
        
@pytest.mark.parametrize("a, b",
    [
        (5,0),
        (10,0)
    ]
)

def test_division_por_cero(a, b):
    with pytest.raises(ZeroDivisionError) as error:
        dividir(a, b)
    assert str(error.value) == "No se puede dividir entre cero"
           
    print(error.value)
    
   
        

            
        
            