#include <stdio.h>
#include <stdlib.h>

struct node {
    int key;
    struct node *left;
    struct node *right;
};

struct node *create_node(int key) {
    struct node *temp = malloc(sizeof(struct node));
    temp->key = key;
    temp->left = NULL;
    temp->right = NULL;
    return temp;
}

struct node *insert(struct node *root, int key) {
    if (root == NULL)
        return create_node(key);
    if (key < root->key)
        root->left = insert(root->left, key);
    else if (key > root->key)
        root->right = insert(root->right, key);
    return root;
}

struct node *search(struct node *root, int key) {
    if (root == NULL || root->key == key)
        return root;
    if (key < root->key)
        return search(root->left, key);
    return search(root->right, key);
}

struct node *min_value_node(struct node *node) {
    struct node *current = node;
    while (current && current->left != NULL)
        current = current->left;
    return current;
}

struct node *delete_node(struct node *root, int key) {
    if (root == NULL)
        return root;
    if (key < root->key)
        root->left = delete_node(root->left, key);
    else if (key > root->key)
        root->right = delete_node(root->right, key);
    else {
        if (root->left == NULL) {
            struct node *temp = root->right;
            free(root);
            return temp;
        } else if (root->right == NULL) {
            struct node *temp = root->left;
            free(root);
            return temp;
        }
        struct node *temp = min_value_node(root->right);
        root->key = temp->key;
        root->right = delete_node(root->right, temp->key);
    }
    return root;
}

void inorder(struct node *root) {
    if (root != NULL) {
        inorder(root->left);
        printf("%d ", root->key);
        inorder(root->right);
    }
}

int height(struct node *root) {
    if (root == NULL)
        return 0;
    int left_height = height(root->left);
    int right_height = height(root->right);
    return (left_height > right_height ? left_height : right_height) + 1;
}

int main() {
    struct node *root = NULL;
    int values[] = {50, 30, 70, 20, 40, 60, 80};
    int size = 7;
    for (int index = 0; index < size; index++)
        root = insert(root, values[index]);
    printf("Inorder: ");
    inorder(root);
    printf("\nHeight: %d\n", height(root));
    root = delete_node(root, 30);
    printf("After delete 30: ");
    inorder(root);
    printf("\n");
    struct node *found = search(root, 60);
    printf("Search 60: %s\n", found ? "found" : "not found");
    return 0;
}
