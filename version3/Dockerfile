FROM python

WORKDIR /app

COPY app/requirements.txt .

RUN pip install -r requirements.txt

COPY app/ .

COPY data/ ./data


CMD ["python","main.py"]