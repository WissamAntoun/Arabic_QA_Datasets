#%%
import json
import re
from tqdm import tqdm

# %%
tydiqa_train_path = './data/tydiqa-goldp-v1.1-train.json'

with open(tydiqa_train_path, "r", encoding='utf-8') as reader:
    input_data = json.load(reader)["data"]
#%%
arabic_data = []
for entry in tqdm(input_data):
    for paragraph in entry["paragraphs"]:
        if 'arabic' in paragraph['qas'][0]['id']:
            arabic_data.append(
                {
                    'paragraphs' : [paragraph],
                    'title' : entry['title']
                }
            )

print(len(arabic_data))
 # %%
arabic_data = {
    "data": arabic_data,
    "version": "TyDiQA-GoldP-1.1-for-SQuAD-1.1",
    'lang' : 'ar'
}
# %%
with open('./data/tydiqa-goldp-v1.1-train-ar.json', "w",encoding='utf-8') as writer:
    json.dump(arabic_data, writer)
# %%
