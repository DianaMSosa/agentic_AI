from strands_tools import retrieve as original_retrieve

# RETRIEVE 

# Clonar la función original con un ID fijo
def retrieve_con_kb_fijo(tool, **kwargs):
    kwargs["knowledgeBaseId"] = "R0IXR8SBIL"
    return original_retrieve(tool, **kwargs)

# Mantener el mismo TOOL_SPEC para que funcione igual
retrieve_con_kb_fijo.TOOL_SPEC = original_retrieve.TOOL_SPEC
