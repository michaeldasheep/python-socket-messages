FROM python:3.11.5-alpine
ADD server2.py /server2.py
CMD ["python3", "server2.py"]