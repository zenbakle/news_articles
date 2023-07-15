import newspaper
import pandas as pd
import json

# Read the CSV file "news_articles.csv" into a DataFrame. This contains all the links for the articles.
df = pd.read_csv("../news_articles.csv")

# Convert the DataFrame to a list of dictionaries, each representing a row in the CSV
csv_reader = df.to_dict("records")

# Loop through each row in the CSV file.
for row in csv_reader:
    try:
        # Create a newspaper.Article object for the current URL
        url_i = newspaper.Article(url="%s" % (row["link"]), language='en')

        # Initialize a variable to keep track of media value
        media_value = 0

        # Download and parse the article content
        url_i.download()
        url_i.parse()

        # Create a new text file with the article content and save in the articles folder
        with open(f'articles/{row["media"]}_{media_value + 1}.txt', 'w') as new_text_file:
            json.dump(url_i.text, new_text_file)

        # Print a message indicating the completion of processing for the current row
        print(f'{row["media"]}: {row["title"]} done')
    except Exception as e:
        # Print an error message if an exception occurs during processing for the current row
        print(f'Error occurred for {row["media"]}: {row["title"]}')
