class StateMachine:
    def __init__(self):
        self.handlers = {}
        self.startState = None
        self.endStates = []

    def add_state(self, name, handler, end_state=0):
        name = name.upper()
        self.handlers[name] = handler
        if end_state:
            self.endStates.append(name)

    def set_start(self, name):
        self.startState = name.upper()

    def run(self, cargo):
        try:
            print("cargo->{0}".format(cargo))
            print("self.startState->{0}".format(self.startState))
            handler = self.handlers[self.startState]
        except:
            raise ValueError("must call .set_start() before .run()")
        if not self.endStates:
            raise  ValueError("at least one state must be an end_state")
    
        while True:
            (newState, cargo) = handler(cargo)
            print("new state = {0} & new word = {1}".format(newState,cargo))
            if newState.upper() in self.endStates:
                print("reached ", newState)
                print("---------------")
                break 
            else:
                handler = self.handlers[newState.upper()]