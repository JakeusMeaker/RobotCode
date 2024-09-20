## WebPigeon was 'ere
## lock your machine, innit.

class base_state(object):

    def enter(self):
        pass

    def tick(self):
        pass

    def exit(self):
        pass


class state(base_state):
    def __init__(self, manager, robot, speed, angle):
        super(state, self).__init__()
        self.manager = manager
        self.robot = robot
        self.speed = speed
        self.angle = angle

    def enter(self):
        super(state, self).enter()
        pass

    def tick(self):
        super(state, self).tick()

        # example: self.manager.set_state("blarg")
        pass

    def exit(self):
        super(state, self).exit()
        pass

class state_manager():

    def __init__(self):
        """Create the state manager"""
        self.curr_state = None
        self.states = {}

    def add_state(self, name, state):
        """Register a new state via name"""
        self.states[name] = state
        self.states[name].manager = self

    def set_state(self, state):
        """Update the current state"""
        if self.curr_state is not None:
            self.curr_state.exit()
        self.curr_state = self.states[state]
        self.curr_state.enter()

    def tick(self):
        """Tick the current state?"""
        if self.curr_state is None:
            return
        self.curr_state.tick()
    
