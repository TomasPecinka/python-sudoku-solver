# python-sudoku-solver
Console-based python program which solves all kinds of sudoku boards using <a href="https://en.wikipedia.org/wiki/Sudoku_solving_algorithms#Backtracking"><strong>backtracking algorithm</strong></a>, which is a type of brute force searching algorithms. <br>
Game board is represented by 9x9 matrix, blank fields are displayed as zeros. <br>
The entire program is divided into 4 python functions:
<ul>
  <li><strong>print_board()</strong> - prints board to a console in more readable way than just list of lists</li>
  <li><strong>find_empty()</strong> - finds position where the number is 0, which means that the field is blank, function returns blank field coordinates in a python list [x_coordinate, y_coordinate]</li>
  <li><strong>validate_board()</strong> - checks if the board complies with the sudoku rules - if number is only used once in row, column, and subsquare</li>
  <li><strong>solve_board()</strong> 
    <ul>
      <li>calls find_empty() to check if there are empty squares on the board, if no, the board is solved and function ends here</li>
      <li>generate number from 1 to 9 and call validate_board() with this number, if it fits, the number is added to the board</li>
      <li>recursively call function solve_board() again with updated parameter</li>
    <ul>
  </li>
</ul>
    
![Image of Console](https://github.com/p-tomas/python-sudoku-solver/blob/main/console_output.png)
