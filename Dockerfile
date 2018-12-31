FROM python:3.4
WORKDIR /app
ADD . /app
RUN pip install -r requirements.txt
EXPOSE 80
ENV NAME World
CMD ["python", "Print.py"]

