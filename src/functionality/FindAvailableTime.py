import os

async def find_avaialbleTime(ctx, client):

    channel = await ctx.author.create_dm()
    # print(ctx.author.id)
    def check(m):
        return m.content is not None and m.channel == channel and m.author == ctx.author

    await channel.send("Let's find time for your event. Enter the Event Type:-")
    event_msg = await client.wait_for("message", check=check)  # Waits for user input
    event_msg = event_msg.content  # Strips message to just the text the user entered
    print(event_msg)

#    get_val = SetTime[event_msg]    
#    startTime = get_val[0] if get_val[0]<12 else get_val[0]-12
#    range = 'am' if get_val[0]<12 else 'pm'
#    timeAvailable = 'You have '+event_msg+' time available between '+str(startTime)+' '+range
#    endTime = get_val[1] if get_val[1]<12 else get_val[1]-12
#    range = 'am' if get_val[1]<12 else 'pm'
#    timeMessage = timeAvailable+' to '+str(endTime)+' '+range

#    await message.author.send(timeMessage)

