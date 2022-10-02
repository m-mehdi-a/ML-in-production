# ML-in-production

In this project, I use pre-trained models from [Hugging Face](https://huggingface.co/) and demonstrate how we can use a model prediction in real time. 

For this specific demo, I use the text classification model from Facebook [here](https://huggingface.co/facebook/bart-large-mnli). 

First, I create a docker image from the model using ```Dockerfile``` and with:

```
docker build -t ml-api -f Dockerfile .
```

Then, I run a container from the generated image using:

```
docker run -it -p 5000:5000 ml-api python3 api.py
```
which runs the container on port 5000 from localhost. I demo the result in ```demo.ipynb``` noteboook.

More precisely, you can send your requests to the model using a dictionary. e.g., 

```
{
    "text": "I love to play football every day",
    "candidate_labels": ["news", "sport", "travel"]
 }
```

and the result returned from the model is

```
{'labels': ['sport', 'news', 'travel'], 'scores': [0.9904438257217407, 0.00824122503399849, 0.001314967987127602], 'sequence': 'I love to play football every day'}
```


