import base64
from algosdk.atomic_transaction_composer import (
    AtomicTransactionComposer,
    AtomicTransactionResponse,
)
from algosdk.abi import Method
from algosdk.future.transaction import (
    ApplicationCreateTxn,
    OnComplete,
    wait_for_confirmation,
)
from algosdk.v2client.algod import AlgodClient

from beaker.sandbox import get_accounts, get_algod_client


def compile_program(algod: AlgodClient) -> bytes:
    # read in file
    with open("switch.teal", "r") as f:
        teal_src = f.read()

    compile_result = algod.compile(teal_src)
    return base64.b64decode(compile_result["result"])


def demo():
    # Grab an account from the KMD
    acct = get_accounts().pop()
    # Get an algod client to the sandbox
    algod = get_algod_client()

    # cache suggested params
    sp = algod.suggested_params()

    # read the teal file and compile it, pretend the clear
    # program is the same as approval
    approval_program = clear_program = compile_program(algod)

    # create and sign the App create txn
    create_txn = ApplicationCreateTxn(
        acct.address,
        sp,
        OnComplete.NoOpOC,
        approval_program,
        clear_program,
        None,
        None,
    ).sign(acct.private_key)

    # Send txn to create app
    txid = algod.send_transaction(create_txn)
    result = wait_for_confirmation(algod, txid, 4)

    # save the app id for the app we just created
    app_id = result["application-index"]

    # Define the method we want to call
    play_method = Method.from_signature("play(uint64)string")

    # Iterate over numbers from [0, 25) and:
    #   if its divisible by 15 print "FizzBuzz"
    #   elseif its divisble by 3 print "Fizz"
    #   elseif its divisible by 5 print "Buzz"
    #   else print "number"

    for i in range(25):
        atc = AtomicTransactionComposer()
        atc.add_method_call(app_id, play_method, acct.address, sp, acct.signer, [i])
        results: AtomicTransactionResponse = atc.execute(algod, 4)
        result = results.abi_results[0].return_value
        match result:
            case "FizzBuzz":
                assert i % 15 == 0
            case "Buzz":
                assert i % 5 == 0
            case "Fizz":
                assert i % 3 == 0
            case "number":
                assert True
            case _:
                raise Exception("wat?")

        print(f"For {i} got {result}")


if __name__ == "__main__":
    demo()
