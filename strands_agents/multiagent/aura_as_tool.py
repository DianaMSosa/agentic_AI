from strands import Agent, tool
from strands.models import BedrockModel
from general_tools import retrieve_con_kb_fijo


# Instrucciones del agente / System promt
nombre_archivo_instrucciones = "instrucciones_agente_aura.txt"
with open(nombre_archivo_instrucciones, "r", encoding="utf-8") as archivo_instrucciones:
    instrucciones = archivo_instrucciones.read()


@tool
def aura(query: str) -> str:
    """
    Agente AURA versión tool 
    """
    try:
        
        # Create a BedrockModel
        bedrock_model = BedrockModel(
            model_id="anthropic.claude-3-5-sonnet-20240620-v1:0",
            region_name='us-east-1'
        )

        # Crear agente
        agent = Agent(model=bedrock_model,
            system_prompt=instrucciones,
            tools=[retrieve_con_kb_fijo],
            callback_handler=None
            )

        # Call the agent and return its response
        response = agent(query)
        return str(response)
    except Exception as e:
        return f"Error in AURA: {str(e)}"