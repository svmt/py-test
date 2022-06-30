FROM python:3.10-slim@sha256:54956d6c929405ff651516d5ebbc204203a6415c9d2757aaddcde35be680431e

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./app /code/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
