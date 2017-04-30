import json


def read_from_file_as_json(track_id):
    return json.loads(open("../data_input/{}.json".format(track_id)).read())


def write_list_as_simple_csv(the_list, output_file_path):
    with open(output_file_path, "w") as text_file:
        for item in the_list:
            text_file.write(str(item) + '\n')


def write_matrix_as_csv(the_matrix, output_file_path):
    with open(output_file_path, "w") as text_file:
        for line in the_matrix:
            for col in line:
                text_file.write(str(col) + ';')
            text_file.write(str(col) + '\n')
