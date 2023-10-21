import copy
import random
from tkinter import *
from tkinter import ttk
import datetime as dt
from utilities import Utility


class Interface:
    def __init__(self):
        self.window = Tk()
        self.window.title("Typing Speed Test")
        self.window.configure(bg="#FFCC70")
        self.window.config(padx=30, pady=50)
        self.window.grid_rowconfigure(0, weight=1)
        self.window.grid_columnconfigure(0, weight=1)
        self.style = ttk.Style(self.window)
        self.style.theme_use("alt")
        self.style.configure('.', focuscolor=self.style.lookup('.', 'background'))
        self.background = Frame(self.window, background="#FFFADD")
        self.background.grid(row=0, column=0, sticky="NWES")
        self.inner_background = Frame(self.window, background="#FFFADD")
        self.inner_background.grid(row=0, column=0, sticky="NWES")
        self.util = Utility()

        # Creating the widgets
        self.title_frame = Frame(self.inner_background, background="#FFFADD")
        self.title_frame.grid(row=0, column=1)
        self.style.configure("Title.TLabel", font=("Calibri", 50))
        self.title = ttk.Label(self.title_frame, text="🆃🆈🅿🅸🅽🅶 🆂🅿🅴🅴🅳 🆃🅴🆂🆃", background="#FFFADD", foreground="#000000",
                               style="Title.TLabel")
        self.title.grid(row=0, column=0, pady=5, padx=50)

        self.style.configure("Description.TLabel", font=("Calibri", 16))
        self.description = ttk.Label(self.inner_background,
                                     text="How quick are your fingers? Take the one-minute typing "
                                          "test to find out! After each word, hit the space bar. \n"
                                          "Finally, you will be given your typing speed in CPM and "
                                          "WPM. Good luck!", background="#FFFADD",
                                     foreground="#000000",
                                     style="Description.TLabel", justify="center")
        self.description.grid(row=1, column=1, pady=5, padx=50)

        self.style.configure("Highscore.TLabel", font=("Calibri", 26))
        self.highscore_text = ttk.Label(self.inner_background, text="𝙷𝙸𝙶𝙷𝚂𝙲𝙾𝚁𝙴", background="#FFFADD",
                                        foreground="#000000",
                                        style="Highscore.TLabel")
        self.highscore_text.grid(row=2, column=1, pady=5, padx=50)

        self.style.configure("Score.TLabel", font=("Calibri", 26))

        self.date = dt.datetime.now().strftime("%d-%m-%y")
        self.record_highscore()
        self.scoreboard_text = Label(self.inner_background, text=f"{self.util.current_date}, {self.util.board_cpm} "
                                                                 f"CPM({self.util.board_wpm} WPM)",
                                     background="#ffffff", width=30, bd=5,
                                     fg="#000000", relief="sunken", font=("Courier New", 16, "bold"))
        self.scoreboard_text.grid(row=3, column=1)

        # Use a LabelFrame cause of the borders
        self.text_frame = LabelFrame(self.inner_background, background="#ffffdd", padx=20, pady=10)
        self.text_frame.grid(row=4, column=1, padx=30, pady=20, sticky="NWES")

        self.inner_text_frame = LabelFrame(self.text_frame, background="#FFFFDD", padx=20, pady=10)
        self.inner_text_frame.grid(row=1, column=0, columnspan=7, padx=30, pady=5, sticky="NWES")

        self.style.configure("Text.TLabel", font=("Calibri", 16))
        self.cpm_details = ttk.Label(self.inner_text_frame, text="Corrected CPM: ", background="#FFFADD",
                                     foreground="#000000",
                                     style="Text.TLabel", justify="center")
        self.cpm_details.grid(row=0, column=0, padx=(20, 0))

        self.cpm_text = Label(self.inner_text_frame, text="?", background="#ffffff", width=5, bd=3, fg="#000000",
                              relief="sunken", font=("Calibri", 16))
        self.cpm_text.grid(row=0, column=1)

        self.wpm_details = ttk.Label(self.inner_text_frame, text="WPM: ", background="#FFFADD",
                                     foreground="#000000",
                                     style="Text.TLabel", justify="center")
        self.wpm_details.grid(row=0, column=2, padx=10)

        self.wpm_text = Label(self.inner_text_frame, text="?", background="#ffffff", width=5,
                              bd=3, fg="#000000", relief="sunken", font=("Calibri", 16))
        self.wpm_text.grid(row=0, column=3)

        self.mistake_details = ttk.Label(self.inner_text_frame, text="Mistakes: ", background="#FFFADD",
                                         foreground="#000000",
                                         style="Text.TLabel", justify="center")
        self.mistake_details.grid(row=0, column=5, padx=10)

        self.mistake_text = Label(self.inner_text_frame, text=f"{self.util.mistakes}", background="#ffffff",
                                  width=5, bd=3, fg="#000000", relief="sunken", font=("Calibri", 16))
        self.mistake_text.grid(row=0, column=6)

        self.time_details = ttk.Label(self.inner_text_frame, text="Time Left: ", background="#FFFADD",
                                      foreground="#000000",
                                      style="Text.TLabel", justify="center")
        self.time_details.grid(row=0, column=7, padx=10)

        self.time_text = Label(self.inner_text_frame, text="0", background="#ffffff",
                               width=5, bd=3, fg="#000000", relief="sunken", font=("Calibri", 16))
        self.time_text.grid(row=0, column=8)

        self.restart_button = ttk.Button(self.inner_text_frame, text="Restart", command=self.restart)
        self.restart_button.grid(row=0, column=9, sticky="e", padx=(60, 20))

        self.inner_text_frame_0 = LabelFrame(self.text_frame, background="#FFFFDD", padx=20, pady=10)
        self.inner_text_frame_0.grid(row=2, column=0, columnspan=7, padx=10, pady=10)

        self.generated_text = Text(self.inner_text_frame_0, background="#ffffff", width=50, wrap=WORD,
                                   foreground="#000000", bd=3, height=10,
                                   font=("Courier New", 21, "bold"))
        self.generated_text.bind("<Key>", self.ignore_input)
        self.generated_text.grid(row=0, column=0, padx=10)

        self.show_score = Text(self.inner_text_frame_0, background="#22668D", width=50, wrap=WORD,
                                   foreground="#ffffff", bd=3, height=10, pady=20,
                                   font=("Courier New", 21, "bold"))
        self.show_score.insert("1.0", " ")
        self.show_score.tag_configure("center", justify='center')
        self.show_score.tag_add("center", "1.0", "end")
        self.show_score.bind("<Key>", self.ignore_input)
        self.show_score.grid(row=0, column=0, padx=10)
        self.show_score.grid_remove()

        self.string_words = StringVar()
        self.string_words.trace_add('write', self.timer_callback)
        self.placeholder = "Type the words here"
        self.word_text = ttk.Entry(self.inner_text_frame_0, background="#FFFADD", textvariable=self.string_words,
                                   width=72, foreground="gray")
        self.word_text.insert(0, self.placeholder)
        self.word_text.grid(row=1, column=0, pady=10)
        self.word_text.bind("<FocusIn>", self.typing_start)
        self.word_text.bind("<FocusOut>", self.typing_stop)
        self.word_text.bind("<Key>", self.check_spelling)

        self.get_words()
        self.change_text()

    def typing_start(self, event):
        """Check if the user has the entry in focus. Delete the placeholder"""
        start_words = self.word_text.get()
        if start_words == self.placeholder:
            self.word_text.delete(0, END)
            self.word_text.config(foreground="black")

    def typing_stop(self, event):
        if not self.word_text.get():
            self.word_text.insert(0, self.placeholder)
            self.word_text.config(foreground="gray")

    def ignore_input(self, event):
        """Make the text widget uneditable"""
        return "break"

    def check_spelling(self, event):
        """This will check each spelling of the text"""
        current_word = self.get_next_word(self.util.current_count)
        self.util.current_char = current_word
        entry_text = self.util.entry_text

        # Check if the entry text is the same as the placeholder and ignore it
        if entry_text == self.placeholder:
            return

        if event.keysym == "space":
            # Checks for space and performs submission
            if len(entry_text) >= len(current_word):
                self.word_pop(entry_text, current_word)
            elif len(self.word_text.get()) >= 1:
                self.util.skipped = True
                self.word_pop(entry_text, current_word)
            self.util.current_word = ''
            return 'break'

        elif event.keysym == "BackSpace":
            self.recall_letter()

        elif event.char != " ":
            self.util.current_word += event.char
            self.util.total_chars += 1
        curr_char = len(self.util.current_word) - 1
        selected_word = self.util.words_displayed_copy[self.util.current_count]

        if len(self.util.current_word) > len(self.util.words_displayed_copy[self.util.current_count]):
            self.util.position = (len(''.join(self.util.words_displayed_copy[:self.util.current_count])) +
                                  len(self.util.entry_typed) + len(selected_word) - 1)
        else:
            self.util.position = (len(''.join(self.util.words_displayed_copy[:self.util.current_count])) +
                                  len(self.util.entry_typed) + len(self.util.current_word) - 1)


        if event.keysym != "space" and event.keysym != "BackSpace":
            try:
                if current_word[curr_char] == event.char:
                    self.check_mistake_pass_points(event.char, current_word[curr_char])
                    self.show_correct()
                else:
                    self.check_mistake_pass_points(event.char, current_word[curr_char])
                    self.show_incorrect()
            except IndexError:
                return

    def show_correct(self):
        char_length = self.util.position
        self.generated_text.tag_config("#0000ff", foreground="#0000ff")
        char = self.util.letter_text[char_length]
        self.generated_text.delete(f"1.{char_length}")
        self.generated_text.insert(f"1.{char_length}", char)
        self.generated_text.tag_add("#0000ff", f"1.{char_length}")

    def show_incorrect(self):
        char_length = self.util.position
        self.generated_text.tag_config("#c00", foreground="#c00")
        char = self.util.letter_text[char_length]
        self.generated_text.delete(f"1.{char_length}")
        self.generated_text.insert(f"1.{char_length}", char)
        self.generated_text.tag_add("#c00", f"1.{char_length}")

    def check_mistake_pass_points(self, char, letter):
        """If a word was skipped or over typed, check the word to color it """
        if char != letter:
            self.util.mistakes += 1
        elif char == letter:
            self.util.pass_points += 1

    def update_typing_score(self):
        """Update the scoreboard with the typing score"""
        if int(self.time_text["text"]) > 0:
            self.util.corrected_cpm = self.util.pass_points
            self.util.net_wpm = (
                int(((self.util.pass_points / 5) - (self.util.mistakes * ((int(self.time_text['text'])) / 60))) /
                    ((int(self.time_text['text'])) / 60)))
            if self.util.net_wpm < 0:
                self.util.net_wpm = 0

            self.mistake_text["text"] = self.util.mistakes
            self.wpm_text["text"] = self.util.net_wpm
            self.cpm_text["text"] = self.util.corrected_cpm

    def display_score(self):
        data = ""
        cpm = int(self.util.pass_points)
        wpm = int((self.util.pass_points / 5) / ((int(self.time_text['text'])) / 60))
        net_wpm = (
            int(((self.util.pass_points / 5) - (self.util.mistakes * ((int(self.time_text['text'])) / 60))) /
                ((int(self.time_text['text'])) / 60)))
        accuracy = int((net_wpm * 100) / wpm)
        if 0 <= net_wpm <= 20:
            data = f"You can do better! You type with the speed of \n\n{net_wpm} WPM ({cpm} CPM). \n\nYour accuracy was {accuracy}%. \n\nKeep practicing!"
        elif 20 < net_wpm <= 50:
            data = f"Nice! You type with the speed of \n\n{net_wpm} WPM ({cpm} CPM). \n\nYour accuracy was {accuracy}%. \n\nKeep practicing!"
        elif net_wpm > 50:
            data = f"Congratulations! You type with the speed of \n\n{net_wpm} WPM ({cpm} CPM). \n\nYour accuracy was {accuracy}%. \n\nKeep it up!"

        self.show_score.grid()
        self.show_score.insert(END, data)


    def recall_letter(self):
        """if the backspace has been clicked, it gets the current index of the generated text"""
        char_length = self.util.position
        words_typed = self.util.words_typed
        user_typed = self.util.entry_typed

        # Checks if the entry is empty on backspace, so it gets the word from the list
        if char_length > 0 and len(self.util.current_word) == 0:
            try:
                if words_typed and user_typed and self.util.current_count > 0:
                    previous_word = words_typed[-1]
                    self.util.words_typed.remove(previous_word)
                    # minus the count that gets the next word
                    self.util.current_count -= 1
                    self.word_text.insert(0, user_typed[self.util.current_count] + " ")
                    self.util.current_word = user_typed[self.util.current_count]
                    self.util.entry_typed = self.util.entry_typed[:-1]

                    # get the difference when it is being removed from the list
                    if previous_word != self.util.last_user_word:
                        change_in_char_length = len(previous_word) + 1 - len(self.util.current_word)
                        self.util.position -= change_in_char_length
            except IndexError as e:
                pass

        elif self.util.current_word != 0:
            try:
                current_count = self.util.current_count
                current_word = self.util.current_word
                length = len(current_word) - 1
                my_word = self.util.words_displayed_copy[current_count][length]
                try:
                    if current_word[-1] == my_word:
                        if self.util.pass_points > 0:
                            self.util.pass_points -= 1
                except ValueError:
                    pass
                self.show_original_letter()
            except IndexError as e:
                pass

            self.util.current_word = self.util.current_word[:-1]

    def show_original_letter(self):
        char_length = self.util.position
        current_char = self.util.current_word[-1]
        my_word = self.util.words_displayed_copy[self.util.current_count][len(self.util.current_word) - 1]
        if my_word == current_char or my_word != current_char and len(self.util.current_char) >= len(
                self.util.current_word):
            self.generated_text.tag_config("#000000", foreground="#000000")
            char = self.util.letter_text[char_length]
            self.generated_text.delete(f"1.{char_length}")
            self.generated_text.insert(f"1.{char_length}", char)
            self.generated_text.tag_add("#000000", f"1.{char_length}")

    def word_pop(self, entry_text, current_word):
        """Clears the entry for the next word"""
        if entry_text:
            self.util.entry_typed.append(entry_text)
        # checks if user skipped a word and add it to the char length to maintain the generated text index
        if self.util.skipped:
            self.util.position += len(current_word) + 1 - len(self.util.entry_typed[-1])
            self.util.skipped = False
        else:
            pass
        self.util.spacebar = False
        self.util.words_typed.append(current_word)
        self.util.current_count += 1
        self.word_text.delete(0, END)
        self.util.entry_text = ""

    def get_next_word(self, index):
        """Gets each word one by one"""
        if self.util.words_displayed is not None:
            if 0 <= index < len(self.util.words_displayed):
                return self.util.words_displayed[index]
            return None

    def record_highscore(self):
        """Save the data in a file"""
        try:
            with open("data.txt", "r") as scores:
                for score in scores:
                    key, value = score.strip().split(': ')
                    self.util.data[key] = value
            wpm = self.util.data.get("wpm", 0)
            cpm = self.util.data.get("cpm", 0)
            self.util.current_date = self.util.data.get("date", self.date)
            if int(self.util.net_wpm) > int(wpm):
                self.util.board_wpm = self.util.net_wpm
            else:
                self.util.board_wpm = wpm
            if int(self.util.corrected_cpm) > int(cpm):
                self.util.board_cpm = self.util.corrected_cpm
            else:
                self.util.board_cpm = cpm
            if self.util.save_data:
                with open("data.txt", "w") as record:
                    record.write(f"wpm: {self.util.board_wpm}\ncpm: {self.util.board_cpm}\ndate: {self.date}")
                self.util.save_data = False
        except FileNotFoundError:
            with open("data.txt", "w") as score:
                score.write(f"cpm: 0\nwpm: 0\ndate: {self.date}")

    def timer_callback(self, var, index, mode):
        self.util.entry_text = self.word_text.get()
        self.update_typing_score()
        self.checks_timer()

    def checks_timer(self):
        """Checks when a user has started typing"""
        if len(self.util.current_word) == 1 and not self.util.timer_start:
            self.util.timer_start = True
            self.timer_countdown(0)

    def timer_countdown(self, count):
        """Starts the timer countdown"""
        if self.util.timer_start:
            if count == 60:
                self.util.save_data = True
                self.record_highscore()
                self.display_score()
                self.reset_time()
                self.scoreboard_text.config(text=f"{self.util.current_date}, {self.util.board_cpm} "
                                                 f"CPM({self.util.board_wpm} WPM)")
            else:
                self.util.time_remaining = self.window.after(1000, self.timer_countdown, count + 1)
                self.time_text["text"] = count

    def reset_time(self):
        """Call the reset time after countdown"""
        self.util.timer_start = False
        self.word_text.config(state="disabled")
        self.time_text["text"] = "0"
        if self.util.time_remaining is not None:
            self.window.after_cancel(self.util.time_remaining)
        self.util.time_remaining = 0

    def restart(self):
        self.util.timer_start = False
        self.word_text.config(state="normal")

        if self.util.time_remaining is not None:
            self.window.after_cancel(self.util.time_remaining)

        try:
            self.window.destroy()
            Interface()
        except ValueError:
            Interface()

    def generate_words(self, words_list):
        """"Generates 20 random words and keeps a copy of it"""
        sample_size = min(60, len(words_list))
        self.util.words_displayed = random.sample(words_list, sample_size)
        self.util.words_displayed_copy = copy.copy(self.util.words_displayed)
        return " ".join(self.util.words_displayed)

    def get_words(self):
        with open("english_words.txt") as text:
            all_text = text.read()
            words = list(map(str, all_text.split()))
            for word in words:
                self.util.word_list.append(word)

    def change_text(self):
        """"render the words on the Text widget and keeps a copy of it"""
        self.util.letter_text = self.generate_words(self.util.word_list)
        self.util.letter_text_copy = copy.copy(self.util.letter_text)
        self.generated_text.delete("1.0", END)
        self.generated_text.insert("1.0", self.util.letter_text)
