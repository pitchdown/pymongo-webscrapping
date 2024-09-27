from bs4 import BeautifulSoup
import requests
import re
import threading
import time

start = time.time()

results_lock = threading.Lock()
results = []


def scrap_recipe_page(url):
    req = requests.get(url)
    soup = BeautifulSoup(req.content, 'html.parser')

    ingredients = soup.find_all('div', class_='list__item')
    instructions = soup.find_all('div', class_='lineList__item')

    recipe_ingredients = []
    recipe_instructions = []

    for ingredient, instruction in zip(ingredients, instructions):
        ingredient_text = re.sub(r'\s+', ' ', ingredient.get_text()).replace('\u200b', '').strip()
        recipe_ingredients.append(ingredient_text)

        step = instruction.find('div', class_='count').get_text()
        instruction_text = instruction.find('p').get_text()
        recipe_instructions.append({'step': step, 'instruction': instruction_text})

    return {'ingredients': recipe_ingredients, 'instructions': recipe_instructions}


def scrap_general_page(url):
    req = requests.get(url)
    soup = BeautifulSoup(req.content, 'html.parser')
    titles = soup.find_all('a', class_='box__title', href=True)
    authors = soup.find_all('div', class_='name')
    imgs = soup.find_all('img', class_='img')

    data = []

    for title, author, img in zip(titles, authors, imgs):
        recipe_url = f'https://kulinaria.ge/{title.get("href")}'
        recipe_details = scrap_recipe_page(recipe_url)

        drink_data = {
            'title': title.get_text().strip(),
            'recipe_url': recipe_url,
            'category': {'title': 'სასმელები', 'url': 'https://kulinaria.ge/receptebi/cat/sasmelebi/'},
            'sub-category': url,
            'img': img.get('src'),
            'description': img.get('alt'),
            'author': author.get_text().strip(),
            'ingredients': recipe_details['ingredients'],
            'instructions': recipe_details['instructions'],
        }

        data.append(drink_data)

    return data


def scrap_and_store(url):
    scraped_data = scrap_general_page(url)
    with results_lock:
        results.extend(scraped_data)


urls = [
    'https://kulinaria.ge/receptebi/cat/sasmelebi/alkoholuri/',
    'https://kulinaria.ge/receptebi/cat/sasmelebi/kompoti/',
    'https://kulinaria.ge/receptebi/cat/sasmelebi/kokteili/',
    'https://kulinaria.ge/receptebi/cat/sasmelebi/limonaTi/',
    'https://kulinaria.ge/receptebi/cat/sasmelebi/milkSeiki/',
    'https://kulinaria.ge/receptebi/cat/sasmelebi/nayeni/',
    'https://kulinaria.ge/receptebi/cat/sasmelebi/smuzi/',
    'https://kulinaria.ge/receptebi/cat/sasmelebi/yava-da-Cai/'
]

threads = []

for url in urls:
    thread = threading.Thread(target=scrap_and_store, args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print(results)

end = time.time()
print(end - start)
