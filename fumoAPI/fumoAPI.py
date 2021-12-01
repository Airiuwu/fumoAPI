import aiohttp, json, requests

url = 'https://fumos.live/api/fumo'

async def pickRandomFumo():
	async with aiohttp.ClientSession() as session:
		async with session.get(url) as requestFumo:
			return (await requestFumo.json())["fumo"]

def randomFumo():
	return (requests.get(url).json())["fumo"] 
