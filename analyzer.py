'''Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.'''
import numpy as np


class DataAnalytics:
    total_objects = 0

    def __init__(self, data=None):
        self.data = np.array(data) if data is not None else np.array([])
        DataAnalytics.total_objects += 1

    def _get_array_input(self, msg="Enter numbers separated by space: "):
        return np.array([float(x) for x in input(msg).split()])

    def show_array(self):
        print(f"\nArray:\n{self.data}\nShape: {self.data.shape}")

    def create_array(self):
        try:
            dim = int(input("Enter dimension (1, 2 or 3): "))
            nums = self._get_array_input()
            shapes = {
                1: lambda: nums,
                2: lambda: nums.reshape(int(input("Rows: ")), int(input("Columns: "))),
                3: lambda: nums.reshape(int(input("Size 1: ")), int(input("Size 2: ")), int(input("Size 3: ")))
            }
            if dim in shapes:
                self.data = shapes[dim]()
                print("Array created.")
            else:
                print("Only 1D, 2D and 3D are allowed.")
        except ValueError:
            print("Invalid size or numbers.")

    def index_slice(self):
        print(self.data)
        try:
            if self.data.ndim == 1:
                print("Value:", self.data[int(input("Enter index: "))])
            elif self.data.ndim == 2:
                r = int(input("Row index: "))
                print(f"Row: {self.data[r]}\nColumn: {self.data[:, r]}")
            else:
                print("First slice:\n", self.data[0])
        except IndexError:
            print("Index is out of range.")

    def combine(self):
        try:
            other = self._get_array_input("Enter another 1D array: ")
            print("Combined:", np.concatenate((self.data.flatten(), other)))
        except ValueError:
            print("Invalid input.")

    def split_array(self):
        try:
            print("Parts:", np.array_split(self.data, int(input("Number of parts: "))))
        except ValueError:
            print("Invalid number.")

    def math_operations(self):
        try:
            other = self._get_array_input("Enter another array (same size): ")
            a = self.data.flatten()
            if len(a) != len(other):
                return print("Both arrays must have the same number of elements.")

            print(f"Addition: {a + other}\nSubtraction: {a - other}\nMultiplication: {a * other}")
            print("Division:", np.divide(a, other, out=np.zeros_like(a), where=other != 0))

            if self.data.ndim == 2:
                print("Matrix multiplication:\n", self.data @ other.reshape(self.data.shape))
            print("Dot product:", np.dot(a, other))
        except ValueError:
            print("Invalid input.")

    def search_sort_filter(self):
        print("\n1. Search  2. Sort Ascending  3. Sort Descending  4. Filter")
        ch = input("Choose: ")
        try:
            if ch == "1":
                print("Positions:", np.where(self.data == float(input("Value to search: "))))
            elif ch == "2":
                print("Sorted:", np.sort(self.data, axis=None))
            elif ch == "3":
                print("Descending:", np.sort(self.data, axis=None)[::-1])
            elif ch == "4":
                print("Filtered:", self.data[self.data > float(input("Show values greater than: "))])
            else:
                print("Wrong choice.")
        except ValueError:
            print("Invalid value.")

    def statistics(self):
        if self.data.size == 0:
            return print("Create an array first.")

        print(f"\nSum: {np.sum(self.data)}\nMean: {np.mean(self.data)}\nMedian: {np.median(self.data)}")
        print(f"Standard deviation: {round(np.std(self.data), 3)}\nVariance: {round(np.var(self.data), 3)}")
        print(f"Minimum: {np.min(self.data)}\nMaximum: {np.max(self.data)}")

        try:
            print("Percentile:", np.percentile(self.data, float(input("Enter percentile (0-100): "))))
        except ValueError:
            print("Invalid percentile.")

    def correlation(self):
        try:
            other = self._get_array_input("Enter second array: ")
            a = self.data.flatten()
            if len(a) != len(other):
                return print("Arrays must have the same size.")
            print("Correlation coefficient:", np.corrcoef(a, other)[0, 1])
        except ValueError:
            print("Invalid input.")

    @classmethod
    def object_count(cls):
        print("DataAnalytics objects created:", cls.total_objects)

    @staticmethod
    def info():
        print("NumPy Analyzer uses NumPy arrays for basic data analysis.")


def main():
    analyzer = DataAnalytics()
    actions = {
        "1": analyzer.create_array,
        "2": lambda: (analyzer.show_array(), analyzer.index_slice()),
        "3": analyzer.combine,
        "4": analyzer.split_array,
        "5": analyzer.math_operations,
        "6": analyzer.search_sort_filter,
        "7": analyzer.statistics,
        "8": analyzer.correlation,
        "9": DataAnalytics.object_count,
        "10": DataAnalytics.info,
    }

    while True:
        print("\n===== NUMPY ANALYZER =====\n1. Create Array\n2. Show / Index / Slice\n3. Combine Arrays")
        print("4. Split Array\n5. Mathematical Operations\n6. Search / Sort / Filter\n7. Statistics")
        print("8. Correlation\n9. Object Count\n10. Program Info\n11. Exit")

        choice = input("Enter choice: ")
        if choice == "11":
            print("Program ended.")
            break
        actions.get(choice, lambda: print("Invalid choice."))()


if __name__ == "__main__":
    main()
