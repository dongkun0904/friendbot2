FROM python:latest

# Setup for virtualenv
ENV VIRTURAL_ENV=/opt/venv
RUN python3 -m venv ${VIRTURAL_ENV}
ENV PATH="$VIRTURAL_ENV/bin:$PATH"

# Setup the directory
RUN mkdir /home/nlu
COPY ./src /home/nlu
WORKDIR /home/nlu

# Install dependencies
RUN pip install -r requirements.txt

# Run the application
CMD ["python", "app.py"]