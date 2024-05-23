import os
import shutil


def move_to_train(s_dir, d_dir):
    try:
        shutil.move(s_dir, d_dir)
    except Exception as e:
        print(f"An error occurred: {e}")


def split_and_move_images(source_dir, destination_dir, names_list):
    # creating train and test folder
    train_path = destination_dir + 'train/'
    test_path = destination_dir + 'test/'
    if not os.path.exists(train_path):
        os.makedirs(train_path)
    if not os.path.exists(test_path):
        os.makedirs(test_path)

    for n in names_list:
        move_to_train(os.path.join(source_dir, n), train_path)
        source_path = os.path.join(train_path, n)
        destination_path = os.path.join(test_path, n)

        # Create destination directory if it doesn't exist
        if not os.path.exists(destination_path):
            os.makedirs(destination_path)

        files = os.listdir(source_path)
        num_files = len(files)
        split_index = int(num_files * 0.1)  # taking 90 %

        # Move files to destination directory
        for file_name in files[:split_index]:
            source_file_path = os.path.join(source_path, file_name)
            destination_file_path = os.path.join(destination_path, file_name)
            shutil.move(str(source_file_path), str(destination_file_path))


# Open the file
with open("lfw-deepfunneled/people.txt", "r") as file:
    # Initialize an empty list to store names
    names = []
    # Iterate over each line in the file
    for line in file:
        # Split the line into name and number
        try:
            name, number = line.strip().split('\t')
        except Exception as e:
            continue
        # Convert number to integer
        number = int(number)
        # Check if the number is greater than 1
        if number > 80:
            # Append the name to the list
            names.append(name)


source_directory = "lfw-deepfunneled/lfw-deepfunneled_copy/"
destination_directory = "lfw-deepfunneled/data/"

print('splitting started..')
split_and_move_images(source_directory, destination_directory, names)
print('data updated.')
