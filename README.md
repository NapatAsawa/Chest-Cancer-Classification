# Chest-Cancer-Classification
1. conda create -n chest-cancer python=3.8 -y
2. conda activate chest-cancer
3. pip install -r requirements.txt
4. dvc init
5. dvc repro
6. bentoml serve service:svc
7. bentoml build
8. bentoml containerize chest-cancer:latest