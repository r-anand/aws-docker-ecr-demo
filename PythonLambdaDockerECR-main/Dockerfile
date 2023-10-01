FROM public.ecr.aws/lambda/python:3.8

COPY requirements.txt ./
RUN pip3 install -r requirements.txt
COPY myfunction.py ./
# tell the port number the container should expose

CMD ["myfunction.lambda_handler"]
