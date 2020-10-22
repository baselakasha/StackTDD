package com.stacktdd.test;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertTrue;

import org.junit.Before;
import org.junit.Test;

import com.stacktdd.Impl.Stack;

public class StackTest {

  Stack<Integer> stack;

  @Before
  public void setup() {
    stack = new Stack<Integer>();
  }

  @Test
  public void testEmptyStack() {
    assertTrue(stack.isEmpty());
    assertEquals(stack.size(), 0);
  }

  @Test(expected = Exception.class)
  public void testPopOnEmpty() {
    stack.pop();
  }

  @Test(expected = Exception.class)
  public void testPeekOnEmpty() {
    stack.peek();
  }

  @Test
  public void testPush() {
    stack.push(12);
    assertEquals(stack.size(), 1);
  }

  @Test
  public void testPeek() {
    stack.push(2);
    stack.push(15);
    assertTrue(stack.peek() == 15);
    assertEquals(stack.size(), 2);
  }

  @Test
  public void testPop() {
    stack.push(18);
    assertTrue(stack.pop() == 18);
    assertEquals(stack.size(), 0);
  }

  @Test
  public void testExhaustively() {
    stack.push(10);
    assertTrue(!stack.isEmpty());
    stack.push(20);
    assertEquals(stack.size(), 2);
    assertTrue(stack.peek() == 20);
    assertEquals(stack.size(), 2);
    assertTrue(stack.pop() == 20);
    assertEquals(stack.size(), 1);
    assertTrue(stack.peek() == 10);
    assertEquals(stack.size(), 1);
    assertTrue(stack.pop() == 10);
    assertEquals(stack.size(), 0);
    assertTrue(stack.isEmpty());
  }
}
