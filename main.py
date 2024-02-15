import requests
import time
import json
from rich.console import Console
import inquirer


"""
 _      ____  _____    _____ ____  ____  _____ _     _____ ____    _      ____  _     _____ ____ 
/ \  /|/  _ \/__ __\  /    //  _ \/  __\/  __// \ |\/  __//  __\  / \__/|/  _ \/ \ |\/  __//  __\
| |\ ||| / \|  / \    |  __\| / \||  \/||  \  | | //|  \  |  \/|  | |\/||| / \|| | //|  \  |  \/|
| | \||| \_/|  | |    | |   | \_/||    /|  /_ | \// |  /_ |    /  | |  ||| \_/|| \// |  /_ |    /
\_/  \|\____/  \_/    \_/   \____/\_/\_\\____\\__/  \____\\_/\_\  \_/  \|\____/\__/  \____\\_/\_\
                 """                                                                                



defaultHeaders = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chr*ome/121.0.0.0 Safari/537.36 Edg/121.0.0.0",
                      "authorization": "",
                      "content-type": "application/json"}

nums = [1,2,3,4,5,6,7,8,9,0]

with open("config.json", "r") as file:
    config = json.load(file)

def parseTargetsIds() -> str:
    targetsChoices = [i for i in config['targets'].keys()]
    targetsChoices.append("Add new")
    targetsChoices.append("Del one")
    questions = [
    inquirer.List('choice',
        message="Choose the target:",
        choices=targetsChoices,
    ),
]
    answers = inquirer.prompt(questions)
    if answers["choice"] == "Add new":
        slowType("Type new target id: ")
        targetId = console.input("")
        req = requests.get(f"https://discord.com/api/v9/users/{targetId}", headers=defaultHeaders)
        res = req.json()
        if req.status_code == 200:
            targetName = res['username']
            slowType(f'Adding target with username "{targetName}"')
            config['targets'][targetName] = targetId
            with open("config.json", "w") as file:
                json.dump(config, file)
            return False

        else:
            slowType(f"Invalid id!")
            return False
    
    elif answers["choice"] == "Del one":
        targetsToDel = [
            inquirer.List('choice',
                message="Choose the guild to delete:",
                choices=[i for i in config['guilds'].keys()],
            ),
        ]
        nameToDel = inquirer.prompt(targetsToDel)
        nameToDel = nameToDel['choice']
        if nameToDel in config['targets'].keys():
            slowType(f"Deleting {nameToDel} (id: {config['targets'][nameToDel]})")
            del config['targets'][nameToDel]

            with open("config.json", "w") as file:
                json.dump(config, file)
            return False
        else:
            slowType("Invalid username")
            return False
    
    else:
        targetName = answers['choice']
        slowType(f'You picked "{targetName}"!')
        return config['targets'][targetName]


def parseGuildsIds() -> str:
    guildChoices = [i for i in config['guilds'].keys()]
    guildChoices.append("Add new")
    guildChoices.append("Del one")
    questions = [
    inquirer.List('choice',
        message="Choose the guild:",
        choices=guildChoices,
    ),
]
    answers = inquirer.prompt(questions)
    if answers["choice"] == "Add new":
        slowType("Type new guild id: ")
        guildId = console.input("")
        req = requests.get(f"https://discord.com/api/v9/guilds/{guildId}", headers=defaultHeaders)
        res = req.json()
        if req.status_code == 200:
            guildName = res['name']
            slowType(f'Adding guild with the name "{guildName}"')
            config['guilds'][guildName] = guildId
            with open("config.json", "w") as file:
                json.dump(config, file)
            return False

        else:
            slowType(f"Invalid id!")
            return False
    
    elif answers["choice"] == "Del one":
        guildsToDel = [
            inquirer.List('choice',
                message="Choose the guild to delete:",
                choices=[i for i in config['guilds'].keys()],
            ),
        ]
        nameToDel = inquirer.prompt(guildsToDel)
        nameToDel = nameToDel['choice']
        if nameToDel in config['guilds'].keys():
            slowType(f"Deleting {nameToDel} (id: {config['guilds'][nameToDel]})")
            del config['guilds'][nameToDel]

            with open("config.json", "w") as file:
                json.dump(config, file)
            return False
        else:
            slowType("Invalid guild name")
            return False
    
    else:
        guildName = answers['choice']
        slowType(f'You picked "{guildName}"!')
        return config['guilds'][guildName]
    

def getToken() -> None:
    clearConsole()
    authToken = console.input("Type your authentication token: ")
    defaultHeaders['authorization'] = authToken
    res = requests.get("https://discord.com/api/v9/users/@me", headers=defaultHeaders)
    if res.status_code == 200:
        slowType("Got it! ")
        res_json = res.json()
        user_data = {'global_name': res_json['global_name'],
                    'user_name': res_json["username"],
                    'user_id': res_json['id']}
        slowType(f"Logging by: {user_data['user_name']}")
        return True
    else:
        slowType("Invalid token!")
        return False

def slowType(line, newLine=True) -> None:
    for i in line:
        console.print(i, end="", new_line_start=newLine)
        time.sleep(0.02)

def clearConsole() -> None:
    console.clear()
    console.print("WELCOME TO SCRIPT BY", justify="center", style="blink bold underline")
    console.print("""
███╗   ██╗ ██████╗ ████████╗    ███████╗██████╗ ██╗   ██╗██████╗
████╗  ██║██╔═══██╗╚══██╔══╝    ██╔════╝██╔══██╗██║   ██║██╔══██╗
██╔██╗ ██║██║   ██║   ██║       █████╗  ██████╔╝██║   ██║██████╔╝
██║╚██╗██║██║   ██║   ██║       ██╔══╝  ██╔══██╗╚██╗ ██╔╝██╔══██╗
██║ ╚████║╚██████╔╝   ██║       ██║     ██║  ██║ ╚████╔╝ ██║  ██║
╚═╝  ╚═══╝ ╚═════╝    ╚═╝       ╚═╝     ╚═╝  ╚═╝  ╚═══╝  ╚═╝  ╚═╝
""", justify="center")
    console.print("TEAM", justify="center", style="blink bold underline")

def main(defaultHeaders) -> None:
    clearConsole()
    console.bell()

    slowType("Enter to continue: ", False)
    _xuinya=input("")
    tokenCycleSwitcher = False
    while tokenCycleSwitcher == False:
        tokenCycleSwitcher = getToken() # To write token to headers
    time.sleep(2)
    clearConsole()
    targetId = False
    while targetId == False:
        targetId = parseTargetsIds()
        time.sleep(2)
        clearConsole()

    guildId = False
    while guildId == False:
        guildId = parseGuildsIds()
        time.sleep(2)
        clearConsole()

    getChannels = requests.get(f"https://discord.com/api/v9/guilds/{guildId}/channels", headers=defaultHeaders)
    allChannels = getChannels.json()
    allVoiceChannels = []

    for i in allChannels:
        if i['type'] == 2:
            allVoiceChannels.append(i['id'])
    
    numToRepeat = console.input("Type the num to repeat the cycle: ")

    for j in range(int(numToRepeat)):
        for i in allVoiceChannels:
            moveMember = requests.patch(f"https://discord.com/api/v9/guilds/{guildId}/members/{targetId}", headers=defaultHeaders, json={"channel_id": i})
            print(moveMember)
            time.sleep(0.1)

if __name__=="__main__":
    console = Console(width=100, style = "magenta")
    console.set_window_title("NOT FRVR MOVER")
    main(defaultHeaders)
