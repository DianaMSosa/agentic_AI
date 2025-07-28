from strands import Agent
from strands.models import BedrockModel
from datetime import datetime
from aura_as_tool import aura

# import asyncio

from strands.session.file_session_manager import FileSessionManager
session_manager = FileSessionManager(session_id="test-session")

# Create a BedrockModel
bedrock_model = BedrockModel(
    model_id="anthropic.claude-3-5-sonnet-20240620-v1:0",
    region_name='us-east-1'
)

# Instrucciones del agente / System promt
nombre_archivo_instrucciones = "instrucciones_orchestrator.txt"
with open(nombre_archivo_instrucciones, "r", encoding="utf-8") as archivo_instrucciones:
    instrucciones = archivo_instrucciones.read()

# Create orchestrator agent
orchestrator = Agent(
    model=bedrock_model,
    system_prompt=instrucciones,
    tools = [aura],
    session_manager=session_manager
)

# Ejecución
end = False
while end is False:
    inputUser = input("Escribe una pregunta para el agente:") 
    initTime = datetime.now() 
    orchestrator(inputUser)
    finishTime = datetime.now()
    executionTime = finishTime - initTime
    print("Tiempo de ejecución: " + str(executionTime))
    
    end_input = input("Deseas continuar con la conversación? y/n:")
    if end_input == "n":
        print(orchestrator.messages)
        end = True

# inputUser = input("Escribe una pregunta para el agente:")

# # Async function that iterators over streamed agent events
# async def process_streaming_response():
#     agent_stream = orchestrator.stream_async(inputUser)
#     async for evento in agent_stream:
#         print(evento)

# # Run the agent
# asyncio.run(process_streaming_response())