from playwright.async_api import async_playwright
import asyncio

url = 'https://www.montevideo.com.uy/Noticias/Esta-tarde-comienza-oficialmente-la-primavera-2025-y-al-parecer-sera-de-las-buenas-uc937301'

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto(url, wait_until="domcontentloaded", timeout=60000)

        # first_link = page.locator('a').first
        # await first_link.click()
        # await page.wait_for_load_state()

        imgs = await page.locator("img").all()
        for i, img in enumerate(imgs[:10], start=1): 
            src = await img.get_attribute("src")
            print(f"{i}: {src}")

        parrafos = await page.locator("p").all()
        for p_tag in parrafos:
            texto = await p_tag.text_content()
            if texto and "Dicho en buen romance" in texto:
                print("\nTexto encontrado:")
                print(texto)
                break

        await browser.close()

asyncio.run(run())