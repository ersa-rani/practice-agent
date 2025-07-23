import chainlit as cl
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel
from dotenv import load_dotenv,find_dotenv
import os

gemini_api_key=os.getenv("GEMINI_API_KEY")

external_client:AsyncOpenAI = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

model:OpenAIChatCompletionsModel = OpenAIChatCompletionsModel(
    model="gemini-2.5-flash",
    openai_client=external_client
)


agent: Agent = Agent(name="Assistant", instructions="You are a helpful assistant", model=model)

@cl.on_message
async def main(message: cl.Message):
    
    result = await Runner.run(agent, message.content)
    await cl.Message(
        content=result.final_output,
    ).send()
