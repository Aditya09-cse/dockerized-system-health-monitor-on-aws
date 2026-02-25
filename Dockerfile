# python base image 
FROM python:3.12-slim

# create workdir 
WORKDIR /app

# copy the src code here
COPY . .

# install requirement to this app
RUN pip install -r requirements.txt

# Expose the port mapping
EXPOSE 8000

# execute application
CMD ["python","app.py"]
