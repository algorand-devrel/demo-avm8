AVM8 Examples
---------------

This repo is meant to demonstrate usage of the ops introduced with AVM8

The full set of opcodes introduced in AVM8 are as follows:

- `bury`: replace the Nth value from the top of the stack with A. bury 0 fails.
- `popn`: remove N values from the top of the stack
- `dupn`: duplicate A, N times
- `pushbytess`: push sequences of immediate byte arrays to stack (first byte array being deepest)
- `pushints`: push sequence of immediate uints to stack in the order they appear (first uint being deepest)
- `proto`: Prepare top call frame for a retsub that will assume A args and R return values.
- `frame_dig`: Nth (signed) value from the frame pointer.
- `frame_bury`: replace the Nth (signed) value from the frame pointer in the stack with A
- `switch`: branch to the Ath label. Continue at following instruction if index A exceeds the number of labels.
- `match`: given match cases from A[1] to A[N], branch to the Ith label where A[I] = B. Continue to the following instruction if no matches are found.
- `box_create`: create a box named A, of length B. Fail if A is empty or B exceeds 32,768. Returns 0 if A already existed, else 1
- `box_extract`: read C bytes from box A, starting at offset B. Fail if A does not exist, or the byte range is outside A's size.
- `box_replace`: write byte-array C into box A, starting at offset B. Fail if A does not exist, or the byte range is outside A's size.
- `box_del`: delete box named A if it exists. Return 1 if A existed, 0 otherwise
- `box_len`: X is the length of box A if A exists, else 0. Y is 1 if A exists, else 0.
- `box_get`: X is the contents of box A if A exists, else ''. Y is 1 if A exists, else 0.
- `box_put`: replaces the contents of box A with byte-array B. Fails if A exists and len(B) != len(box A). Creates A if it does not exist



Prerequisites
-------------

Please have these installed already:

- Python 3.10
- [sandbox](https://github.com/algorand/sandbox) running with the latest protocol version


Use
-----

1) Clone the repo

```sh
git clone git@github.com:algorand-devrel/demo-avm8.git 
# or
git clone https://github.com/algorand-devrel/demo-avm8.git
```
2) cd into it and install dependencies

```sh
cd demo-avm8
poetry install
source .venv/bin/activate
```

3) Run it

### Box demo

Creates a box and does some simple stuff with it.

Files:

- application.py
- box_demo.py


```sh
python box_demo.py
```

### Frame Pointer demo

Simple demo to show how the new frame pointer ops can be used

Files:

- frame_pointer.teal
- frame_pointer_demo.py

```sh
python frame_pointer_demo.py
```

### Switch demo

Simple demo to show how the new switch opcode can be used

Files:

- switch.teal
- switch_demo.py

```sh
python switch_demo.py
```

### Match demo

Simple demo to show how the new match opcode can be used

Files:

- match.teal
- match_demo.py

```sh
python match_demo.py
```