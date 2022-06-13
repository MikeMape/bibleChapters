book = ["Genesis ", "Exodus ", "Leviticus ", "Numbers ", "Deuteronomy ", "Joshua ", "Judges ", "Ruth ", "1 Samuel ", "2 Samuel ", "1 Kings ", "2 Kings ", "1 Chronicles ", "2 Chronicles ", "Ezra ", "Nehemiah ", "Esther ", "Job ", "Psalms ", "Proverbs ", "Ecclesiastes ", "Song of Songs ", "Isaiah ", "Jeremiah ", "Lamentations ", "Ezekiel ", "Daniel ", "Hosea ", "Joel ", "Amos ", "Obadiah ", "Jonah ", "Micah ", "Nahum ", "Habakkuk ", "Zephaniah ", "Haggai ", "Zechariah ", "Malachi ", "Matthew ", "Mark ", "Luke ", "John ", "Acts ", "Romans ", "1 Corinthians ", "2 Corinthians ", "Galatians ", "Ephesians ", "Philippians ", "Colossians ", "1 Thessalonians ", "2 Thessalonians ", "1 Timothy ", "2 Timothy ", "Titus ", "Philemon ", "Hebrews ", "James ", "1 Peter ", "2 Peter ", "1 John ", "2 John ", "3 John ", "Jude ", "Revelation "]
chapter = [51, 41, 28, 37, 35, 25, 22, 5, 32, 25, 23, 26, 30, 37, 11, 14, 11, 43, 151, 32, 13, 9, 67, 53, 6, 49, 13, 15, 4, 10, 2, 5, 8, 4, 4, 4, 3, 15, 5, 29, 17, 25, 22, 29, 17, 17, 14, 7, 7, 5, 5, 6, 4, 7, 5, 4, 2, 14, 6, 6, 4, 6, 2, 2, 2, 23]

bookChoice = 0  # ghbvyuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuut <--My cat walked on the keyboard and i figured I'd leave his contribution.
chapterChoice = 0
while bookChoice <= 65:
    for x in range(1, chapter[chapterChoice]):
        print(book[bookChoice] + str(x))
    bookChoice = bookChoice + 1
    chapterChoice = chapterChoice + 1
