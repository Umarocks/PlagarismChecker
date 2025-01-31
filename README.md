# Plagiarism Checker Using Google Search and NLP

Front-end of the software is under development, please use WebCrawler.py and modify sequence1 to test the software.

This Python-based plagiarism checker leverages the power of Google Search and Natural Language Processing (NLP) to ensure the originality of content. In under 200 words, here's how it works:

1. **Input Text**: You provide the text or document you want to check for plagiarism.

2. **Google Search**: The tool uses Google's search engine to find web pages with content similar to yours. It extracts snippets from these pages.

3. **NLP Analysis**: Employing NLP techniques, the tool analyzes the provided text and the extracted snippets. It identifies similarities in language, structure, and ideas.

4. **Plagiarism Detection**: The tool highlights potential instances of plagiarism, indicating where similarities have been found. It calculates a similarity score to gauge the extent of overlap.

This plagiarism checker offers a comprehensive solution to maintain the integrity of your content. Whether you're a student, writer, or content creator, it ensures that your work is original and free from unauthorized duplication.

## How it works

The program checks `input_string` in `App.py` and assigns a plagiarism score. By uncommenting lines 72-73 in `App.py` you can also see the URLs for the content the app is comparing the input against in order to verify the app is not presenting a false positive. 

![image](https://github.com/user-attachments/assets/5b57ba2e-b13e-4e97-88e5-79208256b849)

Text that the webcrawler does not find a good match for is likely original, and will recieve a low score.

![Original](https://github.com/user-attachments/assets/9fae12db-75f9-4a43-b061-e45e947e1944)

However, text that the webcrawler finds a highly similar (or exact) match for will recieve a high score, indicating likely plagiarism.
![Plagiarized](https://github.com/user-attachments/assets/1d900716-7d03-46aa-bd70-92f9e9ac246f)

![Less-certain-plagiarized](https://github.com/user-attachments/assets/fab0b549-86c1-4047-9229-6c886aaccfaf)

This application is a proof-of-concept demonstration and is not intended to be used as a definitive authority for reporting plagiarism. It is recommended to manually verify any scores the app presents.
