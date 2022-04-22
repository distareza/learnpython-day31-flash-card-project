import pandas
import random


class MyFlashCard:

    def __init__(self):
        try:
            data = pandas.read_csv("data/word_to_learn.csv")
        except FileNotFoundError:
            data = pandas.read_csv("data/french_words.csv")

        # https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_dict.html
        # Convert the DataFrame to a dictionary.
        # ‘records’ : list like [{column -> value}, … , {column -> value}]
        self.to_learn = data.to_dict(orient="records")

    def next_card(self):
        return random.choice(self.to_learn)

    def remove(self, selected_data):
        self.to_learn.remove(selected_data)

    def card_length(self):
        return len(self.to_learn)

    def save_data(self):
        data = pandas.DataFrame(self.to_learn)

        # https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html
        # save csv without index
        data.to_csv("data/word_to_learn.csv", index=False)

myFlashCard = MyFlashCard()

french = myFlashCard.next_card()["French"]
english = myFlashCard.next_card()["English"]

print(french + " = " + english)

# for _ in range(19):
#     next_card = myFlashCard.next_card()
#     myFlashCard.remove(next_card)
#     print(myFlashCard.card_length())