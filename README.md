AVM8 Examples
---------------

This repo is meant to demonstrate usage of the ops introduced with AVM8


Prerequisites
-------------

Please have these installed already:

- Python 3.10
- [sandbox](https://github.com/algorand/sandbox)


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

Creates a box and does some simple stuff with it

```sh
python box_demo.py
```

### Frame Pointer Demo

```sh
python frame_pointer_demo.py
```

### Switch demo

```sh
python switch_demo.py
```

### Match demo

```sh
python match_demo.py
```