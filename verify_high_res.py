import asyncio
from playwright.async_api import async_playwright
import os
import time

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        path = os.path.abspath("index.htm")
        await page.goto(f"file://{path}")
        await asyncio.sleep(3) # Wait for stabilization

        # Measure time for some frames
        start_time = time.time()
        num_frames = 60
        # We can't easily count frames from here without injecting JS,
        # but we can check if it's responsive.

        await page.click("#btn-cut")
        width = page.viewport_size['width']
        height = page.viewport_size['height']

        # Perform a long diagonal cut
        await page.mouse.move(width / 2 - 150, height / 2 - 150)
        await page.mouse.down()
        await page.mouse.move(width / 2 + 150, height / 2 + 150, steps=20)
        await page.mouse.up()

        await asyncio.sleep(2)
        await page.screenshot(path="high_res_diagonal.png")

        # Check floor collision
        await page.screenshot(path="floor_check.png")

        await browser.close()

if __name__ == "__main__":
    asyncio.run(run())
