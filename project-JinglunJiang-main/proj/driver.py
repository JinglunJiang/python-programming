import sys
from markov import identify_speaker

if __name__ == "__main__":
    if len(sys.argv) != 6:
        print(
            f"Usage: python3 {sys.argv[0]} <filenameA> <filenameB> <filenameC> <k> <hashtable-or-dict>"
        )
        sys.exit(1)

    # extract parameters from command line & convert types
    filenameA, filenameB, filenameC, k, hashtable_or_dict = sys.argv[1:]
    k = int(k)
    if hashtable_or_dict not in ("hashtable", "dict"):
        print("Final parameter must either be 'hashtable' or 'dict'")
        sys.exit(1)

    # TODO: add code here to open files & read text
    speech1 = open(filenameA, 'r').read()
    speech2 = open(filenameB, 'r').read()
    speech3 = open(filenameC, 'r').read()

    # TODO: add code to call identify_speaker & print results
    use_hashtable = True if hashtable_or_dict == "hashtable" else False
    prob1, prob2, result = identify_speaker(speech1, speech2, speech3, k, use_hashtable)

    # Output should resemble (values will differ based on inputs):

    # Speaker A: -2.1670591295191572
    # Speaker B: -2.2363636778055525

    # Conclusion: Speaker A is most likely
    print(f"Speaker A: {prob1}")
    print(f"Speaker B: {prob2}")
    print("")
    print(f"Conclusion: Speaker {result} is most likely")
