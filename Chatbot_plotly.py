from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer
from flask import Flask, render_template, request
""" Create chat bot object with parameteres the name read type and logic adptors to lestion
"""
"""
Create a Flask app as app 
"""
app = Flask(__name__)

bot = ChatBot('Solara', read_only=False,
              logic_adaptors=[
                  {

                      "import path": "chatterbot.logic.Bestmach",
                      "default response": "I am sorry I dont have an anzer",
                      "maximum_simularity_threshhold": 0.9
                  }

              ])

""" what to train crete here input and output data"""
# chatbot = ChatBot("bot")
# chatbot.storage.drop()

# list_to_train = [

#         "hi",
#         "hi there",
#         'What is your name ?',
#         'I am Solara your Cytel helper'

# ]
list_to_train = [

    "hi",
    'I am Solara your Cytel helper',
    "what is Solara ?",
    "Solara is clinical trial software Plaese go to this link and find more about it https://mycytel.cytel.com/sign-in?destination=",
    "What is clinical trial software ",
    "A Clinical Trial Management System (CTMS) is a software system used by biotechnology and"
    "pharmaceutical industries to manage clinical trials in clinical research. The system maintains "
    "and manages planning, performing and reporting functions, along with participant contact information, "
    " tracking deadlines and milestones",
    "What is Solara Plans ?",
    "Solara Plans is where you map out the big picture or strategy that drives your desired set of optimal clinical trial designs",
    "what is Solara Design ?",
    "the statistical design stage is when possible values of critical parameters such as power, sample size, trial duration, and cost, among others, are explored and formalized"





]

# """crete a trainer object and pas the cahtbot object to that
# """
List_trainer = ListTrainer(bot)
# """Train the chatbot
# """
chatbot = ChatBot("bot")
chatbot.storage.drop()
List_trainer.train(list_to_train)
"""input to ask user ask
"""
""" add route page for the webapp
"""
""" crete route to the site """
"""crete fuction to execute to return website or reponce"""
# List_trainer = ChatterBotCorpusTrainer(bot)
# List_trainer.train("chatterbot.corpus.english")
