DEFAULT_SO_NEGATIVE_PROMPT = "artifacts, blurry, smooth texture, bad quality, distortions, unrealistic, distorted image, bad proportions, duplicate, two, many, group, occlusion, occluded, side, border, collate"
DEFAULT_OVERALL_NEGATIVE_PROMPT = "artifacts, blurry, smooth texture, bad quality, distortions, unrealistic, distorted image, bad proportions, duplicate"

prompt_scenes = """You are an AI assistant specializing in imagining the scenes depicted in photos. Your task is to envision a variety of scenes that may appear in different photos.  
Your response needs to meet the following requirements:  
1. Ensure that every scene is safe, accessible to most people, and common in real and daily life scenes.
2. The scenes in the photos should be diverse and non repetitive. Each generated scene typically depicts a facility (usually requiring interaction with multiple objects such as a table or furniture) or a room, or a place or area.

Please directly output the generated scenes in the following list format:
['dining table', 'sky', 'street', 'zoo', 'living room', 'sofa', 'desk', 'office table', 'river bank', 'wooden bench']

Now, please generate {n} different scenes.
"""

prompt_objects = """You are an AI assistant specializing in identifying objects likely to appear in a given scene. Your task is to list as many objects as possible that may be found in that scene. 
Your response needs to meet the following requirements:
1. Ensure that each object is based on common situations in reality and daily life. Ensure that objects are relatively simple and easy to draw, and once you see their images, you can determine what objects they are. Ensure that the object is safe and harmless.
2. The objects provided should not be duplicated or too similar. Try to describe an object with one word. If there are words with multiple meanings, it is necessary to ensure that they are distinguishable, such as "animal mouse" and "computer mouse".
3. Each scene needs to list as many objects as possible. If there may be people on site, please add 'person'.

Here I will give you some examples for reference and use the following template in the format of a list for the response:

Scene: dining table  
Objects: ['cup', 'wine glass', 'bowl', 'fork', 'knife', 'cake', 'table']

Scene: street  
Objects: ['person', 'car', 'bicycle', 'stop sign', 'traffic light']

Scene: {scene}  
Objects:
"""

prompt_node = """
You are an AI assistant specializing in describing the object in a given scene. Your task is to generate multiple sets of different descriptions for a given object.

Your response should meet the following requirements:
1. Be careful not to describe object that do not exist in the real world or are unsuitable for the current scene. Try to minimize the appearance of other objects in the description.
2. For some highly abstract objects, they can be described in more detail, such as identifying a person as a man or a woman. For some objects that are difficult to distinguish in the picture, there is no need to specifically describe their species, such as flower, grass, etc.
3. Try to minimize abstract descriptions such as size, length, height, etc. The state of the described object should not be too complex, and there should not be too many overly subtle details to avoid including details that cannot be visualized in the image. Do not use quantity and positional relationships with other objects as descriptions, and try to minimize the use of other objects in the description.
4. Each description needs to have diversity to avoid being too similar. For some objects that are difficult to describe, the number of times they are generated can be reduced, such as clouds, grass, the sun, and so on.
5. You need to choose one or more of the following aspects to describe the object: Orientation and Direction, State and Condition, Color and Appearance, Structural and Physical Characteristics, Viewpoint and Perspective.

Here I will give you some demonstrations for reference and use the following list template for the response:

Scene: grass
Input: rabbit
Output: [{{0: 'a rabbit facing right'}}, {{0: 'a rabbit facing left'}}]

Scene: grass
Input: flower
Output: [{{0: 'a blue flowers'}}, {{0: 'a white flowers'}}, {{0: 'flowers seen from above'}}, {{0: 'flowers seen from the side'}}]

Scene: table
Input: apple
Output: [{{0: 'a apple cut in half'}}, {{0: 'a uncut apple'}}]

Scene: street
Input: person
Output: [{{0: 'a woman in blue'}}, {{0: 'a man in white looks to the right'}}]

Scene: street
Input: car
Output: [{{0: 'a red car with open doors'}}, {{0: 'a red car with its doors closed'}}, {{0: 'a car with a protruding front'}}, {{0: 'a car without protruding front'}}]

Scene: office
Input: table
Output: [{{0: 'a top-down view of an empty wooden table'}}, {{0: 'a side view of an empty wooden table'}}]

Scene: {scene}
Input: {input}
Output: 
"""

