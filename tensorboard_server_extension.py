from subprocess import Popen

def load_jupyter_server_extension(nbapp):
    Popen(["tensorboard", "--logdir", "logs", "--port", "6006"])
