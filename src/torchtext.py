import torch
from torchtext import data

SEED = 1234

torch.manual_seed(SEED)
torch.backends.cudnn.deterministic = True

TEXT = data.Field(tokenize = 'spacy')
LABEL = data.LabelField(dtype = torch.float)

from torchtext import datasets
train_data, test_data = datasets.IMDB.splits(TEXT, LABEL)

fields = {'text': ('t', TEXT), 'label': ('l', LABEL)}
train_data, test_data = data.TabularDataset.splits(
                                        path = '../data',
                                        train = 'news.csv',
                                        test = 'news.csv',
                                        format = 'csv',
                                        fields = fields,
                                        skip_header = True
)

import pandas
df = pd.read_csv("../data/news.csv")

df = df.drop(['Unnamed: 0'], axis = 1)
df = df.drop(['title'], axis = 1)

df.to_json('news.json')


train_data, test_data = data.TabularDataset.splits(
                            path = '.',
                            train = 'news.json',
                            test = 'news.json',
                            format = 'json',
                            fields = fields
)
