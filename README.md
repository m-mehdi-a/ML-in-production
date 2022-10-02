# ML-in-production

In this project, I use pre-trained models from Hugging Face and demonstrate how we can use a model prediction in real time. 

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
