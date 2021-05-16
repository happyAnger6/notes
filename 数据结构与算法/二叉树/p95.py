class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def generate_trees(n):
    def gen_subtree(i, j):
        trees = []

        if i == j:
            return [TreeNode(i)]

        if i > j:
            return [None]

        for v in range(i, j+1):
            left_trees = gen_subtree(i, v-1)
            right_trees = gen_subtree(v+1, j)

            for l in left_trees:
                for r in right_trees:
                    parent = TreeNode(v)
                    parent.left = l
                    parent.right = r
                    trees.append(parent)
        return trees

    return gen_subtree(1, n)

if __name__ == "__main__":
    print(generate_trees(3))
