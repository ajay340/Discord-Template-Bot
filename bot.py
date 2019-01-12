import discord
from discord.ext.commands import Bot

BOT_PREFIX = ("!")
TOKEN = ''

client = Bot(command_prefix=BOT_PREFIX)

#-=-=-=-=-=-Simple Bot Commands-=-=-=-=-=-

@client.event
async def on_message(message):

#-=-=-=-=-=-Basic Template functions-=-=-=-=-=-=-=-

    # Template for text commands
    async def textCom(textMessage):
        msg = textMessage.format(message)
        await client.send_message(message.channel, msg)

    #Template for file commands
    async def fileCom(file):
        filePath = 'files/' + file
        await client.send_file(message.channel, filePath)
    
    #Template to Clear Messages
    async def clearMessages():
        tmp = await client.send_message(message.channel, 'Clearing messages...')
        async for msg in client.logs_from(message.channel):
            await client.delete_message(msg)
    
    #Template for conditional Tag commands
    async def ifTag(*commandExecute):
        if discord.utils.get(message.author.roles, name="tag"):
            count = 0 
            while (count < len(commandExecute)):
                await commandExecute[count]
                count = count + 1
            
        else:
            await textCom("Sorry cannot execute that command because you are not have 'tag'")
    
    #Template to change the Bot's appearance
    async def changeBot(picture, name, status):
        with open('files/' + picture, 'rb') as myfile:
            await client.edit_profile(avatar=myfile.read(), username=name)
            myfile.close()
            await client.change_presence(status=discord.Status(status), afk=False)

#-=-=-=-=-=-Security Precautions-=-=-=-=-=-    
    # The bot cannot initate commands by itself
    if message.author == client.user:
        return

    
    # Commands cannot be initated in private messages
    if message.channel.type == discord.ChannelType.private:
        return

#-=-=-=-=-=-Basic commands-=-=-=-=-=-=-=-


    #If the user types "!hello" in a channel, the bot will reply with "Hello, <user>" in that same channel
    if message.content.startswith('!hello'):
        await textCom("Hello, {0.author.mention}")

    #If the user types "!picture" in a channel, the bot will reply with "Here is a picture" following a picture uploaded in that same channel
    if message.content.startswith('!picture'):
        await textCom("Here is a picture")
        await fileCom('picture.jpg')
    
    #If the user types "!clear" in a channel, the bot will reply with "Clearing messages" following the deletion of 120 messages in that same channel (bot needs sufficent permissions)
    if message.content.startswith('!clear'):
        await clearMessages()

    #If the user types "!ChangeProfile" in a channel, the bot will change its profile picture to the given picture file in the files folder, change its name, and set its status as given.
    if message.content.startswith('!ChangeProfile'):
        await changeBot("unhelper-bot.png", "Helper-Bot", "Idle")

    #If the user types "!ChangeProfileBack" in a channel, the bot will change its profile picture to the given picture file in the files folder, change its name, and set its status as given.
    if message.content.startswith('!ChangeProfileBack'):
        await changeBot("helper-bot.png", "Unhelper-Bot", "Online")

    await client.process_commands(message)

#-=-=-=-=-=-Function Specific Commands-=-=-=-=-=-
@client.command()
async def DivideByTwo(number):
    resultNum = int(number) / 2
    await client.say(str(number) + " divided by two is " + str(resultNum))

#-=-=-=-=-=-Client command errors-=-=-=-=-=-=-=-

@DivideByTwo.error
async def test_on_error(ctx, error):
	await client.say("Sorry you need to enter a number in to be divided by 2")

#-=-=-=-=-=-Client Runtime-=-=-=-=-=-=-=-
@client.event
async def on_ready():
    print('------')
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)