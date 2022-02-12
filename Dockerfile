FROM public.ecr.aws/lambda/python:3.9

COPY . ./

RUN pip install pipenv && pipenv install --deploy --system

CMD ["manage.run_robot"]
