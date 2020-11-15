import seldiscord

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"

with seldiscord.Session(user_agent) as dsc:
  dsc.setup()
  # now that TLS fingerprinting has been evaded, Discord is likely
  # to present no captchas while creating an account
  print(dsc.register(
    username="wowmenokmenaa",
    #email="support@discordapp.com",
    #password="hunter2",
    #invite="fortnite"
  ))
  dsc.gateway()
