from urllib.request import urlopen

url = "https://plato.stanford.edu/entries/plato/"
page = urlopen(url)

html_bytes = page.read()
html = html_bytes.decode("utf-8")


print(html)

