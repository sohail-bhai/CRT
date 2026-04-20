"""
Backtracking Practice Set

"""


def subset_sum_exists(nums, target):
	"""
	Question 1: Subset Sum Decision
	Problem:
	Given a list of integers and a target, check whether any subset sums to target.

	Explanation:
	At each index we have two choices: include the current element or skip it.
	We recursively explore both choices and stop early if target is reached.
	"""

	def backtrack(i, current_sum):
		if current_sum == target:
			return True
		if i == len(nums):
			return False
		return backtrack(i + 1, current_sum + nums[i]) or backtrack(i + 1, current_sum)

	return backtrack(0, 0)


def generate_permutations(nums):
	"""
	Question 2: Generate All Permutations
	Problem:
	Return all permutations of a list of distinct numbers.

	Explanation:
	Build one permutation step by step.
	Track which elements are already used.
	When the current path length equals n, store one full permutation.
	"""

	result = []
	used = [False] * len(nums)
	path = []

	def backtrack():
		if len(path) == len(nums):
			result.append(path[:])
			return

		for i in range(len(nums)):
			if not used[i]:
				used[i] = True
				path.append(nums[i])
				backtrack()
				path.pop()
				used[i] = False

	backtrack()
	return result


def solve_n_queens(n):
	"""
	Question 3: N-Queens
	Problem:
	Place n queens on an n x n board so that no two queens attack each other.
	Return all valid board arrangements.

	Explanation:
	Place one queen row by row.
	A position is valid if column, main diagonal, and anti-diagonal are free.
	If all rows are placed, one solution is found.
	"""

	board = [["."] * n for _ in range(n)]
	cols = set()
	diag1 = set()
	diag2 = set()
	answers = []

	def backtrack(r):
		if r == n:
			answers.append(["".join(row) for row in board])
			return

		for c in range(n):
			if c in cols or (r - c) in diag1 or (r + c) in diag2:
				continue

			cols.add(c)
			diag1.add(r - c)
			diag2.add(r + c)
			board[r][c] = "Q"

			backtrack(r + 1)

			board[r][c] = "."
			cols.remove(c)
			diag1.remove(r - c)
			diag2.remove(r + c)

	backtrack(0)
	return answers


def rat_in_maze_paths(maze):
	"""
	Question 4: Rat in a Maze (All Paths)
	Problem:
	Given an n x n binary matrix where 1 means open and 0 means blocked,
	find all paths from top-left to bottom-right using moves D, L, R, U.

	Explanation:
	Use backtracking to move in 4 directions.
	Mark current cell as visited before exploring neighbors and unmark while returning.
	Add path when destination is reached.
	"""

	n = len(maze)
	if n == 0 or maze[0][0] == 0 or maze[n - 1][n - 1] == 0:
		return []

	directions = [(1, 0, "D"), (0, -1, "L"), (0, 1, "R"), (-1, 0, "U")]
	visited = [[False] * n for _ in range(n)]
	paths = []

	def backtrack(r, c, path):
		if r == n - 1 and c == n - 1:
			paths.append(path)
			return

		visited[r][c] = True

		for dr, dc, move in directions:
			nr, nc = r + dr, c + dc
			if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc] and maze[nr][nc] == 1:
				backtrack(nr, nc, path + move)

		visited[r][c] = False

	backtrack(0, 0, "")
	return paths


def word_search(board, word):
	"""
	Question 5: Word Search
	Problem:
	Given a grid of letters and a word, check if the word exists in the grid.
	Adjacent cells are horizontal or vertical, and one cell cannot be reused.

	Explanation:
	Start from every cell.
	Perform DFS + backtracking matching one character at a time.
	If all characters are matched, return True.
	"""

	if not board or not board[0]:
		return False

	rows, cols = len(board), len(board[0])

	def backtrack(r, c, i):
		if i == len(word):
			return True
		if r < 0 or c < 0 or r >= rows or c >= cols:
			return False
		if board[r][c] != word[i]:
			return False

		temp = board[r][c]
		board[r][c] = "#"

		found = (
			backtrack(r + 1, c, i + 1)
			or backtrack(r - 1, c, i + 1)
			or backtrack(r, c + 1, i + 1)
			or backtrack(r, c - 1, i + 1)
		)

		board[r][c] = temp
		return found

	for r in range(rows):
		for c in range(cols):
			if backtrack(r, c, 0):
				return True

	return False


if __name__ == "__main__":
	print("Question 1: Subset Sum")
	print(subset_sum_exists([3, 34, 4, 12, 5, 2], 9))
	print()

	print("Question 2: Permutations")
	print(generate_permutations([1, 2, 3]))
	print()

	print("Question 3: N-Queens (n=4)")
	queens_solutions = solve_n_queens(4)
	print("Total solutions:", len(queens_solutions))
	for sol in queens_solutions:
		for row in sol:
			print(row)
		print()

	print("Question 4: Rat in a Maze")
	sample_maze = [
		[1, 0, 0, 0],
		[1, 1, 0, 1],
		[1, 1, 0, 0],
		[0, 1, 1, 1],
	]
	print(rat_in_maze_paths(sample_maze))
	print()

	print("Question 5: Word Search")
	sample_board = [
		["A", "B", "C", "E"],
		["S", "F", "C", "S"],
		["A", "D", "E", "E"],
	]
	print(word_search(sample_board, "ABCCED"))
 