from chat_protobufs.chatroom_pb2 import sendMessageRequest, Nothing, connectionRequest, onCloseRequest
from chat_protobufs.chatroom_pb2_grpc import ChatStub
import tkinter as tk
import logging
import threading
import grpc


logging.basicConfig(level=logging.INFO)



class ClientSide:
    def __init__(self, stub: ChatStub, user_name):
        self._root = None
        self._root_main_frame = None
        self._output = None
        self._input_box = None
        self._send_button = None
        self._user_name = user_name
        self._message = ''
        self._grpc_response = None
        self.stub = stub
        self._input_text = None
        self._do_once = False

    def run(self):
        self._root = tk.Tk()
        threading.Thread(target=self._get_messages, daemon=True).start()
        self._main_window()
        self._main_frame()
        self._input_text = tk.StringVar(self._root)
        logging.info("Loaded main frame no error")
        self._output_box()
        logging.info("Loaded output screen no Error")
        self._input()
        self._send()
        logging.info("Initialized No Error")
        self._output.insert(tk.END, f"Welcome {self._user_name} to the Janky ChatRoom\n")
        self._create_connection()
        self._root.protocol("WM_DELETE_WINDOW", self._on_close)
        self._root.mainloop()

    def _main_window(self):
        self._root.title("Janky ChatRoom by Daniel Lugo")
        self._root.minsize(500, 500)
        self._root.maxsize(500, 500)

    def _main_frame(self):
        self._root_main_frame = tk.Frame(self._root, bg="light blue")
        self._root_main_frame.pack(fill='both', expand=True)

    def _output_box(self):
        self._output = tk.Text(self._root_main_frame, bg="light gray", font=(None, 12))
        self._output.see(tk.END)
        self._output.place(relx=0.05, rely=0.05,
                           relwidth=0.90, relheight=0.80)

    def _input(self):
        self._input_box = tk.Entry(self._root_main_frame, bg="white", font=(None, 12), textvariable=self._input_text)
        self._input_box.bind('<Return>', self._on_enter)
        self._input_box.place(relx=0.05, rely=0.87,
                              relwidth=0.65, relheight=0.1)

    def _on_enter(self, event=None):
        self._get_input()
        self._clear_box()

    def _send(self, event=None):
        self._send_button = tk.Button(self._root_main_frame, text='Send', bg="white",
                                      font=(None, 10),
                                      command=lambda: [self._get_input(), self._clear_box()])
        self._send_button.place(relx=0.75, rely=0.87,
                                relwidth=0.20, relheight=0.1)

    def _get_input(self):
        self._message = self._input_text.get()
        logging.info(f"[CLIENT SIDE]: input message: {self._message}")
        try:
            message_request = sendMessageRequest(sentMessage=self._message, userName=self._user_name)
            self._grpc_response = self.stub.sendMessage(message_request)
        except grpc.RpcError as rpc_error:
            logging.info(f"[CLIENT SIDE]: Error at _get_input() CLIENT -> {rpc_error}")
            self._output.insert(tk.END, f"\n\nServer is down\n\n")

    def _get_messages(self):
        logging.info("[CLIENT SIDE]: Listening for messages")
        request = Nothing(nothing=True)
        try:
            for _message in self.stub.messageStream(request):
                logging.info("[CLIENT SIDE]: Iterating through messages in server")
                self._output.insert(tk.END, f"{_message.userName}: {_message.sentMessage}\n")
        except grpc.RpcError as rpc_error:
            if rpc_error.code() == grpc.StatusCode.CANCELLED:
                pass
            else:
                logging.info(f"[CLIENT SIDE]: Error at _get_messages() CLIENT -> {rpc_error}")
                self._output.insert(tk.END, f"\n\nServer is down\n\n")

    def _clear_box(self):
        self._input_box.delete(0, 'end')
        logging.info("[CLIENT SIDE]: Cleared input box")

    def _create_connection(self):
        try:
            request = connectionRequest(userName=self._user_name)
            response = self.stub.connectedUser(request)
            self._output.insert(tk.END, response)
            self._output.insert(tk.END, "\n\n")
            logging.info(f"[CLIENT SIDE]: Created connection {self._user_name}")
        except grpc.RpcError as e:
            logging.info(f"[CLIENT SIDE]: Error at _create_connection() CLIENT -> {e}")
            self._output.insert(tk.END, f"\n\nServer is down\n\n")

    def _on_close(self):
        self._do_once = True
        request = onCloseRequest(userName=self._user_name)
        response = self.stub.onDisconnection(request)
        self._output.insert(tk.END, f"\n{self._user_name} disconnected: {response.disconnected}")
        self._root.destroy()
