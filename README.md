# bristol-ai-text-cwk
EMATM0067 Task 5 group coursework - Bristol MSc Data Science 2026

# EMATM0067 Task 5 - Neural Network Image Description

MSc Data Science group coursework, University of Bristol, 2026.

## Task
Build a neural network to describe simple pictures of shape arrangements.
Given an image of two shapes, the model predicts a sentence describing the scene
(e.g. "a large blue sphere is above a small red cube").

## Team
| Person | Role |
|--------|------|
| Chirag | Sentence dataset generation |
| Junyao | Image generation pipeline |
| Yisheng | Text representation & preprocessing |
| Nikunj | CNN model development, architecture experimentation & hyperparameter tuning |
| Joe | Evaluation, experiments & LLM comparison |
| Vikunj | Report writing |

## Responsibilities
- **Chirag** - sentence templates, vocabulary definition, dataset generation script
- **Junyao** - image generation script, shape rendering, paired image-label dataset
- **Yisheng** - tokenisation, vocabulary creation, one-hot/embedding encoding, text label preparation
- **Nikunj** - CNN implementation, model training, architecture variants, hyperparameter tuning, training logs
- **Joe** - performance metrics, experiment comparison, results plots/tables, error analysis, LLM comparison
- **Vikunj & Joe** - group report writing

## Repo Structure
| Folder | Contents |
|--------|----------|
| /data | Datasets (sentences, images, train/val/test splits) |
| /src/dataset | Sentence and image generation scripts |
| /src/models | CNN model code |
| /src/evaluation | Evaluation and experiment scripts |
| /notebooks | Exploratory analysis notebooks |
| /results | Output plots, tables, logs |

## Deadline
13:00, Tuesday 5th May 2026
