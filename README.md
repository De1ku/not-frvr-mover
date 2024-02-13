# not-frvr-mover
A funny script to move user across all the voice channels available you for moving

You must have the MOVE-MEMBER privilege to use it.

When using the script, you must authorize to it via a discord token. How to get a Discord token:
>1. Firstly you need to open dev console _(CTRL-SHIFT-I in Discord and F12 in other browsers)_
>2. Open the **Network tab**
>![image](https://github.com/De1ku/not-frvr-mover/assets/125497407/b5066cfe-d0fe-4da2-a611-f7c14e9b4191)
>3. **Filter** the requests by **"/api"**, perform some action (e.g. open a page of some server) and open the request
>4. **Find** the **"authorization"** header in the request headers and copy its contents. Done! You have your token, through which you can authorize in the script to your discord account _(The token changes when you log out of your account, keep this in mind. The token you have now may be invalid after logging out of the account on any device)_
>![image](https://github.com/De1ku/not-frvr-mover/assets/125497407/5ad6feeb-801c-41e1-9d95-2576e0eb079c)

Script uses **"requests"**, **"rich"** and **"inquirer"** modules. To install them, go to the script directory and install the modules from requirements.txt **(pip install requirements.txt)**

![image](https://github.com/De1ku/not-frvr-mover/assets/125497407/94666d44-0d89-4439-8677-22e3e9aef760)
