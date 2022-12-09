AVM8 Examples
---------------

This repo is meant to demonstrate usage of the ops introduced with AVM8


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
2) cd into it and create a virtual environment

```sh
cd demo-avm8
python -m venv .venv
source .venv/bin/activate
```

3) Install the requirements

```sh
pip install -r requirements.txt
```

4) Run it

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