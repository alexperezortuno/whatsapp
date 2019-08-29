# Whatsapp message sender

This script uses Selenium to open a new google chrome window and go to web WhatsApp and send messages to visible history users

### Requirements
- pip
- virtualenv

### Installation

```
$ sudo chmod +x install
$ ./install
```

### Usage

```
$ source env/bin/activate
$ python main.py
```

You can terminate the script in any moment pressing CTRL + C

### Additional options
You can modify the main.py file and set static variables
Example:
```
static_name = "name to send message"
static_message = "my static message"
static_count = 1

start_script = Whatsapp(name=static_name,
                        message=static_message, 
                        count=static_count)
start_script.start()
```
