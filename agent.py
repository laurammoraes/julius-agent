from langchain_openai import ChatOpenAI
from browser_use import Agent, Browser
from dotenv import load_dotenv
import asyncio

load_dotenv()

llm = ChatOpenAI(
    model="gpt-4o",
    temperature=0.0,
)

async def main():
    try:
        browser = Browser()
        
        agent = Agent(
            task="Open Google and wait",
            llm=llm,
            browser=browser,
        )

        result = await agent.run()
        print(result)

        await browser.close()
    
    except Exception as e:
        print(f"❌ Erro ocorrido: {e}")

asyncio.run(main())
