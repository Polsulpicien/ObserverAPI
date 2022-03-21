from ObserverAPI import Observer
import asyncio

async def main():
    # Start the Client
    # Note: Don't forget to provide your Observer API Key!
    client = await Observer(key="INSERT YOUR OBSERVER API KEY HERE") 
    

    # A Player Minecraft UUID, this is the only post endpoint,
    # supporting only one uuid for each requests.
    #
    # Note: For this example I haven't provided any UUID, don't forget
    # to provide one! If the registration is sucessful, you will not be
    # able to register the player again...
    uuid = [""] 


    register = await client.register.post(uuid)
    if register == True:
        print("Registered Sucessfully")
    else:
        print("An error occured :/")


asyncio.get_event_loop().run_until_complete(main())
