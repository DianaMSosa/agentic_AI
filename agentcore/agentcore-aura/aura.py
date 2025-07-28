from strands import Agent
from strands.models import BedrockModel
from bedrock_agentcore.runtime import BedrockAgentCoreApp
from general_tools import retrieve_con_kb_fijo
from datetime import datetime

# Crear la app de AgentCore
app = BedrockAgentCoreApp()

# Instrucciones del agente / System promt
nombre_archivo_instrucciones = "instrucciones_agente_aura.txt"
with open(nombre_archivo_instrucciones, "r", encoding="utf-8") as archivo_instrucciones:
    instrucciones = archivo_instrucciones.read()

        
# Create a BedrockModel
bedrock_model = BedrockModel(
    model_id="anthropic.claude-3-5-sonnet-20240620-v1:0",
    region_name='us-east-1'
)

# Crear agente
aura = Agent(model=bedrock_model,
    system_prompt=instrucciones,
    tools=[retrieve_con_kb_fijo]
    )

# Punto de entrada HTTP requerido por Bedrock AgentCore
@app.entrypoint
def invoke(payload, context=None):
    user_message = payload.get("prompt", "Hola")
    
    init_time = datetime.now()
    result = aura(user_message)
    finish_time = datetime.now()
    
    return {
        "result": result.message,
        "execution_time": str(finish_time - init_time)
    }

# Ejecutar el servidor en entorno local o dentro del contenedor
if __name__ == "__main__":
    app.run()