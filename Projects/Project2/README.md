# MY PROJECT 2

## BOT DESCRIPTION
- the bot that I made takes a command (red!) and give you a random quote from the beloved series that is Red vs. Blue. If you haven't seen Red vs. Blue you shoud get on youTube and watch all of it as soon as possible.
- I modified the original code that was provided for us by changing the quotes from The Hitchhikers Guide to the Galaxy quotes, to quotes from Red vs. Blue.
- I also changed the message phrase that triggers the bot to give you a quote from towel! to red!.
- I modified the original bot.py file on my AWS system by first cloning the repo that the file was is to my AWS system. I then created a new brnach and called it work by using git brnach work, to create the new branch. I then used git checkout work to change to the new branch, and changed the quotes and the target work for the code. after I confirmed that the code worked I performed a git add git commit and git push, which told github that the new brach exists.

## DISCORD API KEY
- to create your Discord bot follow the guide from this link:  https://realpython.com/how-to-make-a-discord-bot-python/

- once you set up your Discord app and bot, you will need to place the API key into a file called .env, this file is stored in the same directory that the bot.py file is stored. you then will copy the bot token, by clicking the copy token from the developer portal under "bot token", and paste your token in your .env file like this: DISCORD_TOKEN=your bot token here. 
- you will also need to add the guild name that your bot is a member of, to your .env file. to do this you add DISCORD_GUILD=your guild name.
- also ensure that in your main repo you have a .gitignore file with a realitive path to your .env file, this will ensure that you aren't putting your bots keys on github. If your bots key get exposed, Discord will revoke the key and your bot will not work anymore and you will have to go back to the developent portal to create a new token.

## PYTHON REQUIRMENTS
- In order for this bot to work I had to install a few things into my lacal and aws systems they are listed below:
    - python3, which was already installed on my local system and my AWS system.
    - I did have to install pip, by using "sudo apt install python3-pip"
    - I also had to install dotenv to both my local system and my AWS system. I did this by using pip3 install -U python-dotenv. this allows the code to use your .env file to access your key and guild name.
    - lastly I had to install discord.py, by using the command "pip3 install discord.py", this is the part of the code that says "import discord", knows what to import. 

## RESEARCH
- One way that I have found to keep the bot running all the time, not just when you have the script running is to use the screen command. the screen command allows you to run the script on your remote machine and it will continue running even if you log out of the session. this allows you to run the bot.py script and it will not interupt your use of the terminal.