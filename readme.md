### getting started

create python virtual environment named 'venv'
 
```shell
python -m venv './venv'
```

activate virtual environment with `source ./venv/Scripts/activate`

update pip
```shell
python -m pip install --upgrade pip
 ```

 install library `pystdlib`

 ```shell
pip install git+ssh://git@github.com/ibqn/pystdlib.git
```
test that the library was installed correctly by the following command
```shell
python -c 'import pystdlib;print("ok")'
```
to deactivate venv run `deactivate`

create new repository by running `git init` and check its status with `git status`