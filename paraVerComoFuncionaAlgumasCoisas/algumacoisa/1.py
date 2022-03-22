import urllib.parse
import urllib.request


url = 'https://www.linguee.com.br/portugues-ingles/search?source=auto&query=casa'
with urllib.request.urlopen(url) as response: 
    
    content = response.read()

print(content)