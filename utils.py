import json


class Utils:

    @staticmethod
    def write_json_to_file(file_name, data):
        json_object = json.dumps(data, indent=4)
        with open(file_name, "w") as out_file:
            out_file.write(json_object)

    @staticmethod
    def encode_decode_string(str_to_encode):

        pass
