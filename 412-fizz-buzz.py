"""
Write a program that outputs the string representation of numbers from 1 to n.
But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.
"""


class Solution:
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        str_list = []

        for i in range(1, n + 1):
            string = ''
            if i % 3 == 0:
                string += 'Fizz'
            if i % 5 == 0:
                string += 'Buzz'
            if string == '':
                string += str(i)
            str_list.append(string)

        return str_list


if __name__ == "__main__":
    print(Solution().fizzBuzz(15))
