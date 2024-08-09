FROM python:3.11.5-alpine
WORKDIR /
ADD server2.py /server2.py
CMD ["python", "/server2.py"]