from ncclient import manager
import xml.dom.minidom
# Define  conexion
con = manager.connect(host="192.168.56.102", port=830, username="cisco", password="cisco123!", hostkey_verify=False)

# Filtro  para netconf
netconf_filter = """
<filter>
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native" />
</filter>
"""    

# Recoger información del dispositivo
# 
# netconf_reply = con.get_config(source="running", filter=netconf_filter)   

# Print configuracion
#print(netconf_reply)
print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())
