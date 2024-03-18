import json
import os.path

objects = {}
# print("this is coming from the top", objects)

def get_user_input(**kwargs):
    # construct key.
    while True:
        k = input("Enter attribute name (or 'done' to finish): ")
        if k.lower() == 'done':
            break
            # exit(0)
        value = input(f"Enter value for {k}: ")
        kwargs[k] = value

    key = f"{kwargs['name']}.{kwargs['email']}"
    # this code is about to trigger.
    print("before the kwargs get triggered", objects)
    objects[key] = kwargs

    # control is yet to arrive here.
    with open('database.json', 'w') as file:
        json.dump(objects, file, indent=2)


def reload():
    # want to read the data from toby from the file
    # asign the data back to the file.
    if os.path.exists("database.json") and os.path.getsize("database.json") > 0:
        with open("database.json", "r") as file:
            data = json.load(file)

            for k, v in data.items():
                # print("key: {} value: {}".format(k, v))
                objects[k] = v


reload()
# print("after the reload method", objects)
get_user_input()
# print("this is the big object", objects)



