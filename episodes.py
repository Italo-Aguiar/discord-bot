import requests as req

def get(episode_link):

    site = req.get(episode_link)

    download_href = site.text.find('class="download-podcast button-default -primary"')

    i = download_href-3
    j = site.text[download_href-3]

    while j != '"':
        i -= 1
        j = site.text[i]

    download_link = ''
    for i in range(i+1, download_href-3 + 1):
        download_link += site.text[i]

    res = req.get(download_link)

    episodio = open('episodio.mp3', 'wb')
    episodio.write(res.content)
    episodio.close()

    return True