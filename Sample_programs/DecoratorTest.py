
commands = {
    }

def add_cmd(cmd_lable):
    def inner(functionName):
        commands [cmd_lable] = functionName 
    return inner 

@add_cmd("date")
def show_date():
    return "thu 12 aug 2018"

@add_cmd("pwd")
def show_pwd():
    return "/root"

def process_input(cmd):
    if cmd in commands:
        method =  commands[cmd]
        response = method()
        print response

cmd  = raw_input("please enter cmd:")
process_input(cmd)
