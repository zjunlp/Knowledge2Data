from skg_utils import *
import json
from prompt import prompt_scenes
import argparse
import os
import time

parser = argparse.ArgumentParser()
parser.add_argument("--output_file", default="./data/scenes.txt", type=str)
parser.add_argument("--num_scenes", default=1, type=int,
                    help="The number of scenes to generate")

args = parser.parse_args()

output_scenes = []

p = prompt_scenes.format(n=args.num_scenes)

for i in range(MAX_API_RETRY):
    try:
        output = ask_llm(p)
        output = eval(extract_bracket_content(output))
        output_scenes += output
        print(output)
        break
    except:
        print("retry")
        time.sleep(0.5)

with open(args.output_file, "w") as file:
    for scene in output_scenes:
        file.write(scene + "\n")
