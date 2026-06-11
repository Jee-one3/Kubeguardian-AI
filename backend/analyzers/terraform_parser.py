import hcl2
import pprint

def load_terraform_file(file_path):

    with open(file_path, "r") as file:

        data = hcl2.load(file)
    pprint.pprint(data, width=120)
    return data