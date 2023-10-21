class Utility:
    def __init__(self):
        self.time_remaining = 0
        self.corrected_cpm = 0
        self.net_wpm = 0
        self.board_cpm = 0
        self.board_wpm = 0
        self.current_date = None
        self.data = {}
        self.save_data = False
        self.current_word = ""
        self.current_count = 0
        self.words_displayed = None
        self.letter_text = ""
        self.words_typed = []
        self.entry_typed = []
        self.timer_start = False
        self.entry_text = ""
        self.skipped = False
        self.position = 0
        self.mistakes = 0
        self.pass_points = 0
        self.word_list = []
        self.current_char = ""
