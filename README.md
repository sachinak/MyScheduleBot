![ScheduleBot logo](https://raw.githubusercontent.com/lyonva/ScheduleBot/main/docs/img/banner.png)

![Python v3.11](https://img.shields.io/badge/python-v3.11-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/manali-teke/MyScheduleBot/blob/main/LICENSE)
[![DOI](https://zenodo.org/badge/429946635.svg)](https://zenodo.org/badge/latestdoi/429946635)
![example workflow](https://github.com/manali-teke/MyScheduleBot/actions/workflows/python-app.yml/badge.svg)
[![example workflow](https://github.com/manali-teke/MyScheduleBot/actions/workflows/style_checker.yml/badge.svg)](https://github.com/manali-teke/MyScheduleBot/actions/workflows/style_checker.yml)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/manali-teke/MyScheduleBot)
[![GitHub issues](https://img.shields.io/github/issues/manali-teke/MyScheduleBot)](https://github.com/manali-teke/MyScheduleBot/issues)
[![GitHub release (latest by date including pre-releases)](https://img.shields.io/github/v/release/SEProjGrp5/ScheduleBot?display_name=release)](https://github.com/SEProjGrp5/ScheduleBot/releases)
[![GitHub all releases](https://img.shields.io/github/downloads/SEProjGrp5/ScheduleBot/total)](https://github.com/SEProjGrp5/ScheduleBot/releases)
[![Platform](https://img.shields.io/badge/platform-discord-blue)](https://discord.com/)
[![codecov](https://codecov.io/gh/SEProjGrp5/ScheduleBot/branch/main/graph/badge.svg?token=Z53J2ZN227)](https://codecov.io/gh/SEProjGrp5/ScheduleBot)


# ScheduleBot

> Don't let the fear of the time it will take to accomplish something stand in the way of your doing it. The time will pass anyway; we might just as well put that passing time to the best possible use. - Earl Nightingale

<p align="center">
  <a href="#rocket-getting-started">Getting Started</a>
  ::
  <a href="#thought_balloon-for-developers">For Developers</a>
  ::
  <a href="#muscle-whats-new-in-V3.0.2">What's new in V3.0.2</a> 
</p>

### Version 3.0.2 Submission Video
Click on the image below to check out the video!

[![IMAGE ALT TEXT](http://img.youtube.com/vi/3UVs0_7Tcxk/0.jpg)](https://youtu.be/qQlPuJNerMA "ScheduleBot CSC 510 Project Group 5 NSCU")

ScheduleBot is a Python application that helps you calendarize events and work through a Discord bot. Want to try it out? Simply follow the steps outlined in the [For Developers](#For-Developers) section. ScheduleBot can be configured to run on your Discord server by adding just one line of code!


With ScheduleBot you can quickly schedule events, state your prefered times for certain types of activities (exercise, homework, meetings, etc.) and quickly find out which times you have available to do more stuff.

https://user-images.githubusercontent.com/34405372/139776326-722e8526-4977-4ffd-b00e-c86a8fd5f706.mp4


:rocket: Getting started
---
To get a list of commands, DM the bot the command:

```
!help
```

The bot will reply back you with the list of available commands.

<img width="481" alt="Screen Shot 2021-11-03 at 10 15 04 PM" src="https://user-images.githubusercontent.com/34405372/140246210-6e0f176e-bb49-47ad-88d4-0b9f04ae073d.png">


### **Scheduling an event**

ScheduleBot's unit of work is the **event**. When you use ScheduleBot to organize your activities, it keeps track of your registered events. Each event consists of a period of time, comprised between a starting and ending date/time, event type, event priority and optional notes.  

To schedule a new event, just DM the bot:

```
!schedule
```

The bot will ask you the details of your new event.

![Schedule](docs/img/!schedul.gif)

### **I forgot my agenda for the day**

You can take a look at your events scheduled for a specfic date with the command:

```
!day today(or tomorrow\yesterday)
```

```
!day 3 (3 days from now)
```

```
!day -3 (3 days ago)
```

```
!day 4/20/22 (On Apr 20, 2022)
```

The bot will show you what you have scheduled for the date. This includes events that start before, or end after this date.

![Day](docs/img/!day.gif)

### **I don't really want to work at 3 a.m.**

You can create custom event types to further organize your schedule. You can define your preferred times by creating a new event type:

```
!typecreate
```

The bot will ask you for the name of the type and your preferred times.

![Type Create](docs/img/Type%20Create.gif)

### Import & Export your calendar

You can import or export their calendar events as a CSV file through the bot. You can also import ICS files downloaded from Google Calendar.

```
!exportfile
```
![Export file](docs/img/!export.gif)

```
!importfile
```
Then drag the file to the Schedulebot.

![Import file](docs/img/!import.gif)

### Looking for the spare time?

ScheduleBot will help you find your free times. Just write:

```
!freetime
```
![Freetime](docs/img/!freetime.gif)

### Find available times for a type of event
When you look for available times, you now can use `!find` to find only the available times in your preferred hours. 

![Find Available times](docs/img/find.gif)

:thought_balloon: For Developers
---

### Get your Discord bot 
 Steps to create your discord bot account. <br />

 
 Step1:- Login in the [discord website](https://discord.com/login) or create your account. <br />
 Step2:- Navigate to the [application page](https://discord.com/developers/applications). <br />
 Step3:- Click on the “New Application” button. <br />
 Step4:- Give the application a name and click “Create”. <br />
 Step5:- Go to the “Bot” tab and then click “Add Bot”. You will have to confirm by clicking "Yes, do it!". <br />
 Step6:- Keep the default settings for Public Bot (checked) and Require OAuth2 Code Grant (unchecked). <br />

 Steps to invite the Bot to your server <br />
 Step1:- Go to the "OAuth2" tab. Then select "bot" under the "scopes" section. <br />
 Step2:- Choose the permissions you want for the bot like send messages, read text and manage channels.<br />
 <img width="481" alt="Screen Shot 2021-11-03 at 10 15 04 PM" src="https://www.freecodecamp.org/news/content/images/2021/06/image-124.png"> <br />
 Step3:- Copy the URL and Paste the URL into your browser, choose a server to invite the bot to, and click “Authorize”. <br />
 Step4:- Add the bot, your account needs "Manage Server" permissions. <br />
 
 
 Follow this [tutorial](https://www.freecodecamp.org/news/create-a-discord-bot-with-python/) to create your discord bot account.

### Token
  
  #### Create an environment variable called `TOKEN` in your host machine with your Discord Bot Token 

  OR

  #### Navigate to `./src/config.py`. It looks like this
  ```python
import os
TOKEN = os.getenv("TOKEN") if os.getenv("TOKEN") else "YOUR DISCORD BOT TOKEN" 
  ```
  Replace `YOUR DISCORD API TOKEN` with your Discord Bot token.
  
### Install required packages
  ```
  pip install -r requirements.txt
  ```

### Install dependencies for discord
  ```
  pip install --pre discord
  ```

### Connect to Google Cloud
  1. Create a Project 
  2. Setup Billing 
  3. Enable geocoding API and distancematrix API
  4. Generate API key-
      Refer to [this](https://developers.google.com/maps/documentation/geocoding/get-api-key) link for more information about the same.
  5. Store the API key in the following format-
      File name: key.json \
      File Content: 
      ```
      {"key": "your api key here"}
      ```
  6. Key needs to be stored in the json folder.

### Run the schedulebot.py
  ```
  python3 schedulebot.py
  ```
  Then your scheduleBot should start working.


## Docker Support
Navigate to `docker-build` directory and create `.env` file and configure the environment variables as per `env-example` file.

### Create and run the build using docker-compose

```
docker-compose up -d
```


## Releases
-   [v1.1](https://github.com/lyonva/ScheduleBot/releases/tag/v1.1): First functional release
-   [v2.0](https://github.com/qchen59/ScheduleBot/releases/tag/v2.0.0): First version 2 release with import/export events function, find available time feature, also supports 24 hour time format and event priority.
-   [v2.1](https://github.com/qchen59/ScheduleBot/releases/tag/v2.1.0): Finalized version 2, check what's new in V2
-   [v3.0](https://github.com/SEProjGrp5/ScheduleBot/releases) Finalized version 3, check out what's new in V3
-   [v3.0.2](https://github.com/SEProjGrp5/ScheduleBot/releases) Finalized version 3, check out what's new in V3.0.2

:dizzy: Features in V3:
---

Please note that this is not an exhaustive list, however it does include all major improvements. For a complete list of all changes and bug fixes, please see our closed github issues or commit history.

#### Import & Export your calendar

The user can now import or export their calendar events as a CSV file through the bot. The user can also import ICS files downloaded from Google Calendar.

#### Find time based on schedule + preferred time

ScheduleBot can help you find available times for a type of event based on your schedule and preferred time for the event type.

#### Event types with priority

Users can now assign a priority value for each event. This will help them keep track of important events. It also provides a foundation for future improvements, such as suggesting event removals based on the priority of events.

#### Support 24-hour time format input

We support 24-hour time format input now, in addition to the 12-hour format.

#### User's files encryption/decryption

User's data is now encrypted when it is stored in the host server, so the host will not be able to see other users\' schedules as easily. This improves user's privacy when using Schedulebot.

#### Check schedule for arbitrary days 

Users are able to check the schedule for any specific day in addition to today. Previously, only the events occurring today could be retrieved by the user.

#### Code coverage improvement

In this version, we improved the project's code coverage from 39% to 54%.

Code coverage remains low in this project because many sections of code require a Discord channel, and responses from a non-bot user through Discord. However, we were able to create a mock discord channel and user for several tests by using the "dpytest" library.

#### Fixed bugs related to the welcome message sent at startup

At startup, the bot now sends an on_ready welcome message to all servers the bot is currently listening to, instead of just one specific server. The bot also no longer attempts to respond to reactions to the welcome message made by itself or other bots.

#### Fixed bugs related to finding freetime

!freetime function was not working under certain circumstances, such as when there was only one event in the schedule. This has been fixed in the latest version.

## Getting involved

Thank you for caring for this project and getting involved. To start, please check out [contributing](https://github.com/qchen59/ScheduleBot/blob/main/CONTRIBUTING.md) and [code of conduct](https://github.com/qchen59/ScheduleBot/blob/main/CODE_OF_CONDUCT.md). For more technical detail of implementation of code, you can check out the documentation. When you want to get your hands on the project, take a peek into the [github project](https://github.com/qchen59/ScheduleBot/projects/1), assign yourself a task, move it to To-Do, and convert it into an issue and assign it to yourself.

Check out the [internal documentation](https://htmlpreview.github.io/?https://github.com/qchen59/ScheduleBot/blob/main/docs/src/index.html) if you want to contribute or find out about the inner workings of ScheduleBot.

:muscle: What's new in V3.0.2:
---
Following are the new features that we have implemented for version 3 : 

#### 1. Quick event creation: 
We have added the functionality to add an event in immediate free slot in google calendar for the given duration.


https://github.com/manali-teke/MyScheduleBot/assets/67600147/73ed9e02-9350-4f4e-bca4-9dd1ed1f04a6



#### 2. Add Online event
Added feature to add URLs when scheduling online events.


https://github.com/manali-teke/MyScheduleBot/assets/67600147/e17db504-22c8-481f-9066-de581b2e106d


#### 3. Add Events to Google Calendar
The bot adds a event directly to Google calendar.


https://github.com/manali-teke/MyScheduleBot/assets/67600147/19aad285-6d9d-4e74-8527-6a07ffde27aa



#### 4. Deleting Events from Google Calendar
User can delete events from google calendar.


https://github.com/manali-teke/MyScheduleBot/assets/67600147/faa6be68-d874-4386-85a7-a8fd833a309e



#### 5. Fetching events for today or particular date from Google calendar
Users can check the events for today or any particular date from google calendar

Check event for today

https://github.com/manali-teke/MyScheduleBot/assets/67600147/6df00d31-b857-407a-a05b-b873c0df6cff

Check event for a specific date

https://github.com/manali-teke/MyScheduleBot/assets/67600147/f5edb98e-f2d7-45e7-a6ee-98d0a5fd9835


#### 6. Cancelling event creation
User can exit from while scheduling an event if they no longer want to continue.


https://github.com/manali-teke/MyScheduleBot/assets/67600147/481dc110-5184-42e0-9353-ac414e460571



## Future features
These are example features that could be added to ScheduleBot in the future.


### Suggest event removals
When Your entire day is scheduled
You have event 1 of priority 4
You try to find time for another event of priority 3
ScheduleBot should say there is no time, but can suggest replacing event 1 as it has less priority.

### Edit event
You can edit the event you created:

```
!eventedit
```

### Feature for creating repeating events
### Send invite feature for group schedules
### Feature to add reminder to an event



