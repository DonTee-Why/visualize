
# Visualize

Visualizer-CLI is a terminal program written in Python that enables you to visualize data. The data can be gotten from an API endpoint in key-value pairs (i.e JSON format. dates as keys, and number of users as values). Data is then presented using a graph drawn in the terminal. This version is for the article written on [dev.to](https://dev.to/timiddon). For a more robust package version, check [here](https://github.com/DonTee-Why/visualizer-cli).

## Installation

This project requires [Python](https://www.python.org/downloads/) v3.8+ to run.

1. Clone the project from the repository and then cd into the root directory.

```sh

git clone https://github.com/DonTee-Why/visualize.git
cd visualize

```

2. To avoid alterating global packages, I suggest using a virtual environment. Create a virtual environment

```sh
python -m venv env
```

And then activate it.

On linux:

```sh
source ./env/bin/activate
```

On windows:

```sh
env\Scripts\activate.bat
```

3. Install the dependencies in the virtual environment.

```sh
cd visualize
pip install -r requirements.txt
```

4. Run the project

```sh
python -m visualize -s <START DATE> -e <END DATE>
```

## License

MIT License