prompt_nodes = """You are an AI assistant specializing in describing objects in a given scene. Your task is to first select a subset of candidate objects, and then describe the attributes of the selected objects.
Your response should meet the following requirements:
1. Select 2 to 4 suitable objects from the given objects to form a possible combination. Note that for some candidate objects that are suitable for repeated appearance, they can be selected repeatedly. Please prioritize selecting more common objects. Do not choose objects that are difficult to represent or recognize in the image.
2. Provide further attribute descriptions for the selected objects, including color, orientation, etc., and describe countable objects as singular. Be careful not to describe objects that do not exist in the real world or are unsuitable for the current scene. The description of each object should be concise, without being overly complex and abstract, and avoid including details that cannot be visualized in the image. For some objects that are difficult to add descriptions, additional descriptions can be omitted.
3. The selected combination of objects can be repeated, but the described attributes need to be different.
4. If there are words with multiple meanings, it is necessary to ensure that they are distinguishable and you need to determine which one is more likely based on the scene and other objects, such as 'animal mouse' and 'computer mouse'.
5. You need to provide 20 to 50 possible combinations based on the number of objects given.

Here I will give you some demonstrations for reference and use the following list template for the response:

Scene: street
Objects: person, car, bicycle, stop sign, traffic light, bus, truck
Output: 
[
{{'chosen_objects': ['person', 'person','person', 'traffic light'], 'attributes': {{0: 'a woman in blue', 1: 'a man in white', 2: 'a man in green', 3: 'a traffic light'}}}},
{{'chosen_objects': ['person', 'car', 'bicycle'], 'attributes': {{0: 'a man in white looks to the right', 1: 'a black car', 2: 'a bicycle'}}}},
{{'chosen_objects': ['stop sign', 'traffic light', 'bus'], 'attributes': {{0: 'a stop sign', 1: 'traffic light', 2: 'a blue bus'}}}},
{{'chosen_objects': ['bicycle', 'car', 'bus'], 'attributes': {{0: 'a blue bicycle', 1: 'a green car', 2: 'a green bus'}}}}
]

Scene: park
Objects: person, cat, dog, grass 
Output: 
[
{{'chosen_objects': ['cat', 'cat', 'dog', 'grass'], 'attributes': {{0: 'a black cat facing left', 1: 'a blue cat', 2: 'a orange dog', 3:'grass'}}}},
{{'chosen_objects': ['person', 'cat'], 'attributes': {{0: 'a man in green looks to the left', 1: 'a black cat'}}}}
]

Scene: {scene}
Objects: {objects}
Output: 
"""

prompt_triplets = """You are an AI assistant specializing in describing the positional relationship between objects in a scene. Your task is to describe the positional relationship of the given objects.
Your response needs to meet the following requirements:
1. Be careful not to describe positional relationships that do not exist in the real world. When describing the positional relationship between two objects, do not involve other objects. At most one positional relationship triplet is generated between every two objects.
2. There may be two types of positional relationships between two objects: directional relationships and distance relationships. Directional relationships include above, below, left, right, in front of, behind, etc. Distance relationships include close, far, near, etc. Separate two positional relationships with commas when generating them simultaneously. For situations with a small number of objects, prioritize generating directional relationships.

Here I will give you some demonstrations for reference and use the following template in the format of a list for the response:

Scene: street
Objects: {{0: 'a woman in blue', 1: 'a man in white', 2: 'a black car', 3: 'a bicycle', 4: 'a stop sign', 5: 'a traffic light'}}
Output: [[0, 'on the left of, beside', 1], [0, 'on the right of, far', 2], [2, 'on the right of', 4]]

Scene: restaurant
Objects: {{0: 'a cup', 1: 'a bowl', 2: 'a wooden table'}}
Output: [[0, 'on', 2], [1, 'below', 2]]

Scene: park
Objects: {{0: 'a black cat', 1: 'a black cat', 2: 'a orange dog', 3:'grass'}}
Output: [[0, 'on the left of', 2], [1, 'on the right of', 2], [0, 'on', 3], [1, 'on', 3], [2, 'on', 3]]

Scene: {scene}
Objects: {attributes}
Output: 
"""

