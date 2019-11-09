import CRUD_manager
import user
import stand
import stand_type
import stand_ability
import csv
from os import system, name
def create_new_user():
    print("\n===================================================================")
    print("Insertar Stand Master")
    name = input("Ingrese el Nombre del Stand Master: ")
    birth_year = int(input("Ingrese el año de nacimiento: "))
    height_cm = float(input("Ingrese la altura(en centimetros): "))
    weight_kg = float(input("Ingrese el peso(en kilogramos): "))
    nationality = input("Ingrese la nacionalidad: ")
    new_crud = CRUD_manager.CRUD_manager("User")
    new_crud.create_user(name,birth_year,height_cm,weight_kg,nationality)

def create_new_stand():
    print("\n===================================================================")
    print("Insertar Stand")
    name = input("Ingrese el Nombre del Stand: ")
    print("Seleccione el Stand Master:")
    user_id = select_item_id("users.csv")
    if user_id == None:
        print("No existen Stand Masters, creelos y vuelva a intentar")
    else:
        appearance = input("Ingrese la apariencia: ")
        stand_cry = input("Ingrese el grito del Stand: ")
        origin = input("Ingrese el origen del Stand: ")
        new_crud = CRUD_manager.CRUD_manager("Stand")
        new_crud.create_stand(name,user_id,appearance,stand_cry,origin)

def create_new_stand_ability():
    print("\n===================================================================")
    print("Insertar Habilidad del Stand")
    name = input("Ingrese el Nombre de la habilidad del Stand: ")
    print("Seleccione el Stand: ")
    stand_id = select_item_id("stands.csv")
    if stand_id == None:
        print("No existen Stands, creelos y vuelva a intentar")
    else:
        description = input("Ingrese la descripción de la habilidad: ")
        new_crud = CRUD_manager.CRUD_manager("Stand_ability")
        new_crud.create_stand_ability(name,stand_id,description)

def create_new_stand_type():
    print("\n===================================================================")
    print("Insertar Tipo del Stand")
    name = input("Ingrese el Nombre del tipo de Stand: ")
    print("Seleccione el Stand: ")
    stand_id = select_item_id("stands.csv")
    if stand_id == None:
        print("No existen Stands, creelos y vuelva a intentar")
    else:
        description = input("Ingrese la descripción del tipo: ")
        new_crud = CRUD_manager.CRUD_manager("Stand_type")
        new_crud.create_stand_type(name,stand_id,description)

def create_new_stand_stat():
    print("\n===================================================================")
    print("Insertar el Stat del Stand")
    name = input("Ingrese el Nombre del Stat de Stand: ")
    print("Seleccione el Stand: ")
    stand_id = select_item_id("stands.csv")
    if stand_id == None:
        print("No existen Stands, creelos y vuelva a intentar")
    else:
        description = input("Ingrese la descripción del Stat: ")
        rank = input("Ingrese el ranking de la habilidad: ")
        new_crud = CRUD_manager.CRUD_manager("Stand_stat")
        new_crud.create_stand_stat(name,stand_id,description)

def show_user(user_id):
    new_crud = CRUD_manager.CRUD_manager("User")
    user = new_crud.read_user(user_id)
    print("\n===================================================================")
    print("User ID: "+ user.id)
    print("Nombre: "+ user.name)
    print("Año de nacimiento: "+ str(user.birth_year))
    print("Altura(cm): "+ str(user.height_cm))
    print("Peso(kg): "+ str(user.weight_kg))
    print("Nacionalidad: "+ user.nationality)

def show_all_users():
    try:
        with open("users.csv", 'r') as csv_file:
            reader = csv.DictReader(csv_file, delimiter=',')
            list_objects = list(reader)
            if len(list_objects) == 0:
                print("No existen usuarios")
            for item in list_objects:
                show_user(item["id"])
    except Exception as e:
       print(e)

def show_stand(stand_id):
    new_crud = CRUD_manager.CRUD_manager("Stand")
    print(stand_id)
    stand = new_crud.read_stand(stand_id)
    print("\n===================================================================")
    print("Stand ID: "+ stand.id)
    print("Nombre: "+ stand.name)
    stand_master_name = new_crud.read_user(stand.user_id).name
    print("Stand Master Name: "+ stand_master_name)
    print("Apariencia: "+ stand.appearance)
    print("Grito de Stand: "+ stand.stand_cry)
    print("Origen: "+ stand.origin)

def show_all_stands():
    try:
        with open("stands.csv", 'r') as csv_file:
            reader = csv.DictReader(csv_file, delimiter=',')
            list_objects = list(reader)
            if len(list_objects) == 0:
                print("No existen usuarios")
            for item in list_objects:
                show_stand(item["id"])
    except Exception as e:
       print(e)

def update_user(user_id):
    print("\n===================================================================")
    print("Actualizar Usuario")
    show_user(user_id)
    name = input("Ingrese el Nombre del Stand Master: ")
    birth_year = int(input("Ingrese el año de nacimiento: "))
    height_cm = float(input("Ingrese la altura(en centimetros): "))
    weight_kg = float(input("Ingrese el peso(en kilogramos): "))
    nationality = input("Ingrese la nacionalidad: ")
    updated_user = user.User(name, birth_year, height_cm,
                         weight_kg, nationality, user_id)
    new_crud = CRUD_manager.CRUD_manager("User")
    new_crud.update_user(updated_user)

def update_stand(stand_id):
    print("\n===================================================================")
    print("Actualizar Stand")
    show_stand(stand_id)
    name = input("Ingrese el Nombre del Stand: ")
    print("Seleccione el Stand Master:")
    user_id = select_item_id("users.csv")
    if user_id == None:
        print("No existen Stand Masters, creelos y vuelva a intentar")
    else:
        appearance = input("Ingrese la apariencia: ")
        stand_cry = input("Ingrese el grito del Stand: ")
        origin = input("Ingrese el origen del Stand: ")
        updated_stand = stand.Stand(name,user_id,appearance,stand_cry,origin,stand_id)
        new_crud = CRUD_manager.CRUD_manager("Stand")
        new_crud.update_stand(updated_stand)

def delete_user(user_id):
    new_crud = CRUD_manager.CRUD_manager("User")
    user = new_crud.read_user(user_id)
    new_crud.delete_user(user)

def delete_stand(stand_id):
    new_crud = CRUD_manager.CRUD_manager("Stand")
    stand = new_crud.read_stand(stand_id)
    new_crud.delete_stand(stand)

def select_item_id(filename):
    try:
        with open(filename, 'r') as csv_file:
            reader = csv.DictReader(csv_file, delimiter=',')
            list_objects = list(reader)
            if len(list_objects) < 2:
                return None
            number_line = 0
            for item in list_objects:
                print(str(number_line) + ") "+ item["name"])
                number_line += 1
    except Exception as e:
       print(e)
    selected = int(input("Elige: "))
    print(list_objects[selected])
    print(list_objects[selected]["id"])
    return list_objects[selected]["id"]

def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
