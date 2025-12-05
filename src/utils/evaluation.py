"""Evaluation utilities (accuracy, F1, topic coherence helpers)."""

def accuracy(preds, labels):
    return sum(p==l for p,l in zip(preds, labels))/len(labels)
