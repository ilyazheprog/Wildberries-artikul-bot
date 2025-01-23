import httpx
from modules.envs.settings import settings


async def get_product_details(artikul: int):
    """Get product details from Wildberries"""
    url = f"{settings.wildberries.get_details_url}{artikul}"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        return response.json()