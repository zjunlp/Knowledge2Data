python generate_boxes.py --input_file ./data/skg.json &&
CUDA_VISIBLE_DEVICES=0 python generate_images.py --prompt-type demo --model gpt-4 --save-suffix "auto" --repeats 1 --frozen_step_ratio 0.5 --regenerate 1 --force_run_ind 0 --run-model lmd_plus --no-scale-boxes-default --template_version v0.1  --sdxl --sdxl-step-ratio 0.5  &&
python generate_qa.py &&
python check_qa.py