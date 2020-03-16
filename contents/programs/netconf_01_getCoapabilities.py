from ncclient import manager

# Define  conexion
con = manager.connect(host="192.168.56.102", port=830, username="cisco", password="cisco123!", hostkey_verify=False)

# Printamos capabilities
print("Información de Capabilities")
for capability in con.server capabilities:
    print(capability)
    