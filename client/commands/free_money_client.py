from plug.key import ED25519SigningKey
from plug.hash import sha256
from plug.proof import SingleKeyProof
from free_money.transform import FreeMoney
from plug.transaction import Transaction
from plug.constant import TransactionEvent
from plug.message import Event
from plug.registry import Registry
from client.user import User
import aiohttp
import json
import asyncio

async def init_free_money(client, input_key, amount):

    print("Free Money!")
