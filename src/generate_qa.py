from skg_utils import *
import json
from copy import deepcopy
from tqdm import tqdm
import time
from utils.parse import parse_input_without_negative
import argparse
from prompt import prompt_qa

parser = argparse.ArgumentParser()
parser.add_argument("--input_file", default="./data/skg_images.json", type=str)
parser.add_argument("--output_file", default="./data/data.json", type=str)
args = parser.parse_args()

data = json.load(open(args.input_file, 'r'))
new_data = []

for index, example in tqdm(enumerate(data), total=len(data)):
    objects = str(example['attributes'])
    relationships = str(example['objects_kg'])
    gen_boxes, _, _ = parse_input_without_negative(example['resp'], no_input=True)
    gen_boxes = str(gen_boxes)
    negative_objects = str(example['negative_objects'])

    if 'png' not in example['img']:
        dir_path = example['img']
        example['img'] = [os.path.join(dir_path, img) for img in os.listdir(example['img']) if img.startswith("img")]
    else:
        example['img'] = [example['img']]

    new_img = deepcopy(example['img'])

    img_flag = False

    for image_path in example['img']:
        base64_image = encode_image(image_path)
        p = prompt_qa.format(objects=objects, relationships=relationships, boxes=gen_boxes,
                             negative_objects=negative_objects)
        for i in range(MAX_API_RETRY):
            try:
                output = ask_llm(p, base64_image)
                print(output)

                if 'yes' not in output.lower():
                    new_img.remove(image_path)
                else:
                    output = extract_bracket_content(output)
                    output_lst = eval(output)
                    example['qa'] = output_lst
                    flag = True
                break
            except:
                print('retry')
                time.sleep(0.5)

        if img_flag:
            example['img'] = new_img[0]
            new_data.append(example)
            break

print("Last data:\n", new_data[-1])

with open(args.output_file, 'w') as f:
    json.dump(new_data, f, ensure_ascii=False, indent=4)
