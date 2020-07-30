## Simple quiz API

### Run application
You need to have python, Django and Djangorestframework installed in the system.
Or use`pip` to install them. \
Open the command line and navigate to root directory of the project.\
Run `python manage.py migrate` \
Run `python manage.py runserver`


### API endpoints
#### Authentication
`api-auth/` - For login 

#### Quizes
`GET: quizes/` - to get list of available active quizes with their questions \
`POST: quizes/` - to create the quiz with questions\


    {
        "name" : "",
        "start_date" : "",
        "end_date" : "",
        "description" : "",
        "questions" :
            [
                {
                    "question_text": "",
                    "question_type": "",
                    "answer_variants": ""
                }
            ]
    }

`GET quizes/<quiz_id>` - to get specific quiz \
`PUT quizes/<quiz_id>` - to edit specific quiz 

    {
        "name" : "",
        "end_date" : "",
        "description" : "",
    }

`DELETE quizes/<quiz_id>` - to delete specific quiz 

#### Questions
`GET questions/<question_id>` - to get specific question \
`PUT questions/<question_id>` - to edit specific question 

    {
        "question_text": "",
        "question_type": "",
        "answer_variants": ""
    }

`DELETE questions/<question_id>` - to delete specific question 

####Answers
`POST answers/` - to save the list of answers 

    {
        "user_id": "",
        "answers": 
            [
                {
                    "answer_text": "",
                    "question": ""
                }
            ]
    }

`GET answers/<user_id>` - to get user' answers 