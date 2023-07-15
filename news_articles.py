from GoogleNews import GoogleNews
import pandas as pd

news_stations = [
    'pulse nigeria',
    'punch newspaper',
    'Ripples Nigeria',
    'Sahara Reporters',
    'Sundiata Post',
]

# Iterate over each news agency in the list 'news_stations'
for news_agency in news_stations:
    all_df = pd.DataFrame()  # Create an empty DataFrame to store all page articles

    # Loop through 30 pages of search results
    for page in range(30):
        news = GoogleNews(start="01/01/2022", end="12/31/2022")  # Initialize GoogleNews object
        news.search(news_agency)  # Search for articles related to the current news agency
        news.get_page(page + 1)  # Retrieve the specified page of search results
        result = news.result()  # Get the result (articles) for the current page
        data = pd.DataFrame.from_dict(result)  # Convert the result to a DataFrame
        all_df = pd.concat([all_df, data], ignore_index=True)  # Append the current page's data to the overall DataFrame
        news.clear()  # Clear the GoogleNews object to prepare for the next page of results
        print(page + 1)  # Print the current page number

    print(all_df.shape)  # Print the shape (rows, columns) of the DataFrame containing all articles

    # Save the DataFrame as a CSV file with a name based on the news agency
    all_df.to_csv(f"news_datas/news_site_{news_agency.replace(' ', '_')}.csv", index=False)

    print(f"Current News agency: {news_agency}")  # Print the current news agency being processed
