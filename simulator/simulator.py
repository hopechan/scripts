import requests

# url de login
BASE_URL = ""

# headers de la petición, en caso de ser necesarios
HEADERS = ""

# array con los datos de acceso de cada usuario
students = []


def simulate_login(param):
    """
    Simulate a login to the API.
    """
    response = requests.post(
        BASE_URL, data={"identifier": param}, headers={"Authorization": HEADERS}
    )
    return response.status_code


# por cada usuario, se simula el login e imprime el codigo de estado de la peticion
for student in students:
    response = simulate_login(student)
    print(f"estudiante: {student} status: {response}")
