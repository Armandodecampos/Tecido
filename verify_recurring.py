import asyncio
from playwright.async_api import async_playwright
import os

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        filepath = os.path.abspath("index.htm")
        await page.goto(f"file://{filepath}")

        # 0.5s -> Initial Blue
        await asyncio.sleep(0.5)
        await page.screenshot(path="recurring_0.png")
        print("Captured 0.5s (Blue)")

        # 1.5s -> Red
        await asyncio.sleep(1.0)
        await page.screenshot(path="recurring_1.png")
        print("Captured 1.5s (Red)")

        # 2.5s -> Green
        await asyncio.sleep(1.0)
        await page.screenshot(path="recurring_2.png")
        print("Captured 2.5s (Green)")

        # 3.5s -> Yellow
        await asyncio.sleep(1.0)
        await page.screenshot(path="recurring_3.png")
        print("Captured 3.5s (Yellow)")

        await browser.close()

asyncio.run(run())
