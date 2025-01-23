# Predictive Analysis for Manufacturing Operations

## Objective
To create a RESTful API to predict machine downtime or production defects using a manufacturing dataset.

## Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/AbhinavKaintura/Predictive-Analysis-for-Manufacturing-Operations.git
   cd predictive_analysis

2.  **Install Dependencies**
    ```bash 
    pip install -r requirements.txt

3.  **Prepare the Dataset**
    Place your dataset in the dataset folder.
    Ensure the dataset has columns: Machine_ID, Temperature, Run_Time, Downtime_Flag.

4.  **Run the Application**
    ```bash
    python app.py

5.   Upload Endpoint (POST /upload)
      ```bash
      curl -X POST -F "file=@path/to/your/dataset.csv" http://127.0.0.1:5000/upload

6.   Train Endpoint (POST /train)
     ```bash
     curl -X POST http://127.0.0.1:5000/train

7.   **Test**
      ```bash
      curl -X POST -H "Content-Type: application/json" -d '{"Temperature": 80, "Run_Time": 120}' http://127.0.0.1:5000/predict
   Here you can provide your own values to Temperature and Run_time so as to test for your own values.

   
![image](https://github.com/user-attachments/assets/59536fe9-2c88-4460-aee5-843cbf398e0d)

8.   ## `dataset/synthetic_data.csv`

This is the synthetic dataset you can use for training and testing.

```csv
Machine_ID,Temperature,Run_Time,Downtime_Flag
1,75,100,0
2,80,120,1
3,78,110,0
4,85,130,1
5,90,140,0
6,82,115,0
7,88,135,1
8,79,105,0
9,81,125,1
10,77,95,0
11,84,130,1
12,83,120,0
13,86,140,1
14,76,100,0
15,87,135,1
16,74,90,0
17,89,140,1
18,80,110,0
19,82,125,1
20,78,105,0
21,85,130,1
22,81,115,0
23,87,135,1
24,79,100,0
25,88,125,1
26,77,95,0
27,84,130,1
28,83,120,0
29,86,140,1
30,76,100,0
31,87,135,1
32,74,90,0
33,89,140,1
34,80,110,0
35,82,125,1
36,78,105,0
37,85,130,1
38,81,115,0
39,87,135,1
40,79,100,0
41,88,125,1
42,77,95,0
43,84,130,1
44,83,120,0
45,86,140,1
46,76,100,0
47,87,135,1
48,74,90,0
49,89,140,1
50,80,110,0
