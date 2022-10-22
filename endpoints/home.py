from fastapi import APIRouter


router = APIRouter()


@router.get(
    path="/",
    status_code=200,
    tags=["Home"],
    summary="Hola mundo de la aplicación",
    )
def hello_world():
    """
    # Hola mundo de la aplicación
    Este endpoint muestra un mensaje de bienvenida.

    Parámetros:
    - Request body:
        - Niguno
    - Request query:
        - Ninguno
    - Request header:
        - Ninguno
        
    - Request cookie:
        - Ninguno
    Regresa un JSON con el mensaje de bienvenida.
    """
    return {"message": "Hello World"}