from hashtable import Hashtable
import math

HASH_CELLS = 57
TOO_FULL = 0.5
GROWTH_RATIO = 2

class Markov:
    def __init__(self, k, text, use_hashtable):
        """
        Construct a new k-order markov model using the text 'text'.
        Inputs: k: value of succedding characters to count
                text: the input string
                use_hashtable: whether using the datastructure from hashtable.py or build-in
        """
        self.k = k
        self.text = text
        self.use_hashtable = use_hashtable

        if use_hashtable:
            self.model = Hashtable(HASH_CELLS, 0, TOO_FULL, GROWTH_RATIO)
        else:
            self.model = {}

        self.build_model()

    def build_model(self):
        """
        Method to build 
        """
        for i in range (len(self.text)):
            k_length_string = self.k_length_string(self.text, i)
            k_plus_1_string = self.k_plus_1_string(self.text, i)

            self.update_model(k_length_string)
            self.update_model(k_plus_1_string)

    def k_length_string(self, text, index):
        """
        Helper builder for a k length string for any specific character in a givin index
        Inputs: the text and the index of the character
        Outputs: teh k-length string
        """
        return text[index:min(index + self.k, len(text))] + text[0:max(0, index + self.k - len(text))]
    def k_plus_1_string(self, text, index):
        """
        Helper builder for a k + 1 length string for any specific character in a givin index
        Inputs: the text and the index of the character
        Outputs: teh k + 1-length string
        """
        return text[index:min(index + self.k + 1, len(text))] + text[0:max(0, index + self.k + 1 - len(text))]

    def update_model(self, key):
        """
        Method used to update the number of values for a certain key,
        either equals the original amount plus 1 or 0 + 1
        Inputs: the key
        Outputs: None
        """
        self.model[key] = self.model.get(key, 0) + 1

    def log_probability(self, s):
        """
        Get the log probability of string "s", given the statistics of
        character sequences modeled by this particular Markov model
        This probability is *not* normalized by the length of the string.
        Inputs: the input string
        Outputs: the log probability calculated
        """
        log_prob = 0.0

        for i in range(len(s)):
            k_length_string = self.k_length_string(s, i)
            k_plus_1_string = self.k_plus_1_string(s, i)

            count_k = self.model.get(k_length_string, 0)
            count_k_plus_1 = self.model.get(k_plus_1_string, 0)

            log_prob += math.log((count_k_plus_1 + 1) / (count_k + len(set((self.text)))))
            #set() is used to calculate the number of distinct characters in the original string

        return log_prob                 

def identify_speaker(speech1, speech2, speech3, k, use_hashtable):
    """
    Given sample text from two speakers (1 and 2), and text from an
    unidentified speaker (3), return a tuple with the *normalized* log probabilities
    of each of the speakers uttering that text under a "order" order
    character-based Markov model, and a conclusion of which speaker
    uttered the unidentified text based on the two probabilities.
    Inputs: the speech1 and speech2 used to generate two different models, speech3 is the input string,
            k is the number to calculate for each index, use_hashtable is to choose the model
    Outputs: Tuples that include 2 log probabilities and a result matching the two models
    """
    model1 = Markov(k, speech1, use_hashtable)
    model2 = Markov(k, speech2, use_hashtable)

    log_prob1 = model1.log_probability(speech3) / len(speech3)
    log_prob2 = model2.log_probability(speech3) / len(speech3)

    return (log_prob1, log_prob2, "A" if log_prob1 > log_prob2 else "B")
