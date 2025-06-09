# data_manager.py

import pandas as pd
import os

# --- Constants ---
DATA_DIR = "data"
CSV_PATH = os.path.join(DATA_DIR, "tasks.csv")


# --- Core Data Functions ---

def initialize_data_file():
    """
    Checks if the tasks.csv file exists. If not, create it.
    :return: The loaded DataFrame.
    """
    columns = [
        "task_id",
        "timeline_name",
        "title",
        "caption",
        "is_complete"
    ]

    if not os.path.exists(CSV_PATH):
        print(f"'{CSV_PATH}' not found. Creating a new file.")
        os.makedirs(DATA_DIR, exist_ok=True)
        empty_df = pd.DataFrame(columns=columns)
        # Set the data type for the ID column to allow for missing values (NaN) before the first entry
        empty_df['task_id'] = empty_df['task_id'].astype('Int64')
        empty_df.to_csv(CSV_PATH, index=False)

    return pd.read_csv(CSV_PATH)


def add_task(timeline_name: str, title: str, caption: str):
    """
    Adds a new task to the CSV file.

    Args:
        timeline_name: The name of the timeline the task belongs to.
        title: The main description of the task.
        caption: Extra notes for the task.

    Returns:
        The updated DataFrame.
    """
    # Load the current data
    df = pd.read_csv(CSV_PATH)

    # Determine the new task_id
    if df.empty or df["task_id"].isnull().all():
        new_id = 1
    else:
        new_id = int(df["task_id"].max() + 1)

    # Create a new dictionary for the task
    new_task = {
        "task_id": new_id,
        "timeline_name": timeline_name,
        "title": title,
        "caption": caption,
        "due_date": None,  # New tasks have no due date initially
        "priority": 0,  # Default priority for new tasks
        "is_complete": False  # New tasks are always incomplete
    }

    # Convert the dictionary to a one-row DataFrame and append it
    new_row_df = pd.DataFrame([new_task])
    updated_df = pd.concat([df, new_row_df], ignore_index=True)

    # Save the updated DataFrame back to the CSV
    updated_df.to_csv(CSV_PATH, index=False)

    return updated_df

# You could add more functions here later, like:
# def delete_task(task_id):
#     ...
# def update_task_status(task_id, is_complete):
#     ...