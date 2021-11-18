FROM python:3.9
WORKDIR /app
COPY Pipfile ./
RUN pip install pipenv \
  && pipenv lock --keep-outdated --requirements > requirements.txt \
  && pip install --no-cache-dir -r requirements.txt
# RUN pipenv install --deploy --ignore-pipfile
COPY . .
CMD ["uvicorn", "main:app", "--reload"]