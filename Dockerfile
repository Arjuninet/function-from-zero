FROM public.ecr.aws/lambda/python:3.12

RUN mkdir -p /app
COPY ./main.py /app/
COPY ./requirements.txt /app/requirements.txt
COPY ./wikibot.py /app/wikibot.py
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
WORKDIR /app
EXPOSE 8080
CMD ["main.py"]
ENTRYPOINT [ "python" ]

