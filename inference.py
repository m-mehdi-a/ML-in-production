from transformers import pipeline


class infer:

    def predict(self, text, candidate_lab):

        classifier = pipeline("zero-shot-classification",
                              model="facebook/bart-large-mnli")

        pred = classifier(text, candidate_lab)
        return pred