import json
import yaml


# -------------- Json to txt --------------#
def json_to_text(json_file, text_file):
    with open(json_file, 'r') as js:
        for i in json.load(js):
            with open(text_file, 'a') as txt:
                txt.write(f"{i}\n")


# TESTING
with open("File1.json", 'w') as js:
    json.dump([{"name": "samsung", "price": "500", "quantity": "10"},
               {"name": "iphone", "price": "600", "quantity": "5"}], js, indent=4)
with open("File.txt", 'w') as txt:
    pass
json_to_text("File1.json", "File.txt")


# -------------- Json to YAML --------------#
def json_to_yaml(json_file, yaml_file):
    with open(json_file, 'r') as js:
        with open(yaml_file, 'a') as yml:
            yaml.dump(json.load(js), yml)


# TESTING
with open("File2.yaml", 'w'):
    pass
json_to_yaml("File1.json", "File2.yaml")


# -------------- YAML to Json --------------#
def json_to_yaml(yaml_file, json_file):
    with open(yaml_file, 'r') as yml:
        with open(json_file, 'a') as js:
            json.dump(yaml.load(yml), js)


# TESTING
with open("File3.json", 'w'):
    pass
json_to_yaml("File2.yaml", "File3.json")


# -------------- YAML to txt --------------#
def yaml_to_text(yaml_file, text_file):
    with open(yaml_file, 'r') as yml:
        for i in yaml.load(yml):
            with open(text_file, 'a') as txt:
                txt.write(f"{i}\n")


# TESTING
with open("File4.txt", 'w') as txt1:
    pass
yaml_to_text("File2.yaml", "File4.txt")
