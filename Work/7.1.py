def avg(x, *more):
    try:
        return float(x+sum(more)) / (1+len(more))
    except Exception as e:
        print(f"An error occurred:  {e}")