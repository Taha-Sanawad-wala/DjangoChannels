from channels.consumer import SyncConsumer,AsyncConsumer
from channels.exceptions import StopConsumer
from time import sleep
import asyncio
class MySyncConsumer(SyncConsumer):
    # This handler is called when client initially opens a connection and is about to finish the WebSocket handshake.
    def websocket_connect(self, event):
        print('WebSocket Connect...',event)
        self.send({
            'type':"websocket.accept"
        })
    # This handler is called when data received from Client
    def websocket_receive(self, event):
        print('Websocket Received...',event)
        # self.send({
        #     'type' : 'websocket.send',
        #     'text': 'Message sent to client'
        # })
        for i in range(40):
            self.send({
                'type': 'websocket.send',
                'text': str(i)
            })
            sleep(1)
    # This handler is called when either connection to the client is lost, either from the client closing the connection, the server closing the connection, or loss of the socket.
    def websocket_disconnect(self, event):
        print('Websocket Disconnect...',event)
        raise StopConsumer()

class MyAsyncConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        print('WebSocket Connect...',event)
        await self.send({
            'type':"websocket.accept"
        })
    async def websocket_receive(self, event):
        print('Websocket Received...',event)
        # await self.send({
        #     'type' : 'websocket.send',
        #     'text': 'Message sent to client'
        # })
        for i in range(40):
            await self.send({
                'type': 'websocket.send',
                'text': str(i)
            })
            await asyncio.sleep(1)

    async def websocket_disconnect(self, event):
        print('Websocket Disconnect...',event)
        raise StopConsumer()