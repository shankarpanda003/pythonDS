def permute(s):
    result = []
    def backtrack(path, remaining):
        if not remaining:
            result.append(path)
            return
        for i in range(len(remaining)):
            print("path",path + remaining[i])
            print("remaining",remaining[:i] + remaining[i+1:])
            backtrack(path + remaining[i], remaining[:i] + remaining[i+1:])
    backtrack("", s)
    return result

# Example usage
if __name__ == "__main__":
    s = "abc"
    print(permute(s))


a, bc
ab,ac