from twitchio.ext import commands
import os
import tensorflow as tf
# import tensorflow_hub as hub
import tensorflow_text as text
# import tensorflow.keras.backend as K

class Bot(commands.Bot):

    def __init__(self):
        # Initialise our Bot with our access token, prefix and a list of channels to join on boot...
        # prefix can be a callable, which returns a list of strings or a string...
        # initial_channels can also be a callable which returns a list of strings...
        super().__init__(token='oauth:<YourAuthToken>', prefix='?', initial_channels=['disguisedtoast', 'amouranth'])

    async def event_ready(self):
        # Notify us when everything is ready!
        # We are logged in and ready to chat and use commands...
        print(f'Logged in as | {self.nick}')
        print(f'User id is | {self.user_id}')

    async def event_message(self, message):
        # Messages with echo set to True are messages sent by the bot...
        # For now we just want to ignore them...
        if message.echo:
            return
        dic = {0: 'hate_speech', 1: 'offensive_language', 2: 'neither'}
        # Print the contents of our message to console...
        print(message.content, message.id)
        result =  model.predict([message.content])
        index = result.argmax()
        print(dic[index])
        message_id = message.tags['id']
        
        if(index == 0 or index == 1):
            print(f"Hate Speech or Offensive Language detected by user, {message.author.name}")
            await message.channel.send(f"/delete {message_id}")
            # await message.channel.send(f"/timeout {message.author.name} 1")
            await message.channel.send(f"{message.author.name}, please refrain from using hate speech or offensive language.")
        
        
        # Since we have commands and are overriding the default `event_message`
        # We must let the bot know we want to handle and invoke our commands...
        await self.handle_commands(message)

    @commands.command()
    async def hello(self, ctx: commands.Context):
        # Here we have a command hello, we can invoke our command with our prefix and command name
        # e.g ?hello
        # We can also give our commands aliases (different names) to invoke with.

        # Send a hello back!
        # Sending a reply back to the channel is easy... Below is an example.
        await ctx.send(f'Hello {ctx.author.name}!')

if __name__ == '__main__':
    # Create an instance of our Bot class.
    # This will start the connection to Twitch and start listening for events.
    print('Loading Bert Model...')
    model = tf.keras.models.load_model("C:/Users/apurv/Downloads/wandb/mpl_hate_speech_bert")
    print('Model Loaded!')
    
    bot = Bot()
    bot.run()

    # bot.run() is blocking and will stop execution of any below code here until stopped or closed.
