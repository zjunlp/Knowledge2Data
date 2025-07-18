<div align="center">
<h1 align="center"> 👉 Knowledge2Data 👈 </h1>
<b>Spatial Knowledge Graph-Guided Multimodal Synthesis</b>

[![Awesome](https://awesome.re/badge.svg)](https://github.com/zjunlp/Knowledge2Data) 
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

<div align="center">
<img src="figs/figure1.gif" width="90%">
</div>

<p align="center">
  <a href="https://github.com/zjunlp/Knowledge2Data">Project</a> •
  <a href=https://arxiv.org/abs/2505.22633>Paper</a> •
  <a href="https://huggingface.co/datasets/zjunlp/Knowledge2Data">HuggingFace</a> •
  <a href="#overview">Overview</a> •
  <a href="#quickstart">Quickstart</a> •
  <a href="#citation">Citation</a>
</p>

</div>

## Table of Contents

- <a href="#news">What's New</a> •
- <a href="#overview">Overview</a> •
- <a href="#quickstart">Quickstart</a> •
- <a href="#citation">Citation</a>

## 🔔News
- **2025-02-28, We release the paper.**
---

## 🌟Overview
<div align="center">
<img src="figs/figure2.png" width="90%">
</div>


## ⏩Quickstart
### Data
Get training data and test data from HuggingFace: https://huggingface.co/datasets/zjunlp/Knowledge2Data
### Installation
```
git clone https://github.com/zjunlp/Knowledge2Data
cd Knowledge2Data
conda create -n skg python==3.9
conda activate skg
pip install -r requirements.txt
```

### Download the models
#### Download the following models from HuggingFace

| 🎯 Model Name                 | 🤗 HuggingFace                                                            |
|-------------------------------|---------------------------------------------------------------------------|
| Diffusers-generation-text-box | [gligen/diffusers-generation-text-box](https://huggingface.co/gligen/diffusers-generation-text-box) |
| Sam-vit-base                  | [stabilityai/stable-diffusion-xl-refiner-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-refiner-1.0)       |
| Stable-diffusion-xl-refiner   | [facebook/sam-vit-base](https://huggingface.co/facebook/sam-vit-base)      |

### Export the environment variables.
```shell
cd src
export OPENAI_API_KEY="YOUR_API_KEY"
export SKG_HF_MODELS="LOCAL_HUGGINGFACE_MODELS_DIR"
```
### Generate Spatial KG and multimodal synthetic data.
#### Execute script to generate Spatial KG.
```shell
sh run_skg.sh
```
You can also customize objects and their spatial relationships to form Spatial KG. Save the file format as a JSON file similar to "src/data/skg_demo.json".
#### Execute script to multimodal synthetic data.
```shell
sh run_data.sh
```
For custom data, only the input file parameters "--input_file" need to be modified.

You can find generated data in "src/data" and images in "src/img_generations" as default.
If you want to generate more data, you can modify the parameters including "--num_scenes" ([generate_scenes.py](src%2Fgenerate_scenes.py)) and "--repeats" ([generate_images.py](src%2Fgenerate_images.py)).

## 🌻Acknowledgement

This project is based on open-source projects including [LLM-groundedDiffusion](https://github.com/TonyLianLong/LLM-groundedDiffusion). Thanks for their great contributions!

### 🚩Citation

Please cite the following paper if you use this project in your work.

```bibtex
@misc{xue2025spatialknowledgegraphguidedmultimodal,
      title={Spatial Knowledge Graph-Guided Multimodal Synthesis}, 
      author={Yida Xue and Zhen Bi and Jinnan Yang and Jungang Lou and Huajun Chen and Ningyu Zhang},
      year={2025},
      eprint={2505.22633},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2505.22633}, 
}
```

---
