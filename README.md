# Iceberg-Cube

This project has 2 main phases:

  1) Preprocessing Data: reading Dataset.txt and determining which dimensions each item of data has. Results       are saved in output.csv
  2) Implementation of Iceberg Cube using BUC method:
     
     - load_data(): read preprocessed data and save them in a 2-d array
     - create_cuboids(): This function computes the complete data cube with all the cells by means of the            internal recursion funcsion (top to bottom manner) and returns the output in a dictionary.
     - get_count():This function takes all the data and a cell as input and calculates how many rows of the   
       data correspond to the desired cell.
     - contain(): This function takes two lists as input and checks whether the first list contains the     
       second list or not. If it is included, it will return True and otherwise, it will return False.
     -BUC(): The main function of the code that creates the data cube using the BUC method. At first,
      create_cuboids() creates the complete cube with all the cells. Then, using the get_count() function, it       obtains the measure corresponding to each of the cells. And if the measure corresponding to that 
      cell is less than the min_sup value, that cell is deleted. and finally prints the final output.
