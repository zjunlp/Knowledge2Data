from skg_utils import *
import json
import time
from tqdm import tqdm
import collections
import random
import argparse
from prompt import prompt_nodes, prompt_node, prompt_triplets

parser = argparse.ArgumentParser()
parser.add_argument("--input_file", default="./data/objects.json", type=str)
parser.add_argument("--output_file", default="./data/skg.json", type=str)
parser.add_argument("--add_one_node", action="store_true", help="Add data with only one object present")

args = parser.parse_args()

data = json.load(open(args.input_file, "r"))

new_data = []

for index, example in tqdm(enumerate(data), total=len(data)):
    objects = ", ".join(example["objects"])
    scene = example["scene"]
    p1 = prompt_nodes.format(objects=objects, scene=scene)

    output_lst = []
    for i in range(MAX_API_RETRY):
        try:
            output = ask_llm(p1)
            output = extract_special_bracket_content(output)
            output_lst += eval(output)
            break
        except:
            print("nodes retry")
            time.sleep(0.5)

    all_objects = []

    for tmp in output_lst:
        tmp_dict = {}
        tmp_dict["scene"] = scene
        chosen_objects = list(set(tmp["chosen_objects"]))
        tmp_dict["chosen_objects"] = chosen_objects
        tmp_dict["attributes"] = tmp["attributes"]

        negative_objects = list(set(example["objects"]) - set(chosen_objects))
        tmp_dict["negative_objects"] = random.choice(negative_objects)

        all_objects += chosen_objects

        p3 = prompt_triplets.format(attributes=str(tmp["attributes"]), scene=scene)
        tmp_lst = []

        for i in range(MAX_API_RETRY):
            try:
                output = ask_llm(p3)
                output = extract_two_brackets_content(output)
                tmp_lst += eval(output)
                break
            except:
                print("triplets retry")
                time.sleep(0.5)

        if len(tmp_lst) != 0:
            tmp_dict["objects_kg"] = tmp_lst
            new_data.append(tmp_dict)

    if args.add_one_node:
        all_objects = collections.Counter(all_objects).most_common(3)
        all_objects = [item[0] for item in all_objects]

        for item in all_objects:
            p2 = prompt_node.format(input=item, scene=scene)
            tmp_lst = []

            for i in range(MAX_API_RETRY):
                try:
                    output = ask_llm(p2, "")
                    output = extract_bracket_content(output)
                    tmp_lst += eval(output)
                    break
                except:
                    print("node retry")
                    time.sleep(0.5)

            for object_attributes in tmp_lst:
                tmp_dict = {}
                tmp_dict["scene"] = scene
                tmp_dict["chosen_objects"] = [item]
                tmp_dict["attributes"] = object_attributes
                tmp_dict["negative_objects"] = ""
                tmp_dict["objects_kg"] = []
                new_data.append(tmp_dict)

print("Last data:\n", new_data[-1])

with open(args.output_file, "w") as f:
    json.dump(new_data, f, ensure_ascii=False, indent=4)
