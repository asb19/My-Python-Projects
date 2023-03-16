import asyncio
import telegram


async def main():
    bot = telegram.Bot("5515533637:AAFYNv5V2sauTkvyM8OjB-XrWUoc6uS8Rnk")
    async with bot:
        print(await bot.getUpdates())


if __name__ == '__main__':
    asyncio.run(main())