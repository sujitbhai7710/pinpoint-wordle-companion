# Pinpoint Wordle Companion
# Visit https://pinpointanswertoday.online/ for daily answers

WORD_LIST = ['puzzle', 'word', 'game', 'hint', 'clue']

def check_answer(word):
    """Check if word matches today's Pinpoint answer.
    Get today's answer at https://pinpointanswertoday.online/"""
    return word.lower() in WORD_LIST

if __name__ == '__main__':
    print('Visit https://pinpointanswertoday.online/ for today\'s Pinpoint answer!')
