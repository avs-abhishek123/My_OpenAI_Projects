import os
import openai
import json

openai.api_key = "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"
json_dict = openai.Model.list()
with open("info/models/openAI_models.json", "w") as outfile:
    json.dump(json_dict, outfile, indent=4, sort_keys=True)