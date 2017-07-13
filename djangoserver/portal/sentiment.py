from textblob import TextBlob

def sentiment(text):
    blob=TextBlob(text)
    pol=[]
    for sentence in blob.sentences:
        print(sentence)
        pol.append(sentence.sentiment.polarity)
    print("pol :",pol)
    pos=[po for po in pol if po>0.0]
    print("pos:",pos)
    if(sum(pol)<0):
        return -1
    if(sum(pol)>1):
        return 1
    neg=[po for po in pol if po<0]
    print("neg: ",neg)
    if len(pos)>len(neg):
        return 1
    elif len(pos)<len(neg):
        return -1
    else:
        return 0
