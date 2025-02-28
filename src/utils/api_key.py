import os

# You can either set `OPENAI_API_KEY` environment variable or replace "YOUR_API_KEY" below with your OpenAI API key
if "OPENAI_API_KEY" in os.environ:
    api_key = os.environ["OPENAI_API_KEY"]
else:
    api_key = "sk-2DMUBI0MB3914wuB1c0b79De9eCb481a81677a51E0B31847"
