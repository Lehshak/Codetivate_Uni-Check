import os
import discord
from storage import uniT

my_secret = os.environ['Token']

class University:
 
    def __init__(self, name, arts, science, commerce, engineering):
        self.name = name
        self.arts = arts
        self.science = science
        self.commerce = commerce
        self.engineering = engineering

ulist = []

el = 0
for i in range(int(len(uniT)/5)):
    uni = University(uniT[el], uniT[el+1], uniT[el+2], uniT[el+3], uniT[el+4])
    ulist.append(uni)
    el = el + 5

client = discord.Client()
@client.event
async def on_ready():
  print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('?help'):
    await message.channel.send("```Hello! This is UniChecker and here we check different universities minimum grade requirements for each of their faculties including Arts, Commerce, Science and Engineering. You can also enter your grade average so that we can check which universities you qualify to apply to!\n\nInstructions:\n For a list of every university in the database: ?university\n For specific faculties: ?faculty\n For a specific university and their faculties: ?U *name*(university name)\n ```")

  if message.content.startswith('?university'):
    info = "```\nWe have over 60 different schools in our database right here: \n"
    for i in range(len(ulist)):
      info += "- " + ulist[i].name + "\n"
    
    info += "\n```"
      
    await message.channel.send(info)


  if message.content.startswith("?faculty"):
    info = "```\nTo find grade range for a specific faculties from universities, please use the ? command and your desired faculty(Arts, Science, Commmerce, Engineering\n Ex: ?science <- all lower cases\n```"
    await message.channel.send(info)

  if message.content.startswith("?science"):
    info = "```\n"
    for i in range(len(ulist)):
      info +=  ulist[i].name + " | " + ulist[i].science + "\n"
    info += "```"
    await message.channel.send(info)

  if message.content.startswith("?arts"):
    info = "```\n"
    for i in range(len(ulist)):
      info +=  ulist[i].name + " | " + ulist[i].arts + "\n"
    info += "```"
    await message.channel.send(info)

  if message.content.startswith("?commerce"):
    info = "```\n"
    for i in range(len(ulist)):
      info +=  ulist[i].name + " | " + ulist[i].commerce + "\n"
    info += "```"
    await message.channel.send(info)

  if message.content.startswith("?engineering"):
    info = "```\n"
    for i in range(len(ulist)):
      info +=  ulist[i].name + " | " + ulist[i].engineering + "\n"
    info += "```"
    await message.channel.send(info)
    
  if message.content.startswith("?avr"):
    avr = 0
    elist = []
    info = ""
    for avr in range(100):
      if message.content.endswith(str(avr)):
        a = avr
        break
    for i in range(len(ulist)):
        numeric_filter = filter(str.isdigit, ulist[i].engineering)
        iengineering = "".join(numeric_filter)
        elist.append(iengineering)
        
    for element in elist:
        if len(element) == 2:
            elist[elist.index(element)] = float(element)
        if len(element) ==3:
            elist[elist.index(element)] = float(element[0]+element[1]+"."+element[2])
        if len(element) ==4:
            elist[elist.index(element)] = [float(element[0]+ element[1]),float(element[2]+ element[3])]
            
        if element == '':
            elist[elist.index(element)] = 0
        if len(element) > 4:
            elist[elist.index(element)] = float(element[0] + element[1])
    elist.add(iengineering)

    for i in range(len(ulist)):
      iengineering.append(ulist[i].name)

    avrlist = []

    for element in elist:
      if len(element) == 2:
        if element[0] <= a:
          avrlist.append(element)

      if len(element) == 3:
        if ((element[0] + element[1])/2) <= a:
          avrlist.append(element)

    for i in range(len(avrlist)):
      info +=  avrlist[-1]+ " | " + avrlist[0] + "\n"

    await message.channel.send(info)
  
  
  if message.content.startswith('?hello'):
    await message.channel.send("```Hi```")
    
  if message.content.startswith('?U'):
    for i in range(len(ulist)):
      if message.content.endswith(ulist[i].name):

        info = "```\n" + ulist[i].name + ":\n" + "Faculty of Arts: " + ulist[i].arts + "\n" + "Faculty of Science: " + ulist[i].science + "\n" + "Faculty of Commerce: " + ulist[i].commerce + "\n" + "Faculty of Engineering: " + ulist[i].engineering + "\n```"
      
        await message.channel.send(info)

client.run(my_secret)


