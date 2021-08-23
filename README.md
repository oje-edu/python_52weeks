![GitHub last commit](https://img.shields.io/github/last-commit/oje-edu/python_52weeks) ![GitHub repo size](https://img.shields.io/github/repo-size/oje-edu/python_52weeks)

# I started to learn (on hold)

[52 weeks](https://my.thisisit.io/p/52-weeks-of-python) of python - a free course from and with [@chuckablack](https://twitter.com/chuckablack)

## some things to note:

There are some **requirements**:

#### Debian based

```bash
sudo apt update && sudo apt dist-upgrade -y && \
sudo apt install git python3 python3-venv python3-pip nmap -y && \
sudo reboot
```

### Download & venv (Unix-based)

```bash
git clone https://github.com/oje-edu/python_52weeks.git
cd 52weeks
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
```
