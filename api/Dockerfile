FROM python:3

LABEL name="bradoo_test"
LABEL maintainer="joaoneto4"
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /BradooTest

RUN python -m pip install --upgrade pip

COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY . .

