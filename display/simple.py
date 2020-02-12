import asyncio
import logging
import time

from nextion import Nextion, EventType

password = 'abc123'

async def event_handler(type_, data):
    if type_ == EventType.STARTUP:
        print('We have booted up!')
    elif type_ == EventType.TOUCH:
        if data.component_id == 42:
            key = await client.get('t0.txt')
            if (key == password):
                print('True')
                await client.command('page 4')
            else:
                print('False')
                await client.set('t0.txt', '')
    logging.info('Data: '+str(data))

async def run():
    global client
    client = Nextion('/dev/ttyAMA0', 9600, event_handler)
    await client.connect()

    # await client.sleep()
    await client.wakeup()
    
    #await client.command('sendxy=0')
    await client.command('page 0')
    await asyncio.sleep(2)

    if (await client.get('dp') != 1):
        await client.command('page 1')

    print('finished')

if __name__ == '__main__':
    logging.basicConfig(
        format='%(asctime)s - %(levelname)s - %(message)s',
        level=logging.DEBUG,
        handlers=[
            logging.StreamHandler()
        ])
    loop = asyncio.get_event_loop()
    asyncio.ensure_future(run())
    loop.run_forever()
