#/bin/bash

# auto-gpt
# pip install -r Auto-GPT/requirements.txt

# crfm api
# pip install crfm-helm

# ML dependencies
conda install pytorch torchvision torchaudio -c pytorch -c nvidia
pip install -r requirements.txt
pip install pyg_lib torch_scatter torch_sparse torch_cluster
pip install typing-inspect==0.8.0 typing_extensions==4.5.0
pip install pydantic -U
pip install -U jax==0.4.6
pip install -U numpy
pip install --force-reinstall charset-normalizer==3.1.0