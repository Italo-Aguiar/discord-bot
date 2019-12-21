import requests as req

jovemNerdSite = req.get('https://jovemnerd.com.br/nerdcast/pequenos-prazeres-2/')

print(jovemNerdSite.text)
