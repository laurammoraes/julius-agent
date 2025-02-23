from langchain_openai import ChatOpenAI
from browser_use import Agent, Browser
from dotenv import load_dotenv
from browser_use import BrowserConfig
from browser_use.browser.context import BrowserContextConfig, BrowserContext
import asyncio

load_dotenv()

llm = ChatOpenAI(
    model="gpt-4o",
    temperature=0.0,
)


async  def makeAction(action:str):
    try:
       

        
        config = BrowserContextConfig(
            cookies_file="path/to/cookies.json",
            wait_for_network_idle_page_load_time=3.0,
            browser_window_size={'width': 1280, 'height': 1100},
            locale='en-US',
            user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
            highlight_elements=True,
            viewport_expansion=500,
            allowed_domains=['google.com', 'wikipedia.org'],
        )

        browser = Browser()
        # context = BrowserContext(browser=browser, config=config)
        
        agent = Agent(
            task=action,
            # browser=context,
            llm=llm,
            browser=browser,
            use_vision=True,             
            save_conversation_path="logs/conversation"  
           
        )



        result = await agent.run()
        
       
        await asyncio.sleep(5)
        await browser.close()
        return result
    
    except Exception as e:
        print(f"❌ Erro ocorrido: {e}")

# asyncio.run(makeAction())

