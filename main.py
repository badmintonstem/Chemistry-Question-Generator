from random import randint
import pandas as pd

#CONSTANTS
CSVFILE = "questions.csv"
NUM_QUESTIONS = 5

#Functions
def importQuestions(csvFile):
  questions = pd.read_csv(csvFile)
  return questions

def findTopics(questionFile):
  topics = questionFile["Topic"].unique().tolist()
  return topics

def defineSubset(questions, topicList):
  subset = questions[questions["Topic"].isin(topicList)]
  return subset

def generateRandoms(questionFile):
  randoms = []
  for i in range(NUM_QUESTIONS):
    random = randint(0, len(questionFile)-1)
    while random in randoms:
      random = randint(0, len(questionFile)-1)
    randoms.append(random)
  return randoms

def createQuestionList(questionFile, randomList):
  questions_list = []
  for random in randomList:
    question = questionFile.iloc[random, 1]
    answer = questionFile.iloc[random, 2]
    temp = [question, answer]
    questions_list.append(temp)
  return questions_list

def displayQuestions(questionList):
  print("\n\n\n\n\nQuestions\n")
  for question in questionList:
    print(question[0])
  print("\n\n\n")

def displayAnswers(questionList):
  input("Press any key to display answers")
  print("\n\nAnswers\n")
  for question in questionList:
    print(question[1])

def topicSelection(topicList):
  print("Please Enter the Topic Tiles you are interested in from this list one by one")
  chosenTopics = []
  for topic in topicList:
    print(topic)
  while True:
    topicSel = input("Enter topic choice (blank if finished) > ")
    if topicSel == "":
      return chosenTopics
    elif topicSel in topicList:
      chosenTopics.append(topicSel)
    else:
      print("Topic not valid, please try again")
  

#Main Program
questions = importQuestions(CSVFILE)
topics = findTopics(questions)
subset = defineSubset(questions, topicSelection(topics))
randoms = generateRandoms(subset)
questionList = createQuestionList(subset, randoms)
displayQuestions(questionList)
displayAnswers(questionList)