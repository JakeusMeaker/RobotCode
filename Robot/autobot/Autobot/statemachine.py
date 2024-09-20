import state

class statemachine():

    def __init__():
        self.current_state = state

    def switchstate(new_state):
        current_state.Exit()
        current_state = new_state
        current_state.Enter()

    def update()
    {
        dt = clock.tick(FPS) / 1000
        current_state.tick(dt)
    }
