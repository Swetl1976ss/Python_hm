from smartphone import Smartphone

catalog = []
catalog.append(Smartphone("Iphone", "14 Promax", "+7908-140-26-51"))
catalog.append(Smartphone("Xiaomi", "Ilite", "+7908-140-26-53"))
catalog.append(Smartphone("Mi", "110", "+7908-140-26-54"))
catalog.append(Smartphone("Redmi", "XR", "+7908-140-26-55"))
catalog.append(Smartphone("Samsung", "Galaxy A32", "+7908-140-26-56"))

for phone in catalog :
    print(f'{phone.brand}, {phone.model}, {phone.number}')




