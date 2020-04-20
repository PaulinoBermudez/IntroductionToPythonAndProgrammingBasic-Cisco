from ncclient import manager
import xml.dom.minidom
# Define  conexion
con = manager.connect(host="192.168.56.102", port=830, username="cisco", password="cisco123!", hostkey_verify=False)

# Recoger información del dispositivo
# 
# netconf_reply = con.get_config(source="running")   

# Print configuracion
#print(netconf_reply)
print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())
