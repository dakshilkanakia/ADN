FROM python:latest

# Install dependencies
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the rest of the code
COPY . .

# tell docker which port to run on
EXPOSE 8000
# Run the application

CMD ["python","manage.py","runserver"]

