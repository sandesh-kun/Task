import json
from D9_T8 import User_acc

class SerializableUser(User_acc):
    def to_json(self):
        return json.dumps(self.__dict__)

    @classmethod
    def from_json(cls, json_data):
        user_data = json.loads(json_data)
        return cls(**user_data)

obj = SerializableUser("", "", "")

while True:
    command = input("1. Registration \n2. Login \n3. Serialize User \n4. Deserialize User \nEnter command: ")
    
    if command == '1':
        obj.user_reg()
        
    elif command == '2':
        obj.user_login()

    elif command == '3':
        serialized_user = obj.to_json()
        print("\nSerialized User Object:")
        print(serialized_user)

    elif command == '4':
        json_data = input("Enter JSON data to deserialize: ")
        new_user_obj = SerializableUser.from_json(json_data)
        print("\nDeserialized User Object:")
        print(f"Username: {new_user_obj.u_name}")
        print(f"Password: {new_user_obj.passw}")
        print(f"Phone Number: {new_user_obj.phone_number}")

    else:
        print("Enter valid command.")
