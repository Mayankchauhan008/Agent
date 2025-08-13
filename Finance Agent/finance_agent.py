from phi.agent import Agent
from phi.model.groq import Groq
from dotenv import load_dotenv
from phi.tools.yfinance import YFinanceTools

load_dotenv()

agent = Agent(
    model=Groq(id="llama-3.1-8b-instant"),
    tools = [YFinanceTools()],
    show_tool_calls=True,
    markdown= True,
    instructions=["Use table to display data."],
    debug_mode=True
)

agent.print_response("give a Agentic AI roadmap for industary demands.")