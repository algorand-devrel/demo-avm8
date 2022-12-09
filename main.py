from beaker.sandbox import get_accounts, get_algod_client
from beaker.client import ApplicationClient
from application import DemoAVM8


def demo():
    acct = get_accounts().pop()
    algod = get_algod_client()

    app_client = ApplicationClient(algod, DemoAVM8(), signer=acct.signer)

    app_id, _, _ = app_client.create()
    # Pass 4 box refs so that we have access to the full 4k bytes of our box
    boxes = [[app_id, DemoAVM8._box_name], [0,""], [0,""],[0,""]]
    result = app_client.call(
        DemoAVM8.do_box_stuff, boxes=boxes
    )
    print(result.return_value)


if __name__ == "__main__":
    demo()
