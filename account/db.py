import motor.motor_asyncio

client = motor.motor_asyncio.AsyncIOMotorClient()

db = client['accountdb']  # -> create a database

collection = db['account']  # -> it is a table in database
