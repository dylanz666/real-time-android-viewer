# real-time-android-viewer
A real time solution to view remote android's screen and can control remote android as well.
(This solution is only tested with WinOS)

## Installation
* python3, recommend 3.9+.
* Install 3rd party pip modules.
```commandline
pip install -r requirements.txt
```

## How to set up backend?
* Execute below command:
```commandline
python app.py
```

or:
```commandline
uvicorn app:app --host 0.0.0.0 --port 8000
```

* Start backend with reload(useful for debug):
```commandline
uvicorn app:app --host 0.0.0.0 --port 8000 --reload
```

## How to set up frontend?
* Set your backend server host and port in index.html
```commandline
const server = "localhost:8000";
```

* Set your websocket url in index.html
```commandline
const wsUrl = `ws://${server}/ws`;
```

## How to view your android screen?
* Open index.html on your browser.

## How to control your android device?
* See demo in index.html

## Heads up
There is no need to put backend and frontend together. For example:
1. Set up your backend on your WinOS which have several android connected.
2. Set up your frontend on another frontend server, like Nginx server.
3. Visit your frontend page on another PC's browser, then you can see and control your remote android devices.

## Reference
* Pyscrcpy: https://github.com/yixinNB/pyscrcpy.git