FROM python

COPY . .
RUN pip install -r requirements.txt

CMD ["python", "entry.py"]