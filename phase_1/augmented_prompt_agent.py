# TODO: 1 - Import the AugmentedPromptAgent class
from workflow_agents.base_agents import AugmentedPromptAgent

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve OpenAI API key from environment variables
openai_api_key = "voc-2310356941598742299037688264a2ce6794.44558202"

prompt = "What is the capital of France?"
persona = "You are a college professor; your answers always start with: 'Dear students,'"

# TODO: 2 - Instantiate an object of AugmentedPromptAgent with the required parameters
agent = AugmentedPromptAgent(openai_api_key, persona)

# TODO: 3 - Send the 'prompt' to the agent and store the response in a variable named 'augmented_agent_response'
augmented_agent_response = agent.respond(prompt)
# Print the agent's response
print(augmented_agent_response)

# TODO: 4 - Add a comment explaining:
# - What knowledge the agent likely used to answer the prompt.
# The agent used general world knowledge from its training to answer that Paris is the capital of France.
# - How the system prompt specifying the persona affected the agent's response.
# The system prompt shaped the response by making the agent adopt the professor persona, 
# causing it to begin with “Dear students,” and use a formal, instructional tone.
print("""
The agent likely used general world knowledge from its training to answer that Paris is the capital of France.""")
print("""
The system prompt specifying the persona affected the agent's response by making it adopt the professor persona,
causing it to begin with "Dear students," and use a formal, instructional tone.
""")

