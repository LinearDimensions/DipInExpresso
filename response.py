import NLP
import random
from Quotes import quotes
from Resources import available_resources

def getResponse(input):
    a,b = NLP.predict(input)
    sentiment = int(b[0][0])
    category = a
    output = ''
    output += ('Your sentiment in **{}** has been {}\n\n'.format(category,['negative','positive! Keep up the good work'][sentiment]))
    if sentiment <0.5:
        output += ('Available Resources: \n')
        xx = available_resources[category]
        if len(xx)>0:
            output += xx[random.randint(0,len(xx)-1)]
            output += '\n'
        yy = quotes[category]
        if len(yy)>0:
            output += yy[random.randint(0,len(yy)-1)]
            output += '\n'

    return output