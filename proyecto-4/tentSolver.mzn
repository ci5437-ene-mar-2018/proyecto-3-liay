% tentSolver.mzn
% Universidad Simon Bolivar
% CI5437: Inteligencia Artificial I
%
% Autores: 
%   - Yarima Luciani 13-10770
%   - Lautaro Villalon 12-10427
%
% Equipo: LIAY
% Prof. Blai Bonet
% Ene-Mar 2018


% ------ INPUT PARAMETERS ------ %

	% Number of rows and columns and their domain
	int: rows;
	int: cols;

	set of int: rowRange = 1..rows;
	set of int: colRange = 1..cols;

	% Row hints and Column hints
	array[rowRange] of int: rowHints;
	array[colRange] of int: colHints;

	% Initial board, trees == 2, blank == 0
	array[rowRange, colRange] of {0, 2}: trees;


% ------ DECISION VARIABLES ------ %

	% Solution board of tents, tents == 1, blank == 0
	array[rowRange, colRange] of var {0, 1}: board;


% ------ CONSTRAINTS ------ %

	% There must be the same amount of tents in a column/row as number expressed in every HINT.
	constraint forall([ sum([board[i,j] | j in colRange]) == rowHints[i] | i in rowRange]);
	constraint forall([ sum([board[i,j] | i in rowRange]) == colHints[j] | j in colRange]);


	% There must be one tent perpendicular to every tree
	constraint forall([

		% corners
	    if i == 1 /\ j == 1 then
	    	board[i+1, j] + board[i, j+1] > 0

	    elseif i == 1 /\ j == cols then
	    	board[i+1, j] + board[i, j-1] > 0

	    elseif i == rows /\ j == 1 then 
	    	board[i-1, j] + board[i, j+1] > 0

	    elseif i == rows /\ j == cols then 
	    	board[i-1, j] + board[i, j-1] > 0
	    
	    % sides
	    elseif i == 1 then 
	    	board[i+1, j] + board[i, j-1] + board[i, j+1] > 0

	    elseif i == rows then 
	    	board[i-1, j] + board[i, j-1] + board[i, j+1] > 0

	    elseif j == 1 then 
	    	board[i, j+1] + board[i-1, j] + board[i+1, j] > 0

	    elseif j == cols then 
	    	board[i, j-1] + board[i-1, j] + board[i+1, j] > 0
	    
	    % inside
	    else board[i - 1, j] + board[i + 1, j] + board[i, j - 1] + board[i, j + 1] > 0 endif

	    | i in rowRange, j in colRange where trees[i, j] == 2]);


	% There can't be a tent over a tree
	constraint forall([

		if trees[i, j] == 2 then
			board[i, j] == 0

		else true endif

		| i in rowRange, j in colRange]);


	% There can't be a tent next to another
	constraint forall([

		% corners
	    if i == 1 /\ j == 1 then
	    	board[i+1, j] + board[i, j+1] + board[i+1, j+1] == 0

	    elseif i == 1 /\ j == cols then
	    	board[i+1, j] + board[i, j-1] + board[i+1, j-1] == 0

	    elseif i == rows /\ j == 1 then 
	    	board[i-1, j] + board[i, j+1] + board[i-1, j+1] == 0

	    elseif i == rows /\ j == cols then 
	    	board[i-1, j] + board[i, j-1] + board[i-1, j-1] == 0
	    
	    % sides
	    elseif i == 1 then 
	    	board[i+1, j] + board[i, j-1] + board[i, j+1] + board[i+1, j-1] + board[i+1, j+1] == 0

	    elseif i == rows then 
	    	board[i-1, j] + board[i, j-1] + board[i, j+1] + board[i-1, j-1] + board[i-1, j+1] == 0

	    elseif j == 1 then 
	    	board[i, j+1] + board[i-1, j] + board[i+1, j] + board[i-1, j+1] + board[i+1, j+1] == 0

	    elseif j == cols then 
	    	board[i, j-1] + board[i-1, j] + board[i+1, j] + board[i-1, j-1] + board[i+1, j-1] == 0
	    
	    % inside
	    else board[i-1, j] + board[i+1, j] + board[i, j-1] + board[i, j+1] + board[i-1, j-1] + board[i-1, j+1] + board[i+1, j-1] + board[i+1, j+1] == 0 endif

	    | i in rowRange, j in colRange where board[i, j] == 1]);


% ------ SOLVER ------ %

	% Search for int values in board that satisfy the constraints and represent the maximum value of its domain (1).
	array[1..(rows*cols)] of var {0, 1}: flatBoard = [board[i, j] | i in rowRange, j in colRange];

	solve :: int_search(flatBoard, input_order, indomain_max, complete) satisfy;


% ------ OUTPUT SOLUTION BOARD ------ %

	output [
			show(if trees[i, j] == 2 then 
					trees[i, j]
				 else board[i, j] endif) ++ 

			if j == cols then
			 	"\n"
			else " " endif 
			| i in rowRange, j in colRange
	       ];