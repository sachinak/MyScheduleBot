"""
MIT License

Copyright (c) 2023 SEGroup10

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import datetime
import discord
import os
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build


async def get_events(ctx, arg):
    '''
    function oto extract events from google calendar

    Parameters
    ----------
    ctx : Discord context window
    arg : Discord bot user.

    Returns
    -------
    None.

    '''
    print("in events")
    channel = await ctx.author.create_dm()
    SCOPES = ['https://www.googleapis.com/auth/calendar']
    
    token_file = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(
        os.path.abspath(__file__)))), "json", "token.json")
	# If the user has already logged in, the details are extractecd from token.js
    if os.path.exists(token_file):
        creds = Credentials.from_authorized_user_file(
            token_file, SCOPES)
    else:
        await channel.send("You are not logged into Google. PLease login using the ConnectGoogle command")
    print("token found")
    service = build('calendar', 'v3', credentials=creds)
    now = datetime.datetime.utcnow().isoformat() + 'Z'
    print('Getting the upcoming 10 events')
    events_result = service.events().list(calendarId='primary', timeMin=now,
                                               maxResults=10, singleEvents=True, 
                                               orderBy='startTime').execute()
    events = events_result.get('items', [])
    print(events)

    if not events:
        print('No upcoming events found.')
        return
    events_parsed=[]
    keys_to_keep=['summary','description','start','end','location']
    for i in events:
        events_parsed.append({key: value for key, value in i.items() if key in keys_to_keep})
    
    for e in events:
        embed = discord.Embed(colour=discord.Colour.magenta(), timestamp=ctx.message.created_at,
                              title="Your Schedule:")
        embed.set_footer(text=f"Requested by {ctx.author}")
        
        embed.add_field(name="Event Name:", value=e['summary'], inline=False)
        embed.add_field(name="Start Time:", value=e['start'], inline=True)
        embed.add_field(name="End Time:", value=e['end'], inline=True)
        if 'location' in e.keys():
            embed.add_field(name="Location:", value=e['location'], inline=False)
        else:
            embed.add_field(name="Location:", value='None', inline=False)
        #embed.add_field(name="Description:", value=e['description'], inline=False)
        await ctx.send(embed=embed)
    