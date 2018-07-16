class sequenceError("Exception"):
    def __init__(self, message):
        self.message=message
        if message=="sequenceCount":
            seqCount()

    def seqCount():
        print("No. of elements in the sequence do not match the no. of jobs")

