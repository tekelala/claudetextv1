import os
from anthropic import Anthropic, AsyncAnthropic

# Sync client
client = Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"]) 

# Async client
async_client = AsyncAnthropic(api_key=os.environ["ANTHROPIC_API_KEY"])

def generate_prompt(text_file):
  return f"Role: You are Nancy Duarte part of the Kravata team an expert in crafting slide Decks for startups. Please create a slide deck on: {text_file}"

prompt = generate_prompt("compliance")

response = client.completions.create(
  model="claude-2",
  prompt=prompt,
  max_tokens=500,
  stop_sequences=["That concludes the presentation"],
)

print(response.completion)

async def generate_async():
  prompt = generate_prompt("compliance")
  
  response = await async_client.completions.create(
    model="claude-2",
    prompt=prompt,
    max_tokens=500, 
    stop_sequences=["That concludes the presentation"]
  )

  print(response.completion)

# Call async function
asyncio.run(generate_async())