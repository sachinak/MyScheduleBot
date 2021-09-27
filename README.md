![Python v3.9](https://img.shields.io/badge/python-v3.9-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![DOI](https://zenodo.org/badge/403393616.svg)](https://zenodo.org/badge/latestdoi/403393616)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/lyonva/ScheduleBot)
[![GitHub issues](https://img.shields.io/github/issues/lyonva/ScheduleBot)](https://github.com/lyonva/ScheduleBot/issues)
[![GitHub release (latest by date including pre-releases)](https://img.shields.io/github/v/release/lyonva/ScheduleBot?include_prereleases)](https://github.com/lyonva/ScheduleBot/releases)
[![GitHub all releases](https://img.shields.io/github/downloads/lyonva/ScheduleBot/total)](https://github.com/lyonva/ScheduleBot/releases)
[![Platform](https://img.shields.io/badge/platform-discord-blue)](https://discord.com/)
[![Test cases](https://github.com/lyonva/ScheduleBot/actions/workflows/python-app.yml/badge.svg)](https://github.com/lyonva/ScheduleBot/actions/workflows/python-app.yml)
[![Code coverage](https://raw.githubusercontent.com/lyonva/ScheduleBot/main/doc/img/coverage.svg)](https://github.com/lyonva/ScheduleBot/actions/workflows/python-app.yml)

# ScheduleBot
> Don't let the fear of the time it will take to accomplish something stand in the way of your doing it. The time will pass anyway; we might just as well put that passing time to the best possible use. - Earl Nightingale

ScheduleBot is a Python application that helps you calendarize events and work through a Discord bot. Want to try it out? [Invite the bot into a server](https://discord.com/api/oauth2/authorize?client_id=884865269867102249&permissions=534723951680&scope=bot), and afterward you can DM the bot.

## How can I use the bot?
To get a list of commands, DM the bot the command:
```
!help
```
The bot will reply back you with the list of available commands.

#### Scheduling an event
ScheduleBot's unit of work is the **event**. When you use ScheduleBot to organize your activities, it keeps track of your registered events. Each event consists of a period of time, comprised between a starting and ending date/time. When ScheduleBot tries to find time for a new event, it makes sure it does not overlap with any other events you have. To schedule a new event, just DM the bot:
```
!schedule
```
The bot will ask you the details of your new event.

#### I forgot my agenda for the day
You can take a look at your events scheduled for the day with the command:
```
!day
```

The bot will show you what you have scheduled for the day. This includes events that start before, or end after today.

#### When do I have spare time?
ScheduleBot will help you find a time for that meeting or thing you have been meaning to do. Just write:
```
!find
```

The bot will show you your available times. If you need to find time for another date, try:
```
!find mm/dd/yyyy
```
To see your available times at that date.

#### I don't really want to work at 3 a.m.
You can create custom event types to further organize your schedule. You can define your preferred times by creating a new event type:
```
!typecreate
```
The bot will ask you for the name of the type and your preferred times.

When you look for available times, you now can use ``!find type`` to find only the available times in your preferred hours.


\[Brief description of the workings of the bot\]

\[Picture, gif or demo\]

\[How does it work? More to the point/code detail\]

## Releases

## Documentation

## Getting started

## Commands
