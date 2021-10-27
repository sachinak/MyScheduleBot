![ScheduleBot logo](https://raw.githubusercontent.com/lyonva/ScheduleBot/main/docs/img/banner.png)

![Python v3.9](https://img.shields.io/badge/python-v3.9-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![DOI](https://zenodo.org/badge/419116957.svg)](https://zenodo.org/badge/latestdoi/419116957)
[![Build Status](https://app.travis-ci.com/qchen59/ScheduleBot.svg?branch=main)](https://app.travis-ci.com/github/qchen59/ScheduleBot)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/lyonva/ScheduleBot)
[![GitHub issues](https://img.shields.io/github/issues/lyonva/ScheduleBot)](https://github.com/lyonva/ScheduleBot/issues)
[![GitHub release (latest by date including pre-releases)](https://img.shields.io/github/v/release/lyonva/ScheduleBot?include_prereleases)](https://github.com/lyonva/ScheduleBot/releases)
[![GitHub all releases](https://img.shields.io/github/downloads/lyonva/ScheduleBot/total)](https://github.com/lyonva/ScheduleBot/releases)
[![Platform](https://img.shields.io/badge/platform-discord-blue)](https://discord.com/)
[![Test cases](https://github.com/lyonva/ScheduleBot/actions/workflows/python-app.yml/badge.svg)](https://github.com/lyonva/ScheduleBot/actions/workflows/python-app.yml)
[![Code coverage](https://raw.githubusercontent.com/lyonva/ScheduleBot/main/docs/img/coverage.svg)](https://github.com/lyonva/ScheduleBot/actions/workflows/python-app.yml)

# ScheduleBot

> Don't let the fear of the time it will take to accomplish something stand in the way of your doing it. The time will pass anyway; we might just as well put that passing time to the best possible use. - Earl Nightingale

ScheduleBot is a Python application that helps you calendarize events and work through a Discord bot. Want to try it out? ~~[Invite the bot into a server](https://discord.com/api/oauth2/authorize?client_id=884865269867102249&permissions=534723951680&scope=bot), and afterward you can DM the bot. (To be implemented in the future)~~ Join the [ScheduleBot server](https://discord.gg/xRaact5GmH) and DM the bot.

With ScheduleBot you can quickly schedule events, state your prefered times for certain types of activities (exercise, homework, meetings, etc.) and quickly find out which times you have available to do more stuff.

![Setup](docs/img/Startup.gif)

## Getting started

To get a list of commands, DM the bot the command:

```
!help
```

The bot will reply back you with the list of available commands.

### **Scheduling an event**

ScheduleBot's unit of work is the **event**. When you use ScheduleBot to organize your activities, it keeps track of your registered events. Each event consists of a period of time, comprised between a starting and ending date/time. When ScheduleBot tries to find time for a new event, it makes sure it does not overlap with any other events you have. To schedule a new event, just DM the bot:

```
!schedule
```

The bot will ask you the details of your new event.

![Schedule](docs/img/Schedule.gif)

### **I forgot my agenda for the day**

You can take a look at your events scheduled for the day with the command:

```
!day
```

The bot will show you what you have scheduled for the day. This includes events that start before, or end after today.

![Day](docs/img/Day.gif)

### **I don't really want to work at 3 a.m.**

You can create custom event types to further organize your schedule. You can define your preferred times by creating a new event type:

```
!typecreate
```

The bot will ask you for the name of the type and your preferred times.

![Type Create](docs/img/Type%20Create.gif)


## Releases

-   [All releases](https://github.com/lyonva/ScheduleBot/releases)
-   Latest: [v0](https://github.com/lyonva/ScheduleBot/releases/tag/v0)

## Documentation

## Getting involved

Thank you for caring for this project and getting involved. To start, please check out [contributing](https://github.com/lyonva/ScheduleBot/blob/main/CONTRIBUTING.md) and [code of conduct](https://github.com/lyonva/ScheduleBot/blob/main/CODE_OF_CONDUCT.md). For more technical detail of implementation of code, you can check out the documentation. When you want to get your hands on the project, take a peek into the [github project](https://github.com/lyonva/ScheduleBot/projects/1), assign yourself a task, move it to To-Do, and convert it into an issue and assign it to yourself.

Check out the [online documentation](https://lyonva.github.io/ScheduleBot/) if you want to contribute or find out about the inner workings of ScheduleBot.

## Future features

### **When do I have spare time?**

ScheduleBot will help you find a time for that meeting or thing you have been meaning to do. Just write:

```
!find
```

The bot will show you your available times. If you need to find time for another date, try:

```
!find mm/dd/yyyy
```

To see your available times at that date.

\[Screenshot\]


### Find available times for a type of event
When you look for available times, you now can use `!find type` to find only the available times in your preferred hours. You still can create events of that type outside your preferred hours.

\[Screenshot\]

### Quick event creation

You can quickly create a new event with the command

```
!schedulefind type X
```

\[Screenshot\]

It will find and schedule the first available X contiguous hours, on your preferred hours of the specified `type`.

\[Screenshot\]

\[Add more future functionality\]