prompt_boxes = """You are an intelligent bounding box generator. I will provide you with the scene, objects and their spatial relationships in a photo. Your task is to generate the bounding boxes for the given objects, along with a background prompt describing the scene and a prompt describing the photo. The images are of size 512x512. The top-left corner has coordinate [0, 0]. The bottom-right corner has coordinnate [512, 512]. The bounding boxes should not overlap or go beyond the image boundaries. Each bounding box should be in the format of (object name, [top-left x coordinate, top-left y coordinate, box width, box height]) and should not include more than one object. Do not put objects that are already provided in the bounding boxes into the background prompt. Do not include non-existing or excluded objects in the background prompt.
Use "A realistic scene" as the background prompt if no background is given in the prompt. There may be multiple spatial relationships between objects, and special attention should be paid to using bounding boxes to represent these spatial relationshipss.

Please refer to the example below for the desired format.

Scene: street
Input objects: {{0: 'a green car', 1: 'a blue truck', 2: 'a red air balloon', 3: 'a bird'}}
Input spatial relationships: [['0', 'on the left of', '1']]
Excluded objects: []
Objects: [('a green car', [21, 281, 211, 159]), ('a blue truck', [269, 283, 209, 160]), ('a red air balloon', [66, 8, 145, 135]), ('a bird', [296, 42, 143, 100])]
Background prompt: A realistic office scene
Prompt: A realistic image of office scene depicting a green car parking on the left of a blue truck, with a red air balloon and a bird in the sky

Scene: street
Input objects: {{0: 'a green car', 1: 'a blue truck', 2: 'a red air balloon', 3: 'a bird'}}
Input spatial relationships: [['0', 'on the right of', '1']]
Excluded objects: ['cat']
Objects: [('a blue truck', [21, 281, 211, 159]), ('a green car', [269, 283, 209, 160]), ('a red air balloon', [66, 8, 145, 135]), ('a bird', [296, 42, 143, 100])]
Background prompt: A realistic street scene
Prompt: A realistic image of office scene depicting a green car parking on the right of a blue truck, with a red air balloon and a bird in the sky, without cats

Scene: table
Input objects: {{0: 'a wooden table', 1: 'an apple', 2: 'an apple'}}
Input spatial relationships: [['1', 'on', '0'], ['2', 'on', '0']]
Excluded objects: ['banana']
Objects: [('a wooden table', [20, 148, 472, 216]), ('an apple', [150, 226, 100, 100]), ('an apple', [280, 226, 100, 100])]
Background prompt: A realistic table scene
Prompt: A realistic image of a wooden table with two apples on it, without bananas

Scene: living room
Input objects: {{0: 'a painting', 1: 'a cabinet', 2: 'a flower vase', 3: 'a flower vase'}}
Input spatial relationships: [['1', 'below', '0'], ['2', 'near', '3'], ['2', 'on', '1'], ['3', 'on', '1']]
Excluded objects: []
Objects: [('a painting', [88, 85, 335, 203]), ('a cabinet', [57, 308, 404, 201]), ('a flower vase', [166, 222, 92, 108]), ('a flower vase', [328, 222, 92, 108])]
Background prompt: A realistic living room scene
Prompt: A realistic image of a living room. there are a painting mounted on the wall, a cabinet below the painting, and two flower vases on the cabinet

Scene: park
Input objects: {{0: 'a black cat', 1: 'a black cat', 2: 'a orange dog'}}
Input spatial relationships: [[0, 'on the left of, far', 2], [1, 'on the right of, near', 2]]
Excluded objects: ['bird', 'person']
Objects: [('a black cat', [22, 266, 90, 115]), ('a black cat', [277, 272, 120, 115]), ('an orange dog', [198, 288, 150, 150])]
Background prompt: A realistic park scene
Prompt: A realistic image depicting two black cat and an orange dog without birds and persons

Scene: {scene}
Input objects: {objects}
Input spatial relationships: {relationship}
Excluded objects: {exclusion}
Objects: 
"""

