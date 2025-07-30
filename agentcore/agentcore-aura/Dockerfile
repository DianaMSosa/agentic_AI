# Imagen base compatible con AgentCore Runtime (ARM64 y Python 3.12)
FROM --platform=linux/arm64 python:3.12-slim

# Directorio de trabajo dentro del contenedor
WORKDIR /var/task

# Copiar e instalar dependencias
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copiar el resto del código del proyecto
COPY aura.py general_tools.py instrucciones_agente_aura.txt ./

# Exponer el puerto esperado por Bedrock AgentCore
EXPOSE 8080

# Comando de inicio del agente
CMD ["python", "aura.py"]
