FROM python as builder

WORKDIR /app

COPY requirements.txt .
RUN pip install  --prefix=/install -r requirements.txt

COPY test_requirements.txt .
RUN pip install -r test_requirements.txt

COPY . .

RUN PYTHONPATH=/install/lib/python3.15/site-packages pytest -v


FROM python as runtime

WORKDIR /app

COPY --from=builder /install /usr/local/

COPY main.py .


CMD ["python","main.py"]