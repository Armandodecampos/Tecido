import asyncio
from playwright.async_api import async_playwright
import os

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        # Serve the file
        filepath = os.path.abspath("index.htm")
        await page.goto(f"file://{filepath}")

        print("Waiting for initial blue cloth...")
        await asyncio.sleep(0.5)
        await page.screenshot(path="move_0.png")

        print("Waiting for swap to red (1s)...")
        await asyncio.sleep(1.0) # Total 1.5s
        await page.screenshot(path="move_1.png")

        print("Waiting to see if red cloth moves (another 0.5s)...")
        await asyncio.sleep(0.5) # Total 2.0s
        await page.screenshot(path="move_2.png")

        print("Waiting more (another 0.5s)...")
        await asyncio.sleep(0.5) # Total 2.5s
        await page.screenshot(path="move_3.png")

        await browser.close()

asyncio.run(run())
