# **CISC121_Project**
Interactive Python + Gradio app displaying a Merge Sort algorithm step-by-step for CISC-121 Project

# **Merge Sort Visualizer**
This project is an interactive Python application that demonstrates how the Merge Sort algorithm works. The user enters a list of integers, and the program shows the splitting and merging steps until the list is fully sorted. The purpose of the project is to make the divide-and-conquer approach easier to understand by visualizing it.

## **Screenshots of test**
### Starting Display
![Test Screenshot 1](Screenshot%202025-12-09%20215808.png)

### Input List of Integers
![Test Screenshot 2](Screenshot%202025-12-09%20215903.png)

### 
![Test Screenshot 3](Screenshot%202025-12-09%20215917.png)

## **Why I Chose Merge Sort**
I chose Merge Sort because the divide and conquer system discussed in class, is very fast at sorting lists which is very interesting to me. It also has a consistent time complexity of O(n log n), unlike Bubble Sort or Insertion Sort which can be slower in the worst case. Since Merge Sort produces middle steps automatically, it works well for all list sizes unlike bubble sort where as the list grows the time complexity of O(n^2) gets exponentially less efficient. I could have chosen Binary search or Linear Search to give myself an 'easier' project to code and breakdown however it's much more interesting diving deep into something I'll actually be interested in learning about such as Merge Sort which is extremely efficient.

## **Computational Thinking Breakdown**

**Decomposition:**  
- Take input and convert it into a list of integers  
- Recursively divide the list into two halves  
- Sort each half  
- Merge the sorted halves into one list  
- Display each split and merge step

**Pattern Recognition:**  
- Every recursive call performs the same sequence: *split, sort, merge*  
- The merge step repeatedly compares two lists and builds a new sorted one  
- This pattern continues until the entire list is sorted

**Abstraction:**  
- You do not need to show the app user how to understand recursion or index manipulation  
- Only show the merge steps and final sorted list

**Algorithm Design:**  
Input (list of integers), split recursively, merge sorted halves, output final sorted list

## **How to Run the Program**

#### 1. Clone the repository:

[git-clone: https://huggingface.co/spaces/<username>/<space-name>](https://huggingface.co/spaces/compscimichael/CISC121_Project)


#### 2. Install required libraries:

pip install -r requirements.txt

#### 3. Run the app:

python app.py

A Gradio interface will open in the user's browser. After you will be prompted to enter (a comma-separated) list of integers and then click submit.

## **Testing**

The program was tested using:
- Random integer lists
- Sorted lists
- Reverse-sorted lists
- Lists with duplicate values
- Single element lists
- An empty set

In all cases, the output matched Python’s built-in `sorted()` function.

## **Hugging Face Link**

https://huggingface.co/spaces/compscimichael/CISC121_Project

## Files Included

- `app.py` : Merge Sort implemented into to a Gradio interface  
- `requirements.txt` : required libraries
- `README.md` : project documentation
- `screenshot.png` : short animation of the app running

## **Author and Acknowledgement**

K. Michael MacNeill  
CISC-121 - Section 001  
Fall 2025

Developed using Python, Gradio, and ChatGPT (up to level-4)
