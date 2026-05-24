def get_average_score(scores):
  return (scores["spanish_score"] + scores["science_score"] + scores["history_score"]) / 3


def is_student_exempted(scores):
  return scores["average_score"] > 70


# Scores
juan_scores = {
  "spanish_score": 75,
	"science_score": 95,
  "history_score": 54,
}
sofia_scores = {
  "spanish_score": 64,
	"science_score": 56,
  "history_score": 98,
}
paul_scores = {
  "spanish_score": 72,
	"science_score": 75,
  "history_score": 79,
}

# Averages
juan_scores["average_score"] = get_average_score(juan_scores)
sofia_scores["average_score"] = get_average_score(sofia_scores)
paul_scores["average_score"] = get_average_score(paul_scores)

juan_scores["is_exempted"] = is_student_exempted(juan_scores)
sofia_scores["is_exempted"] = is_student_exempted(sofia_scores)
paul_scores["is_exempted"] = is_student_exempted(paul_scores)

#o iterando
def get_average_score(scores):
  return (scores["spanish_score"] + scores["science_score"] + scores["history_score"]) / 3


def is_student_exempted(scores):
  return scores["average_score"] > 70


# Scores
students = [
  {
    "name": "Juan",
		"spanish_score": 75,
		"science_score": 95,
		"history_score": 54,
	},
  {
    "name": "Sofia",
		"spanish_score": 64,
		"science_score": 56,
		"history_score": 98,
	},
  {
    "name": "Paul",
		"spanish_score": 72,
		"science_score": 75,
		"history_score": 79,
	}
]

# Averages
for student in students:
  student["average_score"] = get_average_score(student)
  student["is_exempted"] = is_student_exempted(student)
  print(student["name"], " is_exempted is ", student["is_exempted"])


def remove_tenths(numbers_list):
  index = 0
  while (index < len(numbers_list)):
    if numbers_list[index] % 10 == 0:
      numbers_list.pop(index)
    else:
      index += 1


def multiply_numbers_by_2(numbers_list):
  for index, number in enumerate(numbers_list):
    numbers_list[index] = number * 2


def main():
  numbers_list = [53, 60, 32, 62, 400, 10]
  remove_tenths(numbers_list)
  multiply_numbers_by_2(numbers_list)
  print(numbers_list)


if __name__ == "__main__":
  main()