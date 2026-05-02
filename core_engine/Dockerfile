FROM python:3.11-slim

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir gunicorn

COPY . .

EXPOSE 7860

ENTRYPOINT []
CMD ["/bin/bash", "entrypoint.sh"]
