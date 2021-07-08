import tkinter as tk
import logging

logging.basicConfig(level=logging.INFO)


class ChatGui:
    def __init__(self):
        self._root = None
        self._root_main_frame = None
        self._output = None
        self._input_box = None
        self._send_button = None
        self._user_name = None
        self._message = None

    def run(self):
        self._root = tk.Tk()
        self._main_window()
        self._main_frame()
        logging.info("Loaded main frame no error")
        self._output_box()
        logging.info("Loaded output screen no Error")
        self._input()
        self._send()
        logging.info("Initialized No Error")
        self._output.insert(tk.END, f"Welcome {self._user_name} to the Janky ChatRoom\n\n\n")
        self._root.mainloop()

    def _welcome_window(self):
        pass

    def _main_window(self):
        self._root.title("Janky ChatRoom by Daniel Lugo")
        self._root.minsize(500, 500)
        self._root.maxsize(500, 500)

    def _main_frame(self):
        self._root_main_frame = tk.Frame(self._root, bg="light blue")
        self._root_main_frame.pack(fill='both', expand=True)

    def _output_box(self):
        self._output = tk.Text(self._root_main_frame, bg="light gray", font=(None, 12))
        self._output.place(relx=0.05, rely=0.05,
                           relwidth=0.90, relheight=0.80)

    def _input(self):
        self._input_box = tk.Text(self._root_main_frame, bg="white", font=(None, 12))
        self._input_box.place(relx=0.05, rely=0.87,
                              relwidth=0.65, relheight=0.1)

    def _send(self):
        self._send_button = tk.Button(self._root_main_frame, text='Send', bg="white",
                                      font=(None, 10),
                                      command=lambda: [self._get_input(), self._clear_box()])
        self._send_button.place(relx=0.75, rely=0.87,
                                relwidth=0.20, relheight=0.1)

    def _get_input(self):
        self._message = self._input_box.get("1.0", tk.END)
        logging.info(f"Got message: {self._message}")

    def _clear_box(self):
        self._input_box.delete("1.0", tk.END)
        logging.info("Cleared Screen")

    def output_message(self, message):
        self._output.insert(tk.END, f"{self._user_name}: {message}")


chat_ = ChatGui()
chat_.run()
# previous_message = ''
#
# while True:
#     print("In while loop")
#     new_message = chat_.output_keypad_press()
#     previous_message = new_message
