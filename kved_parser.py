"""
LAB 3 TASK 1
GitHub: https://github.com/S-Daria/LAB3_TASK1.git
"""

import json


def json_decoding(path):
    with open(path, 'r', encoding='utf-8') as f:
        decoded_kved = json.load(f)
        return decoded_kved


def find_data(decoded_kved: dict, input_code_class: str):
    sections = len(decoded_kved['sections'][0])
    for sec in range(sections):
        section_name = decoded_kved['sections'][0][sec]['sectionName']
        divisions = len(decoded_kved['sections'][0][sec]['divisions'])
        for div in range(divisions):
            if decoded_kved['sections'][0][sec]['divisions'][div]['divisionCode'] == input_code_class[:2]:
                division_name = decoded_kved['sections'][0][sec]['divisions'][div]['divisionName']
                groups = len(decoded_kved['sections']
                             [0][sec]['divisions'][div]['groups'])
                for gro in range(groups):
                    if decoded_kved['sections'][0][sec]['divisions'][div]['groups'][gro]['groupCode'] == input_code_class[:4]:
                        group_name = decoded_kved['sections'][0][sec]['divisions'][div]['groups'][gro]['groupName']
                        classes = len(
                            decoded_kved['sections'][0][sec]['divisions'][div]['groups'][gro]['classes'])
                        for cla in range(classes):
                            if decoded_kved['sections'][0][sec]['divisions'][div]['groups'][gro]['classes'][cla]['classCode'] == input_code_class:
                                class_name = decoded_kved['sections'][0][sec]['divisions'][
                                    div]['groups'][gro]['classes'][cla]['className']

    return {'class_name': class_name, 'group_name': group_name, 'division_name': division_name, 'section_name': section_name, 'classes': classes, 'groups': groups, 'divisions': divisions}


def organize_data(class_name, group_name, division_name, section_name, classes, groups, divisions):
    data = {
        "name": class_name,
        "type": "class",
        "parent": {
            "name": group_name,
            "type": "group",
            "num_children": classes,
            "parent": {
                "name": division_name,
                "type": "division",
                "num_children": groups,
                "parent": {
                    "name": section_name,
                    "type": "section",
                    "num_children": divisions
                }
            }
        }
    }
    return data


def creating_json(data):
    with open('kved_results.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


input_code_class = "01.11"
def parse_kved(input_code_class: str):
    path = "kved.json"
    decoded_kved = json_decoding(path)
    raw_data = find_data(decoded_kved, input_code_class)
    data = organize_data(class_name = raw_data['class_name'], group_name = raw_data['group_name'], division_name = raw_data['division_name'], section_name = raw_data['section_name'], classes = raw_data['classes'], groups = raw_data['groups'], divisions = raw_data['divisions'])
    creating_json(data)

parse_kved(input_code_class)