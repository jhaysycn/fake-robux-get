from playwright.async_api import async_playwright
import asyncio
import random
import os
import time

"""
by playboisanz
"""

async def isRobuxGet(cnt):
    f = open("RobloxAccount_For_getRobux.txt" , "r" , encoding="UTF-8")
    re = f.read()

    rbx_id = re.split(":")[0]
    rbx_pw = re.split(":")[1]

    async with async_playwright() as RBX:
        browser = await RBX.chromium.launch(headless=False)
        bot = await browser.new_page()
        await bot.goto("https://www.roblox.com/login")
        await bot.type("#login-username",rbx_id)
        await bot.type("#login-password",rbx_pw)
        await bot.click("#login-button")
        await asyncio.sleep(3)
        print("Login Success")
        await asyncio.sleep(3)
        path = 'xpath=//*[@id="nav-robux-amount"]'
        rand_second = random.randint(2,9)
        handle = await bot.query_selector(path)
        value = await handle.inner_text()
        print("현재 로벅스 수 : {}".format(value))
        print("최소 2초 최대 9초 까지 시간이 걸릴수 있습니다.")
        result = int(value) + int(cnt)
        print(result)

        for _ in range(2):
            await asyncio.sleep(rand_second)
            await bot.reload()
        x = 'span[id^=nav-robux-amount]'
        await bot.evaluate(f"() => document.querySelector('{x}').innerHTML = ' '")
        await asyncio.sleep(0.3)
        await bot.evaluate(f"() => document.querySelector('{x}').innerHTML = '{str(result)}'")
        
            
        
        await asyncio.sleep(20)
        await bot.close()
        print("로벅스가 정상적으로 들어왔습니다.\n이전 로벅스 수 : {}\n현재 로벅스 수 : {}".format(value,result))
        await asyncio.sleep(1)
        return input("계속 할려면 ENTER 을 누르십시오...")
        
        
def main():
    if os.path.isfile("RobloxAccount_For_getRobux.txt"):
        count = input("로벅스를 받을 갯수를 입력 해 주세요 >> ")
        time.sleep(3)
        os.system("cls")
        asyncio.run(isRobuxGet(count))
    else:
        print("파일이 존재 하지 않습니다!")
        return input("RobloxAccount_For_getRobux.txt 형식으로 파일을 생성 해 주세요.")

if __name__ == "__main__":
    main()    
