from django_cron import CronJobBase, Schedule
from .models import *
from pythainlp import word_tokenize
from pythainlp.corpus import stopwords
from pythainlp.corpus import wordnet
from nltk.stem.porter import PorterStemmer
from nltk.corpus import words
from stop_words import get_stop_words
import datetime
import re
import string
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def clean_msg(msg): 
        for c in string.punctuation:
            msg = re.sub(r'\{}'.format(c),'',msg)
        msg = ' '.join(msg.split())
        return msg

def split_word(text):  
    th_stop = tuple(stopwords.words('thai'))
    en_stop = tuple(get_stop_words('en'))
    p_stemmer = PorterStemmer()
    tokens = word_tokenize(text)
    tokens = [i for i in tokens if not i in th_stop and not i in en_stop]

    tokens = [p_stemmer.stem(i) for i in tokens]

    tokens_temp=[]
    for i in tokens:
        w_syn = wordnet.synsets(i)
        if (len(w_syn)>0) and (len(w_syn[0].lemma_names('tha'))>0):
            tokens_temp.append(w_syn[0].lemma_names('tha')[0])
        else:
            tokens_temp.append(i)
    
    tokens = tokens_temp
    
    tokens = [i for i in tokens if not i.isnumeric()]
    tokens = [i for i in tokens if not ' ' in i]

    return tokens

class MyCronJob(CronJobBase):
    RUN_AT_TIMES = ['01:00']

    schedule = Schedule(run_at_times=RUN_AT_TIMES)
    code = 'assignment.my_cron_job'    # a unique code    


    def do(self):
        print("a")
        now = datetime.datetime.now().strftime('%Y-%m-%d')
        print(now)
        choice_answer = StudentChoiceAnswer.objects.filter(
            question__assignment__end_date=now)
        print(choice_answer)
        # StudentDoAssignment.filter(assignment__end_date=now).update(finish=True)
        
        
        # chocie
        if len(choice_answer):
            for i in choice_answer:
                real_answer = ChoiceAnswer.objects.get(question=i.question)
                student_score = StudentChoiceScore()
                student_score.student = i.student
                student_score.question = i.question
                if i.answer == real_answer.no:
                    student_score.score = i.question.score
                else:
                    student_score.score = 0
                student_score.save()

        # matching
        print("b")
        matching_answer = StudentMatchingAnswer.objects.filter(
            question__assignment__end_date=now)
        
        print(matching_answer)

        if len(matching_answer):
            for i in matching_answer:
                real_answer = MatchingAnswer.objects.get(
                    question=i.question, item_no=i.answer_item)
                student_score = StudentMatchingScore()
                student_score.student = i.student
                student_score.question = i.question
                student_score.item_no = i.answer_item
                print(real_answer)
                print(i.answer_choice)
                print(real_answer.choice_no.no)
                if i.answer_choice == real_answer.choice_no.no:
                    len_choice = len(
                        MatchingAnswer.objects.filter(question=i.question))
                    student_score.score = i.question.score / len_choice
                else:
                    student_score.score = 0
                student_score.save()

        # open ended
        print('c')
        open_answer = StudentOpenEndedAnswer.objects.filter(
            question__assignment__end_date=now)

        print(open_answer)

        if len(open_answer):
            for i in open_answer:
                keywords = OpenEndedKeywords.objects.get(
                    question=i.question)
                print(keywords)

                word1 = split_word(clean_msg(keywords.keyword))
                word2 = split_word(clean_msg(i.answer))

                token_list = [word1,word2]
                tokens_list_j = [','.join(tkn) for tkn in token_list]
                tlidf =TfidfVectorizer(analyzer=lambda x:x.split(','))
                m = tlidf.fit_transform(tokens_list_j)
                cos_sim=cosine_similarity(m[0], m)
                print(cos_sim[0][1])
                if cos_sim[0][1]<0.4:
                    w = 0
                elif cos_sim[0][1]<0.6:
                    w = 0.5
                else:
                    w = 1

                student_score = StudentOpenEndedScore()
                student_score.student = i.student
                student_score.question = i.question
                student_score.score = i.question.score*w
                student_score.save()

        finish = StudentDoAssignment.objects.filter(assignment__end_date=now).update(check=True)
