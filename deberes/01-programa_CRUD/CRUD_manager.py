import user
import stand
import stand_type
import stand_ability
import csv


class CRUD_manager:
    def __init__(self, type_class):
        self.type_class = type_class

    def create_user(self, name, birth_year=0, height_cm=0, weight_kg=0, nationality='unknown'):
        new_user = user.User(name, birth_year, height_cm,
                             weight_kg, nationality)
        filename = "users.csv"
        self.write_to_csv(filename, new_user)

    def create_stand(self, name, user_id, appearance="unknown", stand_cry="unknown", origin="unknown"):
        new_stand = stand.Stand(name, user_id, appearance, stand_cry, origin)
        filename = "stands.csv"
        self.write_to_csv(filename, new_stand)

    def create_stand_ability(self, name, stand_id, description='unknown'):
        new_stand_ability = stand_ability.Stand_ability(
            name, stand_id, description)
        filename = "stand_abilities.csv"
        self.write_to_csv(filename, new_stand_ability)

    def create_stand_stat(self, name, stand_id, description='unknown',rank='unknown'):
        new_stand_stat = stand_stat.Stand_stat(name, stand_id, description, rank)
        filename = "stand_stats.csv"
        self.write_to_csv(filename, new_stand_stat)

    def create_stand_type(self, name, stand_id, description='unknown'):
        new_stand_type = stand_type.Stand_type(name, stand_id, description)
        filename = "stand_types.csv"
        self.write_to_csv(filename, new_stand_type)

    def read_user(self, user_id):
        readed_user = self.get_object_from_csv("users.csv", user_id, "user")
        print(user_id)
        if readed_user == None:
            print("El usuario no existe")
        else:
            return readed_user

    def read_stand(self, stand_id):
        readed_stand = self.get_object_from_csv(
            "stands.csv", stand_id, "stand")
        if readed_stand == None:
            print("El Stand no existe")
        else:
            return readed_stand

    def read_stand_ability(self, stand_ability_id):
        readed_stand_ability = self.get_object_from_csv(
            "stand_abilities.csv", stand_ability_id, "stand_ability")
        if readed_stand_ability == None:
            print("La habilidad del Stando no existe")
        else:
            return readed_stand_ability

    def read_stand_stat(self, stand_stat_id):
        readed_stand_stat = self.get_object_from_csv(
            "stand_stats.csv", stand_stat_id, "stand_stat")
        if readed_stand_ability == None:
            print("El Stat del Stand no existe")
        else:
            return readed_stand_stat

    def read_stand_type(self, stand_type_id):
        readed_stand_type = self.get_object_from_csv(
            "stand_types.csv", stand_type_id, "stand_type")
        if readed_stand_type == None:
            print("El tipo de Stand no existe")
        else:
            return readed_stand_type

    def update_user(self, updated_user):
        self.update_specific_row_on_csv("users.csv", updated_user)

    def update_stand(self, updated_stand):
        self.update_specific_row_on_csv("stands.csv", updated_stand)

    def update_stand_ability(self, updated_stand_ability):
        self.update_specific_row_on_csv(
            "stand_abilities.csv", updated_stand_ability)

    def update_stand_stat(self, updated_stand_stat):
        self.update_specific_row_on_csv("stand_stats.csv", update_stand_stat)

    def update_stand_type(self, updated_stand_type):
        self.update_specific_row_on_csv("stand_types.csv", updated_stand_type)

    def delete_user(self, user_for_delete):
        self.delete_specific_row_on_csv("users.csv", user_for_delete)

    def delete_stand(self, stand_for_delete):
        self.delete_specific_row_on_csv("stands.csv", stand_for_delete)

    def delete_stand_ability(self, stand_ability_for_delete):
        self.delete_specific_row_on_csv(
            "stand_abilities.csv", stand_ability_for_delete)

    def delete_stand_stat(self, stand_stat_for_delete):
        self.delete_specific_row_on_csv("stand_stats.csv", stand_stat_for_delete)

    def delete_stand_type(self, stand_type_for_delete):
        self.delete_specific_row_on_csv("stand_types.csv", stand_type_for_delete)

    def write_to_csv(self, filename, new_object):
        header = self.generate_header_from_object(new_object)
        dictionary_from_object = new_object.__dict__
        flag_header = self.check_for_header(header, filename)
        if(flag_header):
            csv_file = open(filename, "a")
            csv_writer = csv.DictWriter(csv_file, fieldnames=header)
            csv_writer.writerow(dictionary_from_object)
        else:
            csv_file = open(filename, "w+")
            csv_writer = csv.DictWriter(csv_file, fieldnames=header)
            csv_writer.writeheader()
            csv_writer.writerow(dictionary_from_object)

    def check_for_header(self, header, filename):
        try:
            with open(filename) as csv_file:
                reader = csv.reader(csv_file, delimiter=',')
                number_line = 0
                for atributes in reader:
                    if number_line == 0:
                        if atributes == header:
                            return True
                        else:
                            return False
        except Exception as e:
            print(e)
            return False

    def generate_header_from_object(self, object):
        dictionary_from_object = object.__dict__
        list_headers = list(dictionary_from_object.keys())
        return list_headers

    def get_object_position(self, filename, object_id):
        try:
            with open(filename, 'r') as csv_file:
                reader = csv.DictReader(csv_file, delimiter=',')
                list_objects = list(reader)
                number_line = 0
                for rows in list_objects:
                    if rows["id"] == object_id:
                        return number_line
                    else:
                        number_line += 1
        except Exception as e:
            print(e)
            return 0
        return 0

    def get_object_from_csv(self, filename, object_id, object_type):
        object_position = self.get_object_position(filename, object_id)
        try:
            with open(filename, 'r') as csv_file:
                reader = csv.DictReader(csv_file, delimiter=',')
                list_objects = list(reader)
                if object_type == "stand_ability":
                    object_to_return = stand_ability.Stand_ability(
                        **list_objects[object_position])
                    return object_to_return
                elif object_type == "stand_stat":
                    object_to_return = stand_stat.Stand_stat(
                        **list_objects[object_position])
                    return object_to_return
                elif object_type == "stand":
                    object_to_return = stand.Stand(
                        **list_objects[object_position])
                    return object_to_return
                elif object_type == "user":
                    object_to_return = user.User(
                        **list_objects[object_position])
                    return object_to_return
                else:
                    return None
        except Exception as e:
            print(e)
            return None
        return None

    def update_specific_row_on_csv(self, filename, updated_object):
        object_id = updated_object.id
        object_position = self.get_object_position(filename, object_id)
        header = self.generate_header_from_object(updated_object)
        dictionary_from_object = updated_object.__dict__
        try:
            with open(filename, 'r') as csv_file:
                reader = csv.DictReader(csv_file, delimiter=',')
                list_objects = list(reader)
        except Exception as e:
            print(e)
        list_objects[object_position] = dictionary_from_object
        try:
            with open(filename, 'w') as csv_file:
                writer = csv.DictWriter(csv_file, fieldnames=header)
                writer.writeheader()
                writer.writerows(list_objects)
        except Exception as e:
            print(e)

    def delete_specific_row_on_csv(self, filename, object_for_delete):
        object_id = object_for_delete.id
        object_position = self.get_object_position(filename, object_id) - 2
        print("La posicion es" + str(object_position))
        print(object_for_delete)
        header = self.generate_header_from_object(object_for_delete)
        dictionary_from_object = object_for_delete.__dict__
        try:
            with open(filename, 'r') as csv_file:
                reader = csv.DictReader(csv_file, delimiter=',')
                list_objects = list(reader)
                print(len(list_objects))
        except Exception as e:
            print(e)
        print(list_objects[object_position])
        del list_objects[object_position]
        try:
            with open(filename, 'w') as csv_file:
                writer = csv.DictWriter(csv_file, fieldnames=header)
                writer.writeheader()
                writer.writerows(list_objects)
        except Exception as e:
            print(e)
