from smartphone import Smartphone

catalog = []
catalog.append(Smartphone("Iphone", "14 Promax", "8-908-140-26-50"))
catalog.append(Smartphone("Xiaomi", "Ilite", "8-908-140-26-58"))
catalog.append(Smartphone("Mi", "110", "8-908-140-26-59"))
catalog.append(Smartphone("Redmi", "XR", "8-908-140-26-51"))
catalog.append(Smartphone("Samsung", "Galaxy A32", "8-908-140-26-52"))

for phone in catalog :
    print(f'{phone.brand}, {phone.model}, {phone.number}')