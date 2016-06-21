#!/usr/bin/env python

import asyncio
import websockets

@asyncio.coroutine
def hello(websocket, path):
	blob = yield from websocket.recv()
	#print("< {}".format(name))
	reply = "RECEIVED!"
	yield from websocket.send(reply)
	#print("> {}".format(greeting))

	'''
	manipulate file
	'''
	audioFile = open('x.wav','wb')
	audioFile.write(blob)
	audioFile.close()

start_server = websockets.serve(hello, '0.0.0.0', 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
