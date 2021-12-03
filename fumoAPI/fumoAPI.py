from aiohttp import ClientSession
from requests import get

url = 'https://fumos.live/api/fumo'

async def pickRandomFumo():
	async with ClientSession() as session:
		async with session.get(url) as requestFumo:
			fumo = await requestFumo.json()
			return fumo["fumo"]

def randomFumo():
	requestFumo = get(url)
	fumo = requestFumo.json()
	return fumo["fumo"]
