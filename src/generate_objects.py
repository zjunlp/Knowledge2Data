from skg_utils import *
import json
import time
from tqdm import tqdm
import argparse
from prompt import prompt_objects

parser = argparse.ArgumentParser()
parser.add_argument("--input_file", default="./data/scenes.txt", type=str)
parser.add_argument("--rag_file", default="", type=str)
parser.add_argument("--output_file", default="./data/objects.json", type=str)

args = parser.parse_args()

rag = {}
if args.rag_file != "":
    with open(args.rag_file, "r") as f:
        rag = json.load(f)

with open(args.input_file, "r") as file:
    lines = file.readlines()

new_data = []

for scene in tqdm(lines, total=len(lines)):
    scene = scene.strip()
    p = prompt_objects.format(scene=scene)
    if scene in rag.keys():
        p = rag[scene] + "\n" + p

    for i in range(MAX_API_RETRY):
        try:
            output = ask_llm(p)
            output = eval(extract_bracket_content(output))
            tmp_dict = {}
            tmp_dict["scene"] = scene
            tmp_dict["objects"] = output
            new_data.append(tmp_dict)
            break
        except:
            print("retry")
            time.sleep(0.5)

print("Last data:\n", new_data[-1])

with open(args.output_file, "w") as f:
    json.dump(new_data, f, ensure_ascii=False, indent=4)
