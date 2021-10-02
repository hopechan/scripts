import requests
import json


BASE_URL = ""

HEADERS = ""


def generate_code(school_id):
    """
    Generates the code for the school.
    """
    access_code = format(int(school_id) + 128, "X")
    # write here the pattern of the code
    return f"-{access_code}"


# response = requests.get(BASE_URL)
response = requests.get(BASE_URL, headers={"Authorization": HEADERS})
schoolList = []

data = response.json()

for data_school in data:
    print(data_school["code"])
    schoolList.append(
        {
            "codigoEscuela": data_school["code"],
            "nombre": data_school["name"],
            "codigoDeIngreso": generate_code(int(data_school["id"])),
        }
    )

with open("listaEscuelas.json", "w", encoding="utf-8") as f:
    json.dump(schoolList, f, ensure_ascii=False, indent=4)
