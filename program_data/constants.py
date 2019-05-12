SML_FONT = ('Cambria', 12)
MID_FONT = ('Cambria', 15)
LRG_FONT = ('Cambria', 18)

INVALID_UID_WARNING = 'Not a valid user ID! Please type only numbers 0-9.'
NOT_QUITE_FINISHED = 'Please answer all items before continuing.'
FINISHED = 'That\'s all! Thanks for participating.'

QUESTIONS = {
    'GAD7': 'Wie oft fühlten Sie sich im Verlauf der letzten 2 Wochen durch die folgenden Beschwerden beeinträchtigt?',
    'PHQ9': 'Wie oft fühlten Sie sich im Verlauf der letzten 2 Wochen durch die folgenden Beschwerden beeinträchtigt?',
    'BFI10': 'Inwieweit treffen die folgenden Aussagen auf Sie zu? \nIch...',
    'ZMA29_1': 'Inwieweit treffen die folgenden Aussagen auf Sie zu?',
    'ZMA29_2': 'Inwieweit treffen die folgenden Aussagen auf Sie zu?'
}

ANSWERS = {
    'BFI10': ['Trifft überhaupt nicht zu',
             'Trifft eher nicht zu',
             'Weder noch',
             'Eher zutreffend',
             'Trifft voll und ganz zu'],
    'PHQ9': ['Trifft überhaupt nicht zu',
             'Trifft eher nicht zu',
             'Weder noch',
             'Eher zutreffend',
             'Trifft voll und ganz zu'],
    'GAD7': ['Überhaupt nicht',
              'An einzelnen Tagen',
              'An mehr als der Hälfte der Tage',
              'Beinahe jeden Tag'],
    'ZMA29_1': ['Beschreibt mich überhaupt nicht',
              'Beschreibt mich eher nicht',
              'Weder noch',
              'Beschreibt mich eher',
              'Beschreibt mich sehr gut'],
    'ZMA29_2': ['Beschreibt mich überhaupt nicht',
              'Beschreibt mich eher nicht',
              'Weder noch',
              'Beschreibt mich eher',
              'Beschreibt mich sehr gut']
}

def USER_EXISTS_WARNING(uid):
    return 'Data for User ID {} already exists! Please enter a different User ID.'.format(uid)
