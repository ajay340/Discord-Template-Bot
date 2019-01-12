# Discord Template Bot
This is a simple template Discord bot, created using Discord.py

## Getting Started
First create your discord bot by creating an application, in the [discord developer portal](https://discordapp.com/developers/applications/), and then go under the bot section and create your bot.

Now find your client secret id, under general information, and visit the bot authorization page using your client secret id: https://discordapp.com/oauth2/authorize?client_id=CLIENTSECRETID&scope=bot and authorize your bot to the server.

Now put input your bot's token, in bot.py, under the TOKEN variable, and run the python program.

## Simple commands
All simple commands will be entered in under the on_message function.

For sending text responses:
```
if message.content.startswith('!<command>'):
    await textCom('<text>')
```

"text" is the text response and "!command" is the command to trigger the response

For sending file responses:
```
if message.content.startswith('!<command>'):
    await fileCom(<file>)
```

All files must be uploaded to the "files" folder; where "file" is the file name (with the extension) in the "files" directory and "!command" is the command to trigger the response.

## Advance Commands
To contribute parameter functions you will need to include @client.command() and then include an async function with your parameter.

Example:
```
@client.command()
async def DivideByTwo(number):
    resultNum = int(number) / 2
    await client.say(str(number) + " divided by two is " + str(resultNum))
```

This would return with the bot replying:
```
<given number> divided by two is <expected output>
```

It also important to include error exceptions incase there are improper parsed arguments

Example:
```
@DivideByTwo.error
async def test_on_error(ctx, error):
	await client.say("Sorry you need to enter a number in to be divided by 2")
```
