FROM python:3.7.3-stretch
RUN  mkdir -p /app
WORKDIR /app
RUN pip install --no-cache-dir -U pip
RUN  pip install --no-cache-dir -U pip
COPY requirements.txt .
RUN pip install -r ./requirements.txt
RUN pip install --user -U nltk
RUN python -m nltk.downloader popular
COPY . . 
CMD [ "python","NLPAPI.py" ]