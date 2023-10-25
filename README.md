# BeyBlade Battle Simulator

Thomas Loo - T1A3 - Terminal App

## Links

- [Github Repository](https://github.com/NeggFriedRice/terminal_app)
- [Trello](https://trello.com/invite/b/z6dHuYUU/ATTIe6504be03f81ae2c10268f144856b9a937278F7B/t1a3-kanban)
- Presentation

## Code style
- PEP8 style

Please note that Line 458 of class.py file and ASCII banner art in art.py excceeds the 79 character limit due to long variable name and nesting.
# Help Documentation

### Operating system and hardware requirements

- Modern Operating System:
    - Windows 7 or 10
    - Mac OS X 10.11 or higher, 64-bit
    - Linux: RHEL 6/7, 64-bit (almost all libraries also work in Ubuntu)
    - 4 GB RAM
    - 5 GB free disk space

- Software:
    - Python 3.10 or higher
    - Terminal application

- Hardware:
    - Keyboard

# Installation Instructions

1. If you are a Microsoft Windows user you will not be able to run this app without the Windows Subsystem for Linux (WSL). If you have not previously installed WSL please follow the below guide for setup:

    https://learn.microsoft.com/en-us/windows/wsl/install

1. Check that you have Python installed. Open your terminal and execute the following command:

    ```
    python3 --version
    ```

    Your terminal should return the below, or similar:

    ```
    Python 3.10.12
    ```
    If Python is not installed you will receive the following message and will need to download Python:
    ```
    'python3' not found
    ```
    Please head over to Python's website to download the latest version of Python and follow the guide for instructions.

    https://www.python.org/downloads/

1. Clone the app repository to your local environment
    ```
    git clone https://github.com/NeggFriedRice/terminal_app.git
    ```
1. Navigate to the folder that contains the app
    ```
    cd terminal_app
    ```
1. Run the bash script with:
    ```
    bash beyblade.sh
    ```
    This bash script will do the following:
    - Check whether Python 3 has been installed on yoru system
    - Create and activate a virtual environment
    - Install the required dependencies (please see 'Dependencies' section for more information)
    - Run the app file
    - Deactivate the virtual environment when the app is closed

    If you encounter issues running the bash script, enter the following into the terminal
    ```
    chmod +x beyblade.sh 
    ```
1. Enjoy the game!

# Dependencies

```
colorama==0.4.6
```
# How to play the game
- You have arrived on the scene of an international BeyBlade tournament
- To take the win you will need to win at least 2 out of 3 rounds and have enough money leftover to fly home

- The game will require keyboard inputs to navigate through the different sections.

    ![HUD](./docs/HUD.png)

    ![Upgrades shop](./docs/SHOP.png)
- That's it! Enjoy yourself