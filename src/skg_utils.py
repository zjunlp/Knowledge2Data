from openai import OpenAI
import base64
import os
import re

MAX_API_RETRY = 3


def extract_special_bracket_content(input_string):
    match = re.search(r"\[.*\]", input_string, re.DOTALL)
    if match:
        return match.group(0)
    return None


def extract_bracket_content(text):
    matches = re.findall(r"\[.*?\]", text, re.DOTALL)
    return "".join(matches).strip()


def extract_two_brackets_content(text):
    matches = re.findall(r"\[\[.*?\]\]", text, re.DOTALL)
    return "".join(matches).strip()


def extract_dict_content(text):
    matches = re.findall(r"\{.*?\}", text, re.DOTALL)
    return "".join(matches).strip()


def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")


def ask_llm(prompt, base64_image="", model="gpt-4o"):
    client = OpenAI()
    if base64_image != "":
        resp = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "user", "content": [
                    {"type": "text", "text": prompt},
                    {"type": "image_url", "image_url": {
                        "url": f"data:image/png;base64,{base64_image}"}
                     }
                ]}
            ],
        )
    else:
        resp = client.chat.completions.create(
            model=model,
            messages=[{"role": "user",
                       "content": prompt}
                      ],
        )
    answer = resp.choices[0].message.content
    return answer.strip()
