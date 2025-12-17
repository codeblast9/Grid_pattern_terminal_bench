FROM python:3.12-slim

RUN pip install numpy
WORKDIR /app

# ALL files (including solution.sh) to the container
COPY . /app/

# scripts executable
RUN chmod +x /app/solution.sh /app/run-tests.sh

#  placeholder file
RUN touch /app/grid_transform.py && chmod 777 /app/grid_transform.py