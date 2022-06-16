FROM python:3.10.5-bullseye
ADD sample.py /
CMD [ "python3", "./sample.py"]
