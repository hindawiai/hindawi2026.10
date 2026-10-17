// a stack class, in Java
public class Stack {
  private int[] items = new int[16];
  private int top = 0;
  public void push(int value) { items[top++] = value; }
  public int pop() { return items[--top]; }
  public static void main(String[] args) {
    Stack stack = new Stack();
    for (int value = 1; value <= 3; value++) stack.push(value * 10);
    System.out.println(stack.pop() + " " + stack.pop());
  }
}
