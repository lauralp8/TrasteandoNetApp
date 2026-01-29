import requests
from config import NETAPP_HOST, NETAOOP_USER, NETAPP_PASSWORD

def volume_create(volume_name, svm_name, size_bytes, aggregate_name):
    url = f"https://{NETAPP_HOST}/api/storage/volumes"
    payload = {
        "name": volume_name,
        "svm": {"name": svm_name},
        "size": size_bytes,
        "aggregate": {"name": aggregate_name}
    }
    response = requests.post(
        url, 
        json=payload, 
        auth=(NETAOOP_USER, NETAPP_PASSWORD), 
        verify=False
        )
    
    if response.status_code in [200, 201]:
        print(f"Volume {volume_name} created successfully.")
        print(response.json())
    else:   
        print(f"Failed to create volume {volume_name}. Status code: {response.status_code}")
