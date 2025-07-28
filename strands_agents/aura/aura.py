from strands import Agent, tool
from strands.models import BedrockModel
from general_tools import retrieve_con_kb_fijo
from datetime import datetime


# Instrucciones del agente / System promt
nombre_archivo_instrucciones = "instruccionesAgenteAura.txt"
with open(nombre_archivo_instrucciones, "r", encoding="utf-8") as archivo_instrucciones:
    instrucciones = archivo_instrucciones.read()



        
# Create a BedrockModel
bedrock_model = BedrockModel(
    model_id="anthropic.claude-3-5-sonnet-20240620-v1:0",
    region_name='us-east-1'
)

# Crear agente
agent = Agent(model=bedrock_model,
    system_prompt=instrucciones,
    tools=[retrieve_con_kb_fijo]
    )

# Ejecución
end = False
while end is False:
    inputUser = input("Escribe una pregunta para el agente:") 
    initTime = datetime.now() 
    agent(inputUser)
    finishTime = datetime.now()
    executionTime = finishTime - initTime
    print("Tiempo de ejecución: " + str(executionTime))
    
    end_input = input("Deseas continuar con la conversación? y/n:")
    if end_input == "n":
        print(agent.messages)
        end = True
