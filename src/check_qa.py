from skg_utils import *
import json
from copy import deepcopy
from tqdm import tqdm
import time
import argparse
from prompt import prompt_check

parser = argparse.ArgumentParser()
parser.add_argument("--input_file", default="./data/data.json", type=str)
parser.add_argument("--output_file", default="./data/data_filtered.json", type=str)

args = parser.parse_args()

data = json.load(open(args.input_file, 'r'))

new_data = []

MAX_API_RETRY = 5

for index, example in tqdm(enumerate(data), total=len(data)):
    if 'options' in example['qa'][0]:
        new_qa = []
        for j in range(len(example['qa'])):
            d = example['qa'][j]
            d['question'] = d['question'] + '\n' + d['options']
            del d['options']
            new_qa.append(d)
        example['qa'] = new_qa
    qa = str(example['qa'])

    image_path = example['img']

    base64_image = encode_image(image_path)
    p = prompt_check.format(qa=qa)
    for i in range(MAX_API_RETRY):
        try:
            output = ask_llm(p, base64_image)
            output = extract_bracket_content(output)
            output_lst = eval(output)
            example['qa'] = output_lst
            new_data.append(example)
            break
        except:
            print('retry')
            time.sleep(0.5)

print("Last data:\n", new_data[-1])

with open(args.output_file, 'w') as f:
    json.dump(new_data, f, ensure_ascii=False, indent=4)
