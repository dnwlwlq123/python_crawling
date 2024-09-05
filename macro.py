import asyncio
from playwright.async_api import async_playwright
from time import time, sleep

async def naver_search(page, search_keyword='새싹'):
    search = await page.wait_for_selector('#query')
    await search.type(search_keyword)
    await page.evaluate('() => {window.scrollTo(0, 10000);};')

    execute_search = await page.wait_for_selector('.btn_search')
    await execute_search.click()
    await page.wait_for_selector('.sc_page_inner')
    await page.evaluate('() => {window.scrollTo(0, 10000);};')
async def main():
    async with async_playwright() as p:
        browser = await  p.chromium.launch(headless = False)
        context = await browser.new_context()
        page = await browser.new_page()
        await page.goto('https://www.letskorail.com/')
        await naver_search(page, search_keyword = '레츠코레일')
if __name__ == '__main__':
    asyncio.run(main())