prompt_qa = """
You are an AI assistant specializing in evaluating the quality of a given image and generating question and answer pairs related to the image. Your task is to first determine whether the given image should be saved based on its quality and whether it matches the descriptions, and then continue generating question and answer pairs if it is determined to be saved.
Descriptions of the image will provide information about the objects present in the image, their quantity, their attributes, their positional relationships, their bounding boxes (object name, [top-left x coordinate, top-left y coordinate, box width, box height]), and objects that are absent from the image.

You need to follow the steps below to complete the task:
Step 1. You need to ensure the clarity, quality, and authenticity of the image. You need to verify if there are any unrealistic or unreasonable parts in this image, such as clearly unrealistic looking humans or animals, and if there are any indistinguishable objects.
Step 2. You need to ensure that the image contains the specified objects and does not contain any excluded objects. Specified objects are given in the form of dict, and excluded objects are presented in a list format. Please note that the image should accurately reflect the attributes of the specified object, such as Orientation and Direction, State and Condition, Color and Appearance, Structural and Physical Characteristics, Viewpoint and Perspective.
Step 3. You need to ensure that the objects in the image have a positional relationship with the matching descriptions. The positional relationships are given in the form of a list, and the objects correspond to the dict.
Step 4. If the image matches step 1 and basically matches steps 2 and 3, please answer 'Yes' and proceed to the next steps to generate question answer pairs. Otherwise, please answer 'No' and do not proceed to the next steps.
Step 5. You need to generate as many question answer pairs as possible based on the correct parts of these descriptions and information that can be confidently determined in the given image, while ensuring quality and diversity.
For Step 5, the following requirements must be met:
1. Please note not to mention any information related to the image descriptions in your question-answer pairs, as the image description will not be provided in future tasks using these question-answer pairs.
2. Please note that due to the possibility of objects not mentioned in the image descriptions and incomplete matching between the image and descriptions, you need to carefully examine the image to ensure that each question and answer pair is generated with sufficient confidence.
3. The question-answer pairs can include questions about the existence of objects, the quantity of objects, the attributes of objects, the approximate position of objects in the image layout (Where are the objects in the image located throughout the entire image, such as the center, top, bottom, left, and right sides of the image), the positional relationships between objects (Choose a specific object as a reference, which object is closer or farther away from the reference relative to another object, which objects are on the left or right side of the reference, etc.), and reasoning (The position, orientation, etc. of an object that matches specific attributes among multiple objects). Generate as many question answer pairs as possible for each of the above types.
4. Use the template in the format of a JSON list to generate question and answer pairs without any other information.

Below are reference responses for saving and not saving this image:

Yes. Question and answer pairs:
[
    {{
        "question": "[your question]",
        "answer": "[your answer]",
    }},
    {{
        "question": "[your question]",
        "answer": "[your answer]",
    }}
]

Below are reference responses for not saving this image:

No.

Here is the image and corresponding descriptions. Please provide your response.
Objects: {objects}
Positional relationships: {relationships}
Bounding boxes: {boxes}
Excluded objects: {negative_objects}
"""

prompt_check = """
You are an AI assistant specializing in reviewing question-answer pairs about a given image. Your task is to find the correct question-answer pairs based on the given image.

Your response needs to meet the following requirements:
1. You need to determine whether the answers to the questions are correct based on the given images, and save the correct question-answer pairs.
2. Use a JSON list format template with the same format as the input to generate correct question-answer pairs without generating any additional information.

Here is the question and answer about the given image:

Question-answer pairs: {qa}
Correct question-answer pairs:
"""

prompt_types = [
    "demo",
    "lmd_negation",
    "lmd_numeracy",
    "lmd_attribution",
    "lmd_spatial",
    "lmd",
]
templates = {"v0.1": prompt_boxes}
template_versions = ["v0.1"]

stop = "\n\n"
prompts_demo_gpt4, prompts_demo_gpt3_5 = [], []


def get_prompts(prompt_type, model, allow_non_exist=False):
    """
    This function returns the text prompts according to the requested `prompt_type` and `model`. Set `model` to "all" to return all the text prompts in the current type. Otherwise we may want to have different prompts for gpt-3.5 and gpt-4 to prevent confusion.
    """
    prompts_gpt4, prompts_gpt3_5 = {}, {}
    if prompt_type.startswith("lmd"):
        from utils.eval.lmd import get_lmd_prompts

        prompts = get_lmd_prompts()

        # We do not add to both dict to prevent duplicates when model is set to "all".
        if "gpt-4" in model:
            prompts_gpt4.update(prompts)
        else:
            prompts_gpt3_5.update(prompts)
    elif prompt_type == "demo":
        prompts_gpt4["demo"] = prompts_demo_gpt4
        prompts_gpt3_5["demo"] = prompts_demo_gpt3_5

    if "all" in model:
        return prompts_gpt4.get(prompt_type, []) + prompts_gpt3_5.get(prompt_type, [])
    elif "gpt-4" in model:
        if allow_non_exist:
            return prompts_gpt4.get(prompt_type, [])
        return prompts_gpt4[prompt_type]
    else:
        # Default: gpt-3.5
        if allow_non_exist:
            return prompts_gpt3_5.get(prompt_type, [])
        return prompts_gpt3_5[prompt_type]
