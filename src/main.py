import json


def load_tax_data(filepath):
    with open(filepath, "r") as config:
        return json.load(config)


def main():
    pass


main()
