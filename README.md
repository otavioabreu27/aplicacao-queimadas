# Installation guide
## 1. Clone the repository
First of all, clone this repository on your local environment. For doing so execute the command line bellow.

```console
    git clone <url>
```

## 2. Virtual Environment
As we will be working with python packages we will need a virtual environment. We do this because in the virtual environment we can install packages without affecting other instances of python on our machine.
Without further ado, execute the code bellow for creating your environment.

```console
    cd selecao_queimadas
    python -m venv <name>
```

- In some OS's the python line may change for this one:
```console
    cd selecao_queimadas
    python3 -m venv <name>
```

## 3. Activating the Environment
Now that you setup your venv is time for activating it. This part is the one that varies the most depending on the Terminal that you are using.

#### 3.1 CMD
For activating the venv on CMD you will have to follow this path: venv/Scripts/ and execute the command below:

```console
   activate.bat
```

#### 3.2 PowerShell
For activating the venv on PS execute the command below:

```console
   .\venv\Scripts\Activate.ps1
```

#### 3.3 Linux Terminal / MacOS
For activating the venv on Linux Terminal and MacOS execute the command below:

```console
   source .\venv\bin\activate
```

## 4. Installing Packages
With the venv activated, go back to the root of the directory and use the command below for installing all the necessary packages:

```console
   pip install -r requirements.txt
```

## 5. Running the Application
On the terminal go to the /src directory and execute the command bellow:

```console
   python app.py
```

## Congratulations, you have installed the project!