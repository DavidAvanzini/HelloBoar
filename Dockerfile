# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.9


RUN apt-get update -y
RUN apt install libgl1-mesa-glx -y
RUN apt-get install 'ffmpeg'\
    'libsm6'\
    'libxext6'  -y

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Install pip requirements
COPY requirements.pip .
#RUN python -m pip install  detecto
#RUN python -m pip install  flask 
#RUN python -m pip install  flask_restful 
RUN pip install matplotlib
RUN pip install mock
RUN pip install opencv-python
RUN pip install pandas
RUN pip install pytest
RUN pip install sphinx
RUN pip install torch
RUN pip install torchvision
RUN pip install tqdm
RUN python -m pip install  detecto
RUN pip install fastapi
RUN pip install uvicorn[standard] 
RUN pip install aiofiles
RUN pip install python-multipart
RUN python -m pip install  Pillow


WORKDIR /app
COPY webapp/ /app

# Creates a non-root user with an explicit UID and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
#RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
#USER appuser
EXPOSE 8000
# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
#CMD ["python", "webapp\restservice.py"]
CMD ["uvicorn", "main:app", "--reload","--host", "0.0.0.0", "--port", "8000"]