
contacts = {}

def input_error(error):
    def wrapper(*args, **kwargs):
        try:
            return error(*args, **kwargs)
        except KeyError:
            return "Ви ввели не вірне ім'я"
        except IndexError:
            return "Потрібне ім'я та номер телефону"
        except ValueError as red:
            return red.args[0]
    return wrapper

@input_error
def first_step():
    return "How can I help you?"


@input_error
def add_contacts(data):
    new_data = data.strip().split(" ")
    name = new_data[0]
    phone = new_data[1]
    if name in contacts:
        raise ValueError("Дублікат імені")
    contacts[name] = phone
    return f"Ви створили {name}:{phone}"



@input_error
def change_funk(data):
    new_data = data.strip().split(" ")
    name = new_data[0]
    phone = new_data[1]
    if name in contacts:
        contacts[name] = phone
        return f"Для контакту {name} змінено номер на {phone}"
    return f"За даним {name} контакту не існує, зверніться до команди add "



@input_error
def find_phone(data):
    new_data = data.strip()
    name = new_data[0]
    return contacts.get(name)



@input_error
def show_all_funk():
    contact = ""
    for name, phone in contacts.items():
        contact += f"{name} : {phone} \n"
    return contact


@input_error
def quit_funk():  # Функція виходу з команд "good bye", "close", "exit".
    return "До наступної зустрічі"

COMMANDS = {
"hello" : first_step,
"add" : add_contacts,
"change": change_funk,
"phone": find_phone,
"show all": show_all_funk,
"good bye" : quit_funk,
"close" : quit_funk,
"exit" : quit_funk
}

def return_func(data):
    return COMMANDS.get(data, error_func)


def error_func():
    return "Помилкова команда"


def edits(input_data):
    key_part = input_data
    data_part = ""
    for command in COMMANDS:
        if input_data.strip().lower().startswith(command):
            key_part = command
            data_part = input_data[len(key_part):]
            break
    if data_part:
        return return_func(key_part)(data_part)
    else:
        return return_func(key_part)()


def main():
    while True:
        user_input = input("Введіть команду: ")
        res = edits(user_input)
        print(res)
        if res == "До наступної зустрічі":
            break



if __name__ == "__main__":
    main()