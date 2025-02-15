import asyncio
import time
from datetime import datetime

async def task():
    print("Hello")
    await asyncio.sleep(3) 
    print("Posting")
    
async def test():
    print("Wazzap!")
    await asyncio.sleep(2)
    print("testing")
    

async def main():
    await asyncio.gather(task(), task(), test(), test(), task())


asyncio.run(main())

# def task1():
#     print("Hello")
#     time.sleep(3)
#     print("Posting")

# def task2():
#     print("Wazzap!")
#     time.sleep(2)
#     print("testing")

# def main():
#     task1()
#     task2()
    
# main()

