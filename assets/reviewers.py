from tqdm import tqdm
import requests
import pandas as pd
import csv

import arcas

with open('reviewers.txt', 'r') as textfile:
    names = textfile.read()
names = names.split('\n')

pbar = tqdm(total=5)
 
for p in [arcas.Springer]: 
    for author in names:
        api = p()
        switch = True
        start = 1

        while switch is not False and start < 100:
            parameters = api.parameters_fix(author=author, records=10, start=start)
            url = api.create_url_search(parameters)

            request = api.make_request(url)
            root = api.get_root(request)
            raw_article = api.parse(root)

            try:
                articles = []
                for art in raw_article:
                    articles.append(api.to_dataframe(art))


                df = pd.concat(articles, ignore_index=True)
                api.export(df, "/home/nightwing/data/reviews/{}_{}_{}.json".format(author, api.__class__.__name__, start))
            except TypeError:
                switch=False
            start += 10
    pbar.update(1)









