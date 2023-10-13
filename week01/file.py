import json


data_dict = {
    "numbers" : [24, 34, 76, 54, 99, 11, 32, 59, 78, 32],
    "names" : ["Bob", "Betty", "James", "Jane", "Billy"],
    "phone numbers" : [20832405803, 24039823049, 29374023978]

}

def write_data_to_file(filename, data):
    try:
        with open(filename, "wt") as file_handle:
            json_data = json.dumps(data)
            file_handle.write(json_data)
    except FileNotFoundError:
        print("An error occured. The file was not found")


def read_data_from_file(filename):
    """
    Read data from filename file and return the dictionary.
    
    """
    try:
        with open(filename, "rt") as file_handle:
            json_data = file_handle.read()
            dict_data = json.loads(json_data)
            return dict_data
    except FileNotFoundError:
        print(f"An Error occured. The file: {filename} could not be found")
        return {}

def main():
    """
    Main function to drive the program
    """

    print(data_dict["numbers"])
    print(data_dict["names"])
    print(data_dict["phone numbers"])
    print()

    filename = "test_json.json"
    write_data_to_file(filename, data_dict)
    data = read_data_from_file(filename)
    print(data["numbers"])
    print(data["names"])
    print(data["phone numbers"])

if __name__=="__main__":
    main()