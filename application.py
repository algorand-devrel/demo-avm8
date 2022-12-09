from pyteal import *
from beaker import * 


class DemoAVM8(Application):
    pass


if __name__ == "__main__":
    DemoAVM8().dump("artifacts")