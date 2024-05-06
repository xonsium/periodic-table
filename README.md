# Periodic Table
*get info about specific element on the periodic table*

The data that this api returns is taken from https://gist.github.com/GoodmanSciences/c2dd862cd38f21b0ad36b8f96b4bf1ee

Installation
=============
```sh
$ git clone https://github.com/Famewix/Element-API.git
$ cd Element-API
$ pip install -r requirements.txt
```
Run
=============
I haven't hosted this api yet, so for now you have to host it by youself.
```sh
$ uvicorn main:app --host IP --port 8000
```
or in Development mode
```sh
$ uvicorn main:app --reload
```

Usage
==========

#### Get Information about an Element
```
protocol://domain:8000/e/{symbol_of_element}
```
#### Get list of all Elements
```
protocol://domain:8000/elements/
```

#### Get list of all Symbols
```
protocol://domain:8000/symbols/
```