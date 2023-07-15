import pandas as pd
import os


# set the paths to the input and output directories
input_folder = "/News-articles/news_data"
output_folder = "/News-articles/news_cleaned"

def duplicated_article():
    # loop through all files in the input directory
    for filename in os.listdir(input_folder):
        # check if the file is a CSV file
        if filename.endswith(".csv"):
            # construct the full path to the file
            filepath = os.path.join(input_folder, filename)
            # read the CSV file into a pandas dataframe
            df = pd.read_csv(filepath)
            # remove duplicate rows
            df = df.drop_duplicates()
            # construct the full path to the output file
            output_filepath = os.path.join(output_folder, filename)
            # write the dataframe to a new CSV file
            df.to_csv(output_filepath, index=False)


def merge_data():
    # create an empty list to store the individual dataframes
    dfs = []

    # loop through all files in the folder
    for filename in os.listdir(output_folder):
        # check if the file is a CSV file
        if filename.endswith(".csv"):
            # construct the full path to the file
            filepath = os.path.join(output_folder, filename)
            # read the CSV file into a pandas dataframe and append it to the list of dataframes
            df = pd.read_csv(filepath)
            dfs.append(df)

    # concatenate all dataframes into a single dataframe
    merged_df = pd.concat(dfs, ignore_index=True)

    # remove duplicate rows
    merged_df = merged_df.drop_duplicates(subset=["title", "media"])
    merged_df = merged_df.drop_duplicates(subset=["link"])

    # write the merged dataframe to a CSV file
    merged_df.to_csv("news_articles.csv", index=False)

def save_news_agencies():
    # Read the CSV file "news_articles.csv" into a DataFrame
    df = pd.read_csv("../news_articles.csv")

    # Extract unique values from the "media" column and convert them into a list
    data = list(df["media"].unique())

    # Convert each element in the "data" list to a string
    data = [str(x) for x in data]

    # Define the file path where the list will be saved as a text file
    file_path = "/News-articles/my_list.txt"

    # Open the file in write mode and use a context manager ("with" statement) to ensure proper file handling
    with open(file_path, mode="w") as file:
        # Write the elements of the "data" list, separated by newline characters, into the file
        file.write("\n".join(data))
