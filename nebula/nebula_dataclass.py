from dataclasses import dataclass
from random import random, randrange


#Dataclass Pattern
@dataclass
class NebulaDataClass:
    """Dataclass containing all the data emissions
    and user input to and from Nebula"""

    move_rnn: float = random()
    """Net 1 raw emission"""

    affect_rnn: float = random()
    """Net 2 raw emission"""

    move_affect_conv2: float = random()
    """Net 3 raw emission"""

    affect_move_conv2: float = random()
    """Net 4 raw emission"""

    master_output: float = random()
    """Master output from the affect process"""

    user_in: float = random()
    """Percept input stream from client e.g. live mic level"""

    rnd_poetry: float = random()
    """Random stream to spice things up"""

    affect_net: float = random()
    """Output from affect module"""

    self_awareness: float = random()
    """Net that has some self awareness - ???"""

    affect_decision: str = " "
    """Current stream chosen by affect process"""

    rhythm_rate: float = randrange(30, 100) / 100
    """Internal clock/ rhythm sub division"""

    # eeg_board: list
    """Live data from brainbit"""

    eda: int = 0
    """Live data from Bitalino"""


#DataBorg Pattern
class DataBorg:

    __shared_state = {}

    def __init__(self):
        self.__dict__ = self.__shared_state

        self.move_rnn: float = random()
        """Net 1 raw emission"""

        self.affect_rnn: float = random()
        """Net 2 raw emission"""

        self.move_affect_conv2: float = random()
        """Net 3 raw emission"""

        self.affect_move_conv2: float = random()
        """Net 4 raw emission"""

        self.master_output: float = random()
        """Master output from the affect process"""

        self.user_in: float = random()
        """Percept input stream from client e.g. live mic level"""

        self.rnd_poetry: float = random()
        """Random stream to spice things up"""

        self.affect_net: float = random()
        """Output from affect module"""

        self.self_awareness: float = random()
        """Net that has some self awareness - ???"""

        self.affect_decision: str = " "
        """Current stream chosen by affect process"""

        self.rhythm_rate: float = randrange(30, 100) / 100
        """Internal clock/ rhythm sub division"""

        self.rnd_stream: str = ""
        """Stream name currently used for active data"""

        self.eeg: list = [0, 0, 0, 0]
        """Live data from brainbit"""

        self.eda: int = 0
        """Live data from Bitalino"""

    def randomiser(self):
        """ Blitz's the DataBorg dict with random numbers"""
        self.move_rnn = random()
        self.affect_rnn = random()
        self.move_affect_conv2 = random()
        self.affect_move_conv2 = random()
        self.master_output = random()
        self.user_in = random()
        self.rnd_poetry = random()
        self.affect_net = random()
        self.self_awareness = random()
        # self.affect_decision = ""
        self.rhythm_rate = randrange(30, 100) / 100
        # self.rnd_stream = ""
        self.eeg = [0, 0, 0, 0]


        # if not DataBorg.__monostate:
        #     DataBorg.__monostate = self.__dict__
            # self.borg_dict = {"move_rnn": random(),
            #                   "affect_rnn": random(),
            #                   "move_affect_conv2": random(),
            #                   "affect_move_conv2": random(),
            #                   "master_output": random(),
            #                   "user_in": random(),
            #                   "rnd_poetry": random(),
            #                   "affect_net": random(),
            #                   "self_awareness": random(),
            #                   "affect_decision": "",
            #                   "rhythm_rate": randrange(30, 100) / 100,
            #                   "rnd_stream": "",
            #                   "eeg_board": [0, 0, 0, 0],
            #                   }






            #
            # self.fields = [self.move_rnn,
            #                self.affect_rnn,
            #                self.move_affect_conv2,
            #                self.affect_move_conv2,
            #                self.master_output,
            #                self.user_in,
            #                self.rnd_poetry,
            #                self.affect_net,
            #                self.self_awareness,
            #                self.affect_decision,
            #                self.rhythm_rate,
            #                self.eeg_board
            #                ]
        #
        # else:
        #     self.__dict__ = DataBorg.__monostate
        #
