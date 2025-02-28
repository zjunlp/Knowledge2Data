from tqdm import tqdm
import time
from skg_utils import *
from utils.parse import parse_input_without_negative, filter_boxes, show_boxes
import json
import argparse
from prompt import prompt_boxes

parser = argparse.ArgumentParser()
parser.add_argument("--input_file", default="./data/skg.json", type=str)
parser.add_argument("--output_file", default="./data/skg_boxes.json", type=str)

args = parser.parse_args()

data = json.load(open(args.input_file, "r"))

new_data = []

for index, example in tqdm(enumerate(data), total=len(data)):
    scene = example['scene']
    objects = str(example['attributes'])
    relationship = str(example['objects_kg'])
    if example['negative_objects'] == '':
        exclusion = str([])
    else:
        exclusion = str([example['negative_objects']])
    prompt_full = prompt_boxes.format(scene=scene, objects=objects, exclusion=exclusion, relationship=relationship)

    for i in range(MAX_API_RETRY):
        try:
            output = ask_llm(prompt_full, model="gpt-4")
            gen_boxes, bg_prompt, prompt = parse_input_without_negative(output, no_input=True)
            example['resp'] = output
            new_data.append(example)
            break
        except:
            print('retry')
            time.sleep(0.5)

print("Last data:\n", new_data[-1])

with open(args.output_file, 'w') as f:
    json.dump(new_data, f, ensure_ascii=False, indent=4)