import gradio as gr

# Merge Sort Logic

def merge(left, right, steps, depth):

    i = j = 0
    merged = []

    # Record the start of a merge
    steps.append(
        f"Depth {depth}: MERGE START\n"
        f"  Left : {left}\n"
        f"  Right: {right}"
    )

    # Merge to compare elements from both lists
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # Append the remaining elements.
    while i < len(left):
        merged.append(left[i])
        i += 1

    while j < len(right):
        merged.append(right[j])
        j += 1

    # Record the result of the merge.
    steps.append(
        f"Depth {depth}: MERGE RESULT\n"
        f"  Merged: {merged}"
    )

    return merged


def merge_sort(arr, steps, depth=0):

    # Base case: a list of length 0 or 1 is already sorted.
    if len(arr) <= 1:
        steps.append(
            f"Depth {depth}: BASE CASE\n"
            f"  List: {arr}"
        )
        return arr

    # Find the middle index and split the list in half.
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    # Record the split.
    steps.append(
        f"Depth {depth}: SPLIT\n"
        f"  Original: {arr}\n"
        f"  Left    : {left}\n"
        f"  Right   : {right}"
    )

    # Recursively sort each half (increase depth).
    sorted_left = merge_sort(left, steps, depth + 1)
    sorted_right = merge_sort(right, steps, depth + 1)

    # Merge the two sorted halves.
    return merge(sorted_left, sorted_right, steps, depth)



# Input Parsing & App Logic


def parse_input_list(input_str):
    """
    Convert a comma-separated string of integers into a Python list of ints.

    Example:
        "5, 3, 8, 1" -> [5, 3, 8, 1]

    Raises ValueError if any value is not an integer.
    """
    # Strip whitespace from both ends.
    input_str = input_str.strip()

    # Handle empty input explicitly.
    if not input_str:
        return []

    # Split on commas and convert each part to an integer.
    parts = input_str.split(",")
    result = []
    for p in parts:
        p = p.strip()
        if p == "":
            # Skip blank entries caused by stray commas like "1,2,,3"
            continue
        try:
            value = int(p)
        except ValueError:
            raise ValueError(f"Could not convert '{p}' to an integer.")
        result.append(value)

    return result


def visualize_merge_sort(input_str):
    try:
        numbers = parse_input_list(input_str)
    except ValueError as e:
        # Return error message in the steps output, and an empty sorted list.
        error_msg = f"Input error: {e}\n\nPlease enter a comma separated list of integers, e.g.:\n5, 3, 8, 1"
        return "N/A", error_msg

    # If the list is empty, still handle it gracefully.
    if len(numbers) == 0:
        return "[]", "The list is empty. Nothing to sort."

    steps = []
    sorted_list = merge_sort(numbers, steps, depth=0)

    # Join the recorded steps into a single markdown-friendly string.
    steps_output = "### Merge Sort Steps\n"
    for idx, step in enumerate(steps, start=1):
        steps_output += f"**Step {idx}:**\n{step}\n\n"

    return str(sorted_list), steps_output


# Gradio Interface

with gr.Blocks() as demo:
    gr.Markdown("# Merge Sort Visualizer")
    gr.Markdown(
        "Enter a comma-separated list of integers below. "
        "The app will show each split and merge step of the Merge Sort algorithm."
    )

    with gr.Row():
        input_box = gr.Textbox(
            label="Input List",
            placeholder="Example: 5, 3, 8, 1, 2",
        )

    with gr.Row():
        sorted_output = gr.Textbox(
            label="Sorted List",
            interactive=False
        )
        steps_output = gr.Markdown(
            label="Step-by-Step Merge Sort"
        )

    run_button = gr.Button("Run Merge Sort")

    # Connect the button to the function.
    run_button.click(
        fn=visualize_merge_sort,
        inputs=input_box,
        outputs=[sorted_output, steps_output]
    )

if __name__ == "__main__":
    # Launch the Gradio app when running `python app.py`
    demo.launch()
