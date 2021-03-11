import asyncio
import aiohttp
import requests
import json
import time
import nest_asyncio
nest_asyncio.apply()

def download_images():
    response = requests.get("https://picsum.photos/v2/list")
    if response.status_code != 200:
        raise AttributeError('GET /tasks/ {}'.format(response.status_code))
    data = json.loads(response.text)

    pictures=[]
    for s in data:
        pictures.append(s['download_url']+".jpg")
    return pictures

async def download_images_asyncio(link, session):
    filename = link.split('/')[6].split('.')[0]
    fileformat = link.split('/')[6].split('.')[1]
    async with session.get(link) as response:
        with open("downloads/{}.{}".format(filename, fileformat), 'wb') as fd:
            async for data in response.content.iter_chunked(1024):
                fd.write(data)

async def main_asyncio():
    images = download_images()

    async with aiohttp.ClientSession() as session:
        tasks=[download_images_asyncio(image,session)for image in images]
        return await asyncio.gather(*tasks)

start_time = time.time()
asyncio.run(main_asyncio())
duration_asyncio = time.time() - start_time
print(f"Time taken to download 30 images into the downloads folder with asyncio: {duration_asyncio}")