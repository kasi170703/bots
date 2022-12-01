from decouple import config


passw=config("PASSWORD", cast=int)
print(type(passw), passw)



name = config("NAME")
print(name)

