print("El script arranca correctamente")

from netapp_api import volume_create

print("Importación correcta")

VOLUME_NAME = "my_volume"
SVM_NAME = "my_svm"
AGREGATE_NAME = "my_aggregate"
SIZE_BYTES = 10*1024*1024*1024  # 10 GiB

volume_create(VOLUME_NAME, SVM_NAME, SIZE_BYTES, AGREGATE_NAME)
