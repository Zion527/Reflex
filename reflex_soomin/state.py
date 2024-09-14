import reflex as rx 

class State(rx.State):
    # 참고: 
    count: int = 0

    def increment(self):
        self.count += 1

    def decrement(self):
        self.count -= 1


