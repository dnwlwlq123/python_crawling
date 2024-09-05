import asyncio
from playwright.async_api import async_playwright
from time import time, sleep

async def login(page):
    login_button = await page.wait_for_selector('a[onclick = "return m_login_link()"]')
    await login_button.click()
    await page.evaluate('() => {window.scrollTo(0, 3);};')

    login_phone_button = await page.wait_for_selector('input[onclick = "fn_chgInputFlg(4)"]')
    await login_phone_button.click()

    await page.fill('input[id="txtCpNo2"]', '4193')
    await page.fill('input[id="txtCpNo3"]', '2683')
    await page.fill('input[id="txtPwd1"]', 'jko12033030@')

    submit_button = await page.wait_for_selector('a[onclick="return Login(1);"]')
    await submit_button.click()

    location_start_button = await page.wait_for_selector('a[onclick="return btnPopWin(1,\'txtGoStart\');"]')
    await location_start_button.click()

    await page.wait_for_selector('.sc_page_inner')
    start_handle = await page.wait_for_selector("a[href='javascript:putStation('천안아산','0502')']")
    await start_handle.click()

    # location_end_handle = await page.wait_for_selector("a[href='return btnPopWin(1,'txtGoEnd')']")
    # await location_end_handle.click()


async def main():
    async with async_playwright() as p:
        browser = await  p.chromium.launch(headless = False)
        context = await browser.new_context()
        page = await browser.new_page()
        await page.goto('https://www.letskorail.com/')
        await login(page)
        sleep(1000000)


if __name__ == '__main__':
    asyncio.run(main())