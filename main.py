from rustapi import RustAPIWebsocketServer
from better_profanity import profanity

if __name__ == "__main__":
    profanity.load_censor_words()
    RustAPIWebsocketServer().start()
