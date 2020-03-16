from ncclient import manager
import xml.dom.minidom
# Define  conexion
con = manager.connect(host="192.168.56.102", port=830, username="cisco", password="cisco123!", hostkey_verify=False)

# Filtro  para netconf
netconf_filter = """
<config>
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native" />
    <interface>
        <Loopback>
            <name>88</name>
            <description> Interface_test_Loopback </description>
            <ip>
                <address>
                    <primary>
                        <address>88.88.88.88</address>
                        <mask>255.0.0.0</mask>
                    </primary>
                </address>
            </ip>
        </Loopback>
    </interface>
</config>
"""    

# Recoger información del dispositivo
# 
# netconf_reply = con.get_config(target="running",  config=netconf_filter)   

# Print configuracion
#print(netconf_reply)
print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())
