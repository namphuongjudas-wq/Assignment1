import random

def approximate_pi():
    # Ask the user for the number of random points (N)
    try:
        total_points = int(input("How many random points would you like to generate? "))
    except ValueError:
        print("Please enter a valid integer.")
        return

    points_inside_circle = 0

    for _ in range(total_points):
        # Generate random x and y coordinates between -1 and 1
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        # Check if the point is inside the circle using x^2 + y^2 < 1
        if x**2 + y**2 < 1:
            points_inside_circle += 1

    # Calculate pi using the formula: pi ≈ 4 * (n / N)
    pi_approximation = 4 * (points_inside_circle / total_points)

    print(f"\nAfter generating {total_points} points:")
    print(f"Points inside circle (n): {points_inside_circle}")
    print(f"Approximation of pi: {pi_approximation}")

if __name__ == "__main__":
    approximate_pi()