"""
NetApp ONTAP Volume Retrieval Script

This script connects to a NetApp ONTAP cluster and retrieves information
about a specific volume. It prompts the user for a volume name, establishes
a connection to the ONTAP cluster using REST API, and fetches the volume
details using the NetApp ONTAP Python SDK.
"""

# support connection to the ONTAP cluster and error handling
# volume resource to interact with volume objects
from os import name
from netapp_ontap import config, HostConnection, NetAppRestError
from netapp_ontap.resources import Volume

# takes user input for volume name
print()
vol_name = input("Enter Volume Name: ")
print()


# host connection object to establish connection to the ONTAP cluster
# save it into a global config object
config.CONNECTION = HostConnection(
    'cluster1.demo.netapp.com',
    'admin',
    'Netapp1!',
    verify=False
)



print("Retrieving volume info...")
vol = Volume()

# gets volume details
try:
    vol.get(**{"name": vol_name})
    print(vol)
    pass
except NetAppRestError as error:
    print("Exception :" + str(error))
