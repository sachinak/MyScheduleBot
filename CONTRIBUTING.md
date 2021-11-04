# Contributing to this project
Thank you for taking your time for learning how to contribute. Below are some general guidelines and practices that you should keep in mind when contributing to this repository.

## Code of Conduct
Please follow the guidelines stated in our [code of conduct](https://github.com/ConnorS1110/CSC510_Homework2b_Group14/blob/main/CODE_OF_CONDUCT.md). You're expected to uphold this code when contributing.

## Setting Up

### Get your Discord bot 

 Follow this [tutorial](https://www.freecodecamp.org/news/create-a-discord-bot-with-python/) to create your discord bot account.

### Token
  To "login" to your bot through our program, place a file named `config.py` in your src directory with the content:
  
  ```
  token = ************(your discord bot token)
  ```
  
### Intall required packages
  ```
  pip install -r requirements.txt
  ```
### Run the schedulebot.py
  ```
  python3 schedulebot.py
  ```
  Then your scheduleBot should start working.

## Ways to Contribute

### Report bugs
Report any issues you encounter while using or contributing to this repository as a new github issue, using the Bug tag. When reporting a bug please describe:
1. Any preconditions (your operating system, status of your data, files that the program may access, and if the program is running on an external drive)
2. Sequence of actions from the initial execution of the program to the bug.
3. Expected behavior (i.e. if the bug was not there).
4. Actual behavior (i.e. the effect of the bug).

### Suggest enhancements
Suggestions are very much welcome. If you have a suggestion for this project, please report it as a github issue, using the Feature Request tag, and provide the following information:
- Use a clear, descriptive title.
- Provide as many details as posible on how do you envision this feature:
  - Provide a step-by-step of any process.
  - Attach a prototype if it requires an UI change.
- Explain *why* you believe this contribution is worthwhile.

### Contribute code
We use git flow in this repo. If you want to contribute through code, please fork an existing branch to work on your feature. If you're working on a current issue, respond to that issue with "I'm working on this". When you are done, submit a pull request to join your contribution to the branch you forked. Before submiting your request, please:
- Implement functional, passing test cases that test your contribution
- Check that all previous test cases and other status checks are passing.

## Style guidelines
### Git commit
- Use present tense ("Add feature", not "Added feature")
- Use imperative mood ("Move cursor to...", not "Moves cursor to...")
- Keep the first line to once sentence.

### Python style guide
Please follow the [PEP8 guide](https://www.python.org/dev/peps/pep-0008/) for Python. In addition, please follow the following conventions:
- Use underscores to separate words in non class names: n_samples rather than nsamples.
- Use relative imports for code. For test cases, use absolute imports.
- Do not use import \*, as it has been discouraged by the [official Python recommendations](https://docs.python.org/3.1/howto/doanddont.html#at-module-level).

### Documentation
- Use pdoc3
