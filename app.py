from libpockey import Pockey


class App:
    TARGET_FPS = 5

    def __init__(self, pockey: Pockey):
        self.pockey = pockey

    def setup(self):
        pass

    def mainloop(self):
        pass

    def teardown(self):
        pass

    def handle_button(self, number, edge):
        pass