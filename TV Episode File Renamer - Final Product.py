"""
This program is intended to simply rename the files of a TV series in a more readable format.
Since I download different shows from different sources often, and they all have their own file naming styles,
I wanted to automatically rename the files to a more personally preferable format in order to more easily find the episode number in the file name.


There are certain assumptions before using this program:
One folder is processed at a time, with one folder representing one season of a TV series.
The only files in the folder are the episode files.
The episode files are already listed in the desired order within the folder (i.e., episode 1 is before episode 2, which is before episode 3, etc.)
"""

import os


def main():
    print("Welcome to the TV Episode File Renamer!")
    series_name = input("Enter the name of the TV series: ")
    season = input("Enter the season of the series: ")
    num_episodes = int(input("Enter the number of episodes in the season: "))
    folder_path = input("Enter the folder path containing the episodes: ")


    files = os.listdir(folder_path)

    # Check if the number of files matches the number of episodes
    if len(files) != num_episodes:
        print("The number of files in the folder does not match the number of episodes specified.")
        print("Please ensure the folder contains exactly the number of episodes entered and try again.")


    else:
        # Initialize episode_number at 1
        episode_number = 1

        # Process each file in the directory
        for filename in files:
            # Get the file extension
            file_extension = os.path.splitext(filename)[1]  # This extracts the extension, e.g., '.mkv'

            # Create a new name for each episode
            new_name = f"{series_name}_S{season.zfill(2)}E{str(episode_number).zfill(2)}{file_extension}" #.zfill(2) ensures 2 digits for naming, i.e. 1 is 01

            # Construct full file paths
            old_file = os.path.join(folder_path, filename)
            new_file = os.path.join(folder_path, new_name)

            # Rename the file
            os.rename(old_file, new_file)
            print(f"Renamed '{filename}' to '{new_name}'")

            # Increase the episode_number by 1
            episode_number += 1

        print("All files have been renamed successfully!")



if __name__ == "__main__":
    main()