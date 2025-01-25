sentence=input("enter a sentence: ")
def word_counter(sentence):
    words=sentence.lower().split()
    word_count={}
    for word in words:
        if word in word_count:
            word_count[word]+=1
        else:
            word_count[word]=1
        for word,count in word_count.items():
            print(f"'{word} :{count}")

def main():
    word_counter(sentence)
main()